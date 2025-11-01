# NYC Property Sales Dataset

A **data engineering project** analyzing New York City property sales over a 12-month period.  
Includes a complete **ETL pipeline**, **data parsing**, and **EDA** in Python.

---

## Overview

**Goals:**
- Extract, clean, and transform NYC property sales data  
- Load processed data into PostgreSQL and Parquet  
- Visualize and analyze sales trends  

**Dataset:**
- Source: NYC Department of Finance  
- [Google Drive Link](https://drive.google.com/drive/folders/1NhSdry2LAagL66Vec8ckH4ypVeg3Iwp6?usp=sharing)  
- Includes location, sale, and property classification details  
- Covers both full-building and unit sales  

---

## Structure

```
NYC-Property-Sales/
├── api_example/                 # API integration examples
│   ├── api_reader.py
│   └── README.md
├── etl/                         # ETL pipeline
│   ├── __init__.py
│   ├── extract.py               # Extract data from sources
│   ├── transform.py             # Data cleaning and transformation
│   ├── load.py                  # Load data to DB and Parquet
│   └── main.py                  # ETL entry point
├── parse_example/               # Data parsing examples
│   ├── data_parser.py
│   └── README.md
├── notebook/                    # Jupyter notebooks for analysis
│   ├── EDA.ipynb
│   └── README.md
├── src/                         # Project modules
│   ├── data_loader.py
│   └── README.md
├── pyproject.toml               # Project configuration (Poetry)
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

---

## Installation

```bash
conda create -n nyc_sales python=3.13 pip
conda activate nyc_sales
pip install pandas numpy matplotlib seaborn plotly jupyterlab gdown sqlalchemy psycopg2-binary pyarrow
```

---

## ETL Pipeline
# Run full pipeline
python -m etl.main run --file-id 1NhSdry2LAagL66Vec8ckH4ypVeg3Iwp6

# Extract / Transform / Load separately
python -m etl.main extract --file-id ...
python -m etl.main transform --input data/raw/nyc_sales.csv
python -m etl.main load --input data/processed/nyc_sales_clean.csv --table nyc_property_sales

Stages:

Extract: Download dataset → /data/raw/

Transform: Clean and normalize data

Load: Save to Parquet + load ≤100 rows into PostgreSQL

## EDA

Run interactive notebook:
jupyter notebook notebook/EDA.ipynb

**Includes:**
- Sales trends by borough
- Price distributions
- Correlation and anomaly detection

---

## Applications
- Real estate market & valuation analysis
- Price prediction models
- Spatial and time-series analysis

---

## Main Libraries
`pandas`, `numpy`, `matplotlib`, `seaborn`, `plotly`,  
`sqlalchemy`, `psycopg2-binary`, `pyarrow`, `jupyterlab`, `gdown`

