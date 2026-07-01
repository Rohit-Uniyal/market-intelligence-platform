# 📈 Market Intelligence Platform

An end-to-end data engineering project that collects real-time financial market discussions from X (formerly Twitter), processes the data through an ETL pipeline, performs keyword analysis using TF-IDF, and generates visual insights.

The project demonstrates practical data engineering concepts including web scraping, data cleaning, data transformation, Parquet storage, text analytics, and visualization.

---

## Project Overview

Financial markets generate a large volume of discussions every day across social media platforms. This project automates the process of collecting market-related tweets using Selenium, transforms the raw data into an analytics-ready format, and extracts trending keywords for further analysis.

The pipeline is designed using a modular architecture where each stage of the ETL process is separated into individual components.

---

## Features

- Collects live tweets from X (Twitter) using Selenium
- Searches multiple stock market related hashtags
- Removes duplicate tweets
- Cleans and prepares raw text data
- Stores processed data in both CSV and Parquet formats
- Performs keyword extraction using TF-IDF
- Generates visual reports
- Modular and reusable project structure

---

## Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Web Scraping | Selenium |
| Data Processing | Pandas |
| Text Analytics | Scikit-learn (TF-IDF) |
| Storage | CSV, Parquet |
| Visualization | Matplotlib |
| Version Control | Git |
| Repository | GitHub |

---

# Project Structure

```
market-intelligence-platform/
│
├── output/
│   ├── twitter_market_data.csv
│   ├── twitter_market_data_cleaned.csv
│   ├── twitter_market_data.parquet
│   ├── trending_keywords.csv
│   ├── top_keywords.png
│   └── hashtag_distribution.png
│
├── src/
│   ├── scraper/
│   │   ├── browser.py
│   │   ├── constants.py
│   │   ├── parser.py
│   │   └── twitter_scraper.py
│   │
│   ├── processing/
│   │   └── clean_data.py
│   │
│   ├── storage/
│   │   ├── save_data.py
│   │   └── save_parquet.py
│   │
│   └── analysis/
│       ├── keyword_analysis.py
│       └── visualization.py
│
├── tests/
│
├── main.py
├── requirements.txt
└── README.md
```

---

# ETL Pipeline

```
Twitter (X)

        │

        ▼

 Selenium Web Scraper

        │

        ▼

 Raw CSV Storage

        │

        ▼

 Data Cleaning

        │

        ▼

 Parquet Conversion

        │

        ▼

 TF-IDF Keyword Analysis

        │

        ▼

 Data Visualization
```

---

## Workflow

### Step 1 – Data Collection

The scraper connects to X (Twitter) using Selenium and collects market-related tweets based on predefined financial hashtags.

Examples include:

- #nifty50
- #sensex
- #banknifty
- #stockmarket
- #intraday
- #trading

---

### Step 2 – Data Cleaning

The collected tweets are cleaned by removing:

- duplicate records
- missing values
- unnecessary whitespace

The cleaned dataset is stored for further processing.

---

### Step 3 – Data Storage

The project stores processed data in:

- CSV
- Parquet

Parquet is used as an optimized columnar storage format commonly used in modern data engineering pipelines.

---

### Step 4 – Keyword Analysis

The project applies the TF-IDF algorithm to identify important keywords from market discussions.

The output is stored in:

```
output/trending_keywords.csv
```

---

### Step 5 – Visualization

Two visual reports are automatically generated.

- Top Trending Keywords
- Tweet Distribution by Hashtag

These charts help identify the most discussed financial topics.

---

# Sample Outputs

Generated files include:

- twitter_market_data.csv
- twitter_market_data_cleaned.csv
- twitter_market_data.parquet
- trending_keywords.csv
- top_keywords.png
- hashtag_distribution.png

---

# Installation

Clone the repository

```bash
git clone https://github.com/Rohit-Uniyal/market-intelligence-platform.git
```

Navigate to the project directory

```bash
cd market-intelligence-platform
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
python main.py
```

---

# Skills Demonstrated

- Python Programming
- Selenium Automation
- Data Engineering
- ETL Pipeline Development
- Data Cleaning
- Parquet Storage
- Text Analytics
- TF-IDF
- Data Visualization
- Git Version Control

---

# Future Enhancements

- Apache Kafka for streaming ingestion
- Apache Airflow for workflow orchestration
- PostgreSQL data warehouse
- Sentiment Analysis
- Power BI dashboard
- Docker containerization
- Cloud deployment

---

# Author

**Rohit Uniyal**

GitHub:
https://github.com/Rohit-Uniyal

LinkedIn:
linkedin.com/in/rohituniyal

---

## License

This project is developed for educational and portfolio purposes.
