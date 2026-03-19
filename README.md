# 📱 PhonePe Transaction Insights
### End-to-End Data Engineering & Exploratory Data Analysis on India's Digital Payment Ecosystem

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue?logo=postgresql)
![Pandas](https://img.shields.io/badge/Pandas-2.x-green?logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-orange)
![Seaborn](https://img.shields.io/badge/Seaborn-0.12+-teal)
![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

---
## 🚀 Live Demo

> **[Click here to open the live dashboard](https://phonepe-transaction-insights-p6kyoz4r2zcpsnjkn6hpab.streamlit.app)**

## 📌 Table of Contents

- [Project Overview](#project-overview)
- [Business Problem Statement](#business-problem-statement)
- [Dataset Description](#dataset-description)
- [Project Architecture](#project-architecture)
- [Directory Structure](#directory-structure)
- [Tech Stack](#tech-stack)
- [ETL Pipeline](#etl-pipeline)
- [Database Schema](#database-schema)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Key Insights & Findings](#key-insights--findings)
- [Charts Gallery](#charts-gallery)
- [How to Run](#how-to-run)
- [Database Restore](#database-restore)
- [Future Enhancements](#future-enhancements)
- [Data Source](#data-source)
- [Author](#author)

---

## 📖 Project Overview

**PhonePe Transaction Insights** is a full-stack data engineering and analytics project built on top of the publicly available **PhonePe Pulse** dataset — the same data that powers [PhonePe Pulse](https://www.phonepe.com/pulse/), India's most comprehensive digital payments intelligence platform.

This project covers the **entire data lifecycle**:
1. Raw JSON ingestion from PhonePe Pulse GitHub repository
2. Schema design and ETL into a relational PostgreSQL database
3. SQL-based aggregations and feature derivation
4. Rich Exploratory Data Analysis (EDA) with 22 publication-quality charts
5. Full database backup for reproducibility

The goal is to uncover **actionable insights** into how India's 1.4 billion citizens are transacting digitally — across states, districts, device brands, payment categories, and insurance adoption — from **2018 to 2024**.

---

## 💼 Business Problem Statement

India has witnessed an unprecedented surge in digital payments, driven by UPI adoption. However, understanding **where**, **how**, and **how much** people transact — and how insurance adoption is growing alongside payments — requires structured analysis of massive, multi-dimensional data.

**Key business questions this project answers:**
- Which states drive the highest transaction volumes and amounts?
- How is PhonePe's insurance vertical growing quarter-over-quarter?
- What device brands are most common among PhonePe users?
- Which districts are digital payment leaders vs. laggards?
- What is the year-over-year growth trajectory of UPI transactions?
- How does average transaction value vary across states?
- Is there a seasonal pattern in quarterly transactions?
- What is the relationship between user count and transaction amount?

---

## 📦 Dataset Description

Data sourced from the official **[PhonePe Pulse GitHub Repository](https://github.com/PhonePe/pulse)** — an open data initiative covering **2,000+ crore anonymized UPI transactions**.

### Data Sections

| Section | Type | Description |
|---|---|---|
| **Aggregated** | Transactions | Payment category-wise aggregated transaction count & amount at country/state level |
| **Aggregated** | Users | Registered & app-opened users by state, year, quarter |
| **Aggregated** | Insurance | Insurance policy count & premium amount by state |
| **Map** | Transactions | Total transaction count & amount at state & district level |
| **Map** | Users | Registered users at state & district level |
| **Map** | Insurance | Insurance metrics at state & district level |
| **Top** | Transactions | Top states, districts, pin codes by transaction volume |
| **Top** | Users | Top states, districts, pin codes by registered users |
| **Top** | Insurance | Top states, districts by insurance metrics |

### Data Dimensions

| Attribute | Details |
|---|---|
| **Time Range** | 2018 Q1 → 2024 Q4 |
| **Granularity** | Country → State → District → Pin Code |
| **Format (Raw)** | JSON (hierarchical, nested) |
| **Format (Processed)** | PostgreSQL relational tables |
| **Raw Data Size** | ~150 MB |
| **DB Backup Size** | 6.6 MB (compressed SQL dump) |

### Transaction Types Covered
- **Peer-to-Peer (P2P)** payments
- **Peer-to-Merchant (P2M)** payments
- **Recharge & Bill Payments**
- **Financial Services**
- **Others**

---

## 🏗️ Project Architecture

```
PhonePe Pulse GitHub (Raw JSON)
            │
            ▼
    ┌──────────────────┐
    │   ETL Pipeline   │  ← Python (json, os, pandas)
    │  (etl/ scripts)  │
    └────────┬─────────┘
             │  Cleaned DataFrames
             ▼
    ┌──────────────────┐
    │  PostgreSQL DB   │  ← psycopg2 / SQLAlchemy
    │ (database/ init) │
    └────────┬─────────┘
             │  SQL Queries
             ▼
    ┌──────────────────┐
    │  EDA & Analysis  │  ← Pandas, Matplotlib, Seaborn
    │ (notebooks/ &    │
    │  analysis/)      │
    └────────┬─────────┘
             │  22 PNG Charts
             ▼
    ┌──────────────────┐
    │  Insights Report │  ← analysis/charts/
    │  (docs/)         │
    └──────────────────┘
```

---

## 📁 Directory Structure

```
PhonePe_Transaction_Insights/
│
├── 📂 data/                          # Raw PhonePe Pulse JSON data (gitignored, ~150MB)
│   ├── aggregated/
│   │   ├── transaction/
│   │   │   └── country/india/
│   │   │       ├── YYYY/Q.json
│   │   │       └── state/<state>/YYYY/Q.json
│   │   ├── user/
│   │   └── insurance/
│   ├── map/
│   └── top/
│
├── 📂 etl/                           # ETL extraction & transformation scripts
│   ├── extract_aggregated.py
│   ├── extract_map.py
│   ├── extract_top.py
│   └── load_to_db.py
│
├── 📂 database/                      # Database initialization & schema
│   ├── schema.sql
│   └── db_config.py
│
├── 📂 notebooks/                     # Jupyter notebooks for EDA
│   ├── 01_data_exploration.ipynb
│   ├── 02_transaction_analysis.ipynb
│   ├── 03_user_brand_analysis.ipynb
│   ├── 04_insurance_analysis.ipynb
│   └── 05_district_state_analysis.ipynb
│
├── 📂 analysis/
│   └── charts/                       # All 22 EDA output charts (PNG)
│       ├── 01_top10_states_amount.png
│       ├── 02_top10_states_count.png
│       ├── 03_txn_type_pie.png
│       ├── 04_txn_type_bar.png
│       ├── 05_quarterly_amount_trend.png
│       ├── 06_quarterly_count_trend.png
│       ├── 07_brand_user_count.png
│       ├── 08_brand_pie.png
│       ├── 09_insurance_policy_growth.png
│       ├── 10_insurance_premium_trend.png
│       ├── 11_top10_districts.png
│       ├── 12_state_registered_users.png
│       ├── 13_yearly_amount.png
│       ├── 14_yearly_insurance.png
│       ├── 15_avg_txn_value_state.png
│       ├── 16_state_year_heatmap.png
│       ├── 17_quarterly_seasonality.png
│       ├── 18_avg_premium_per_policy.png
│       ├── 19_scatter_count_vs_amount.png
│       ├── 20_dual_axis_count_amount.png
│       ├── 21_top10_dist_grouped.png
│       └── 22_odisha_districts.png
│
├── 📂 assets/
├── 📂 docs/
├── phonepe_pulse_backup.sql
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Language** | Python 3.10+ | Core scripting, ETL, EDA |
| **Data Extraction** | `os`, `json`, `glob` | Traverse & parse nested JSON files |
| **Data Manipulation** | `pandas`, `numpy` | DataFrames, aggregations, transforms |
| **Database** | PostgreSQL 15 | Relational storage & SQL analytics |
| **DB Connector** | `psycopg2`, `SQLAlchemy` | Python ↔ PostgreSQL bridge |
| **Visualization** | `matplotlib`, `seaborn` | 22 publication-quality EDA charts |
| **Notebooks** | Jupyter Notebook / JupyterLab | Interactive analysis |
| **Version Control** | Git + GitHub | Source control |
| **Environment** | Python `venv` | Dependency isolation |

---

## ⚙️ ETL Pipeline

### Step 1 — Extraction

```python
import os, json, pandas as pd

def extract_aggregated_transactions(base_path):
    records = []
    for state in os.listdir(f"{base_path}/state"):
        for year in os.listdir(f"{base_path}/state/{state}"):
            for file in os.listdir(f"{base_path}/state/{state}/{year}"):
                quarter = file.replace(".json", "")
                with open(f"{base_path}/state/{state}/{year}/{file}") as f:
                    data = json.load(f)
                for txn in data["data"]["transactionData"]:
                    records.append({
                        "state": state, "year": int(year),
                        "quarter": int(quarter),
                        "transaction_type": txn["name"],
                        "transaction_count": txn["paymentInstruments"]["count"],
                        "transaction_amount": txn["paymentInstruments"]["amount"]
                    })
    return pd.DataFrame(records)
```

### Step 2 — Transformation
- Normalize state names (e.g., `dadra-&-nagar-haveli` → `Dadra & Nagar Haveli`)
- Cast data types (`year` → int, `amount` → float64)
- Derive `period` column: `YYYY-QN` format for time-series plotting
- Handle missing districts / null insurance records
- Remove duplicates and validate row counts

### Step 3 — Loading

```python
from sqlalchemy import create_engine

engine = create_engine("postgresql://user:password@localhost:5432/phonepe_db")
df_agg_txn.to_sql("agg_transactions", engine, if_exists="replace", index=False)
df_agg_user.to_sql("agg_users",        engine, if_exists="replace", index=False)
df_agg_ins.to_sql("agg_insurance",     engine, if_exists="replace", index=False)
df_map_txn.to_sql("map_transactions",  engine, if_exists="replace", index=False)
df_map_user.to_sql("map_users",        engine, if_exists="replace", index=False)
df_top_txn.to_sql("top_transactions",  engine, if_exists="replace", index=False)
```

---

## 🗄️ Database Schema

```
phonepe_db
├── agg_transactions
├── agg_users
├── agg_insurance
├── map_transactions
├── map_users
├── map_insurance
├── top_transactions
├── top_users
└── top_insurance
```

### `agg_transactions`

| Column | Type | Description |
|---|---|---|
| `state` | VARCHAR | State name |
| `year` | INTEGER | Year (2018–2024) |
| `quarter` | INTEGER | Quarter (1–4) |
| `transaction_type` | VARCHAR | Payment category |
| `transaction_count` | BIGINT | Number of transactions |
| `transaction_amount` | FLOAT | Total amount (₹) |

### `agg_users`

| Column | Type | Description |
|---|---|---|
| `state` | VARCHAR | State name |
| `year` | INTEGER | Year |
| `quarter` | INTEGER | Quarter |
| `brand` | VARCHAR | Device brand |
| `user_count` | BIGINT | Count of users by brand |
| `registered_users` | BIGINT | Total registered users |
| `app_opens` | BIGINT | App opens count |

### `agg_insurance`

| Column | Type | Description |
|---|---|---|
| `state` | VARCHAR | State name |
| `year` | INTEGER | Year |
| `quarter` | INTEGER | Quarter |
| `policy_count` | BIGINT | Number of policies |
| `premium_amount` | FLOAT | Total premium (₹) |

---

## 📊 Exploratory Data Analysis

### 1. 🗺️ State-Level Transaction Analysis
- Top 10 states by total transaction amount and count
- Average transaction value per state
- Registered users by state

### 2. 💳 Transaction Type Analysis
- Pie + bar chart dual view of payment categories
- P2P vs P2M vs Recharge vs Financial Services breakdown

### 3. 📅 Time-Series & Trend Analysis
- Quarterly and yearly transaction trends (2018–2024)
- Dual-axis chart: count + amount on same timeline
- Seasonality detection across quarters

### 4. 📱 Device Brand Analysis
- Top brands by registered user count
- Brand market share pie chart

### 5. 🛡️ Insurance Analysis
- Quarter-wise policy growth curve
- Premium trend and average premium per policy by year

### 6. 🏙️ District-Level Analysis
- Top 10 districts nationally and grouped
- Odisha district deep dive
- State × Year heatmap

### 7. 🔬 Statistical Analysis
- Scatter: transaction count vs amount (correlation)
- Outlier state identification

---

## 💡 Key Insights & Findings

### 💰 Transaction Volume
- **Maharashtra, Karnataka, and Telangana** consistently rank Top 3 by amount
- **Delhi, Rajasthan, and Uttar Pradesh** lead in count — high-frequency, low-value transactions

### 📈 Growth Trajectory
- Transactions grew **>40x** from 2018 to 2024
- **Q4 records highest volume** across all years — strong year-end seasonality
- Steepest growth post-2020 (COVID-19 accelerated UPI adoption)

### 💳 Payment Types
- **P2P** payments dominate count; **P2M** drives higher average value
- Recharge & Bill Payments show steady linear growth

### 📱 Device Ecosystem
- **Xiaomi (Redmi)** forms the largest user segment — strong tier-2/3 city penetration
- **Apple/iOS** represents a very small fraction — PhonePe is Android-first

### 🛡️ Insurance
- Policy counts grew **exponentially** from 2020 onward
- Average premium declining YoY — driven by micro-insurance for lower-income segments
- **Tamil Nadu and Karnataka** are top insurance states

### 🗺️ Odisha Deep Dive
- **Khordha district** (Bhubaneswar) leads Odisha in both count and amount
- **Sundargarh** and **Cuttack** are second-tier digital payment hubs

---

## 🖼️ Charts Gallery

| # | Chart | Description |
|---|---|---|
| 01 | `01_top10_states_amount.png` | Top 10 states by total transaction amount |
| 02 | `02_top10_states_count.png` | Top 10 states by transaction count |
| 03 | `03_txn_type_pie.png` | Transaction type distribution — pie |
| 04 | `04_txn_type_bar.png` | Transaction type distribution — bar |
| 05 | `05_quarterly_amount_trend.png` | Quarterly amount trend (2018–2024) |
| 06 | `06_quarterly_count_trend.png` | Quarterly count trend |
| 07 | `07_brand_user_count.png` | Device brand user count |
| 08 | `08_brand_pie.png` | Brand market share |
| 09 | `09_insurance_policy_growth.png` | Insurance policy growth |
| 10 | `10_insurance_premium_trend.png` | Insurance premium trend |
| 11 | `11_top10_districts.png` | Top 10 districts by amount |
| 12 | `12_state_registered_users.png` | Registered users by state |
| 13 | `13_yearly_amount.png` | Year-over-year total amount |
| 14 | `14_yearly_insurance.png` | Year-over-year insurance policies |
| 15 | `15_avg_txn_value_state.png` | Avg transaction value per state |
| 16 | `16_state_year_heatmap.png` | State × Year heatmap |
| 17 | `17_quarterly_seasonality.png` | Quarterly seasonality patterns |
| 18 | `18_avg_premium_per_policy.png` | Avg premium per policy by year |
| 19 | `19_scatter_count_vs_amount.png` | Scatter: count vs amount |
| 20 | `20_dual_axis_count_amount.png` | Dual-axis count + amount |
| 21 | `21_top10_dist_grouped.png` | Top 10 districts grouped |
| 22 | `22_odisha_districts.png` | Odisha district deep dive |

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/PhonePe_Transaction_Insights.git
cd PhonePe_Transaction_Insights
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
source venv/Scripts/activate   # Windows Git Bash
# source venv/bin/activate     # Linux / macOS
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download Raw Data

```bash
git clone https://github.com/PhonePe/pulse.git data/
```

### 5. Configure Database

```bash
psql -U postgres -c "CREATE DATABASE phonepe_db;"
# Update DB_URL in database/db_config.py
```

### 6. Run ETL Pipeline

```bash
psql -U postgres -d phonepe_db -f database/schema.sql
python etl/extract_aggregated.py
python etl/extract_map.py
python etl/extract_top.py
python etl/load_to_db.py
```

### 7. Run EDA Notebooks

```bash
jupyter notebook notebooks/
```

### 8. Regenerate Charts

```bash
python analysis/generate_charts.py
```

---

## 🗃️ Database Restore

```bash
psql -U postgres -c "CREATE DATABASE phonepe_db;"
psql -U postgres -d phonepe_db -f phonepe_pulse_backup.sql
psql -U postgres -d phonepe_db -c "\dt"
```

---

## 🔮 Future Enhancements

- [ ] Interactive Streamlit + Plotly geo-visualization dashboard
- [ ] Choropleth maps using GeoJSON at state & district level
- [ ] ARIMA / Prophet forecasting for 2025–2026 transaction volumes
- [ ] Pin code level hyperlocal transaction insights
- [ ] ML classification to predict high-growth districts
- [ ] FastAPI endpoints for aggregated statistics
- [ ] Docker Compose for one-command environment spin-up
- [ ] Metabase / Apache Superset BI integration

---

## 📚 Data Source

| Attribute | Details |
|---|---|
| **Source** | [PhonePe Pulse GitHub](https://github.com/PhonePe/pulse) |
| **Publisher** | PhonePe Private Limited |
| **License** | CDLA-Permissive-2.0 |
| **Coverage** | 2018 Q1 — 2024 Q4 |
| **Transactions** | 2,000+ crore anonymized UPI transactions |

> ⚠️ All data is anonymized and aggregated. No individual user data is present.

---

## 👨‍💻 Author

**Prasanth Kumar Sahu**
📍India

[![GitHub](https://img.shields.io/badge/GitHub-YOUR_USERNAME-black?logo=github)](https://github.com/PrasanthKumarS777)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://linkedin.com/in/prasanthsahu7)

---

## 📄 License

MIT License. PhonePe Pulse data licensed under CDLA-Permissive-2.0.

---

<div align="center">
  <sub>Built with ❤️ using Python, PostgreSQL, and open data from PhonePe Pulse</sub>
</div>
