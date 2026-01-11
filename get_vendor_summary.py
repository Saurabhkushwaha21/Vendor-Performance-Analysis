import pandas as pd
import logging
from inventory_data.ingestion import ingest_db
from sqlalchemy import create_engine
import numpy as np

logging.basicConfig(
    filename="logs/get_vendor_summary.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

def create_vendor_summary(engine):
    query = """
    WITH sales_agg AS (
        SELECT VendorNo, Brand,
               SUM(SalesQuantity) AS TotalsalesQuantity,
               SUM(SalesDollars) AS TotalsalesDollers,
               SUM(SalesPrice) AS TotalsalesPrice,
               SUM(ExciseTax) AS TotalsalesExciseTax
        FROM sales
        GROUP BY VendorNo, Brand
    ),
    purchase_agg AS (
        SELECT VendorNumber,
               SUM(Quantity) AS TotalpurchaseQuantity,
               SUM(Dollars) AS TotalPurchaseDollars,
               SUM(Freight) AS FreightCost
        FROM vendor_invoice
        GROUP BY VendorNumber
    )
    SELECT
        pp.VendorNumber, pp.VendorName, pp.Brand, pp.Description,
        pp.Price AS Actual_Price, pp.PurchasePrice, pp.Volume,
        sa.TotalsalesQuantity, sa.TotalsalesDollers,
        sa.TotalsalesPrice, sa.TotalsalesExciseTax,
        pa.TotalpurchaseQuantity, pa.TotalPurchaseDollars, pa.FreightCost
    FROM purchase_prices pp
    LEFT JOIN sales_agg sa
        ON pp.VendorNumber = sa.VendorNo AND pp.Brand = sa.Brand
    LEFT JOIN purchase_agg pa
        ON pp.VendorNumber = pa.VendorNumber;
    """
    return pd.read_sql(query, engine)

def clean_data(df):
    df['Volume'] = pd.to_numeric(df['Volume'], errors='coerce')
    df.fillna(0, inplace=True)

    df['VendorName'] = df['VendorName'].str.strip()
    df['Description'] = df['Description'].str.strip()

    # Calculate GrossProfit
    df['GrossProfit'] = df['TotalsalesDollers'] - df['TotalPurchaseDollars']

    # Calculate StockturnOver and SalesPurchaseRate safely to avoid inf
    df['StockturnOver'] = np.where(df['TotalpurchaseQuantity'] != 0,
                                   df['TotalsalesQuantity'] / df['TotalpurchaseQuantity'], 0)
    df['SalesPurchaseRate'] = np.where(df['TotalPurchaseDollars'] != 0,
                                       df['TotalsalesDollers'] / df['TotalPurchaseDollars'], 0)

    # Replace any remaining inf/-inf with 0
    df.replace([np.inf, -np.inf], 0, inplace=True)

    return df

if __name__ == "__main__":
    # SQLAlchemy engine
    engine = create_engine("mysql+pymysql://root:saurabh%40123@localhost/inventory")

    logging.info("Creating vendor summary table")
    summary_df = create_vendor_summary(engine)
    logging.info(summary_df.head())

    logging.info("Cleaning data")
    clean_df = clean_data(summary_df)
    logging.info(clean_df.head())

    logging.info("Ingesting data")
    ingest_db(clean_df, "vendor_sales_summary", engine)

    logging.info("Completed successfully")
