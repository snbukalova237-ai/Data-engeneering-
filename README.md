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

NYC-Property-Sales/
├── api_example/           # API integration examples
│   ├── api_reader.py
│   └── README.md
├── etl/                   # ETL pipeline
│   ├── init.py
│   ├── extract.py         # Extract data from sources
│   ├── transform.py       # Data cleaning and transformation
│   ├── load.py            # Load data to DB and Parquet
│   └── main.py            # ETL entry point
├── parse_example/         # Data parsing examples
│   ├── data_parser.py
│   └── README.md
├── notebook/              # Jupyter notebooks for analysis
│   ├── EDA.ipynb
│   └── README.md
├── src/                   # Project modules
│   ├── data_loader.py
│   └── README.md
├── pyproject.toml          # Project configuration (Poetry)
├── requirments.txt         # Python dependencies
└── README.md               # Project documentation


