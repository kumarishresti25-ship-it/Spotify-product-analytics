#  Spotify Product Usage Analytics & Feature Adoption Tracker

> An end-to-end product data analytics portfolio project tracking listener behavior, drop-off rates across the core streaming funnel, and the retention impact of personalized discovery features (AI DJ, Discover Weekly) to optimize Free-to-Premium conversion.

---

##  Project Architecture

```text
spotify-product-analytics/
│
├── data/
│   └── datagenerate_spotify_data.py   # Python script simulating user session & event logs
│
├── analytics/
│   └── funnel_analysis.py             # Python engine calculating conversion rates & feature adoption
│
├── sql/
│   ├── 01_schema_setup.sql            # PostgreSQL table schema creation
│   ├── 02_funnel_analysis.sql         # Search-to-listening conversion & drop-off queries
│   └── 03_feature_adoption.sql        # Feature penetration & engagement impact queries
│
├── dashboard/
│   └── app.py                         # Streamlit interactive stakeholder dashboard
│
│
└── README.md

## Tech Stack & Skills Demonstrated
Python (Pandas, NumPy): Automated synthetic event log generation and data processing pipelines.

SQL (PostgreSQL): Advanced querying using Common Table Expressions (CTEs), multi-stage funnel analysis, and data aggregation.

Data Visualization & BI: Interactive web dashboard development using Streamlit.

Product Management: Defining core KPIs, isolating behavioral friction points, and evaluating the ROI of feature rollouts.
