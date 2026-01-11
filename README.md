# 📊 Vendor Performance Analysis – End-to-End Data Analytics Project

## 🔍 Project Overview

This report is based on the **Vendor Performance Analysis** project, where an end-to-end data analytics workflow was implemented. The project covers:

* Data understanding and preparation
* Exploratory Data Analysis (EDA) using Python
* SQL queries for business-level aggregations
* Power BI dashboard creation
* Extraction of meaningful, business-focused insights

The objective is to evaluate **vendor and brand performance** in terms of sales, purchases, profitability, and contribution to overall business revenue.

---

## ❓ Business Questions & Answers

### Q1. Which vendors and brands demonstrate the highest sales performance?

**Answer:**
Using EDA and SQL aggregation on total sales quantity and total sales dollars:

* A small group of top vendors contributes a disproportionately large share of total sales.
* Certain brands consistently appear in the top tier across both **sales quantity** and **sales value**, indicating strong market demand and customer preference.

**Business Insight:**
These vendors and brands should be treated as **key revenue drivers**. Priority should be given to inventory availability, contract retention, and strategic partnerships with them.

---

### Q2. Which vendors contribute the most to total purchase dollars?

**Answer:**
SQL queries were used to summarize **Total Purchase Dollars by Vendor**.

* A limited number of vendors account for the majority of purchase spending.
* Some vendors show high purchase value but relatively lower sales contribution.

**Business Insight:**
High purchase dependency on a few vendors increases **supply-chain risk**. The business should consider vendor diversification or renegotiation of purchase terms.

---

### Q3. Identify brands that need promotional or pricing attention.

**Answer:**
By comparing:

* Sales quantity
* Sales dollars
* Profit margin

It was observed that:

* Certain brands have **low sales volume but high profit margins**.
* Other brands have **high sales volume but low margins**.

**Business Insight:**

* Low-sales, high-margin brands may benefit from **targeted promotions** to increase volume.
* High-sales, low-margin brands require **cost optimization or price revision** strategies.

---

### Q4. Which vendors show low sales performance but higher profitability?

**Answer:**
EDA revealed that:

* Some vendors generate modest sales but maintain strong margins.
* These vendors operate efficiently or sell premium products.

**Business Insight:**
Such vendors should not be eliminated based solely on sales volume. They represent **niche profitability opportunities** and can be positioned as premium or specialty suppliers.

---

### Q5. What is the overall sales and purchase distribution across vendors?

**Answer:**
Distribution analysis showed:

* A **right-skewed distribution**, where a few vendors dominate sales and purchases.
* Long-tail vendors contribute minimally on an individual basis but collectively add value.

**Business Insight:**
The business follows a **Pareto (80/20) pattern**, where focusing on top vendors yields maximum impact while selectively optimizing long-tail vendors.

---

## 📈 Exploratory Data Analysis (EDA)

EDA was performed using Python to:

* Check data quality and missing values
* Analyze distributions of sales, purchases, and profit
* Identify outliers and performance extremes
* Compare vendor-level and brand-level metrics

**Key Observations:**

* Strong correlation between purchase volume and sales value
* Noticeable variation in profit margins across brands
* Presence of outlier vendors with unusually high contribution

---

## 🗄️ SQL Analysis

SQL queries were used for:

* Vendor-wise and brand-wise aggregation
* Calculation of total sales, total purchases, and contribution percentages
* Ranking vendors based on performance metrics

**Value of SQL:**
SQL enabled efficient transformation of raw transactional data into **business-ready summary tables**, which were later used in Power BI.

---

## 📊 Power BI Dashboard

A Power BI dashboard was created to visualize:

* Top vendors by sales and purchases
* Brand-level performance comparison
* Contribution percentage of vendors
* Key KPIs such as Total Sales, Total Purchases, and Profit

**Dashboard Benefits:**

* Interactive filtering by vendor and brand
* Quick identification of top and underperforming entities
* Executive-level visibility into business performance

---

## 💡 Key Business Insights

* Sales and purchases are highly concentrated among a few vendors.
* Not all high-purchase vendors translate into high sales, indicating inefficiencies.
* Profitability varies significantly across brands, independent of sales volume.
* Promotional strategies should be data-driven rather than volume-driven.

---

## ✅ Conclusion

This project demonstrates a complete **end-to-end data analytics solution**, combining Python (EDA), SQL (data aggregation), and Power BI (visual storytelling). The insights generated can support:

* Vendor negotiation strategies
* Inventory planning
* Pricing and promotion decisions
* Risk reduction in vendor dependency

Overall, the analysis provides **actionable, business-meaningful insights** that enable data-driven decision-making.

---

---

## 🧰 Tools & Technologies Used

* **Python** (Pandas, NumPy, Matplotlib, Seaborn)
* **SQL** (CTEs, Aggregations, Ranking)
* **Power BI** (Interactive Dashboards & KPIs)
* **Jupyter Notebook** (EDA & Analysis)

## 📂 Project Structure

```
├── data/                  # Raw and cleaned datasets
├── notebooks/             # Jupyter notebooks for EDA
├── sql/                   # SQL queries used for analysis
├── powerbi/               # Power BI dashboard file (.pbix)
├── README.md              # Project documentation
```

## 📌 How to Use This Project

1. Review the Jupyter Notebook for EDA and data preparation.
2. Execute SQL queries to generate vendor and brand summaries.
3. Open the Power BI file to explore interactive dashboards.
4. Refer to the insights section for business recommendations.

---

### 👤 Author

**Saurabh Kushwaha**
Data Analyst | Python | SQL | Power BI
