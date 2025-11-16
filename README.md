# Ecommerce ETL Pipeline

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![AWS S3](https://img.shields.io/badge/AWS-S3-orange?logo=amazon-aws)](https://aws.amazon.com/s3/)
[![SageMaker](https://img.shields.io/badge/AWS-SageMaker-darkgreen?logo=amazon-aws)](https://aws.amazon.com/sagemaker/)
[![Glue](https://img.shields.io/badge/AWS-Glue-purple?logo=amazon-aws)](https://aws.amazon.com/glue/)
[![Data Engineering](https://img.shields.io/badge/Data%20Engineering-pipeline-blueviolet)](#)
[![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Supported-brightgreen)](#)
[![Project Type](https://img.shields.io/badge/Type-Academic%20Research-lightgrey)](#)
[![Last Updated](https://img.shields.io/badge/Updated-Nov%202025-purple)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

End-to-end ETL and analytics pipeline for splitting, transforming, and managing large datasets (Amazon, Google Merchandise, Bluesky, etc.) across AWS S3, Lambda, Glue, and SageMaker for advanced analysis and machine learning.

---

## 🧭 Purpose
Efficiently ingest, clean, transform, and deliver advanced e-commerce data for automated analytics and production ML at scale.

- Split, deduplicate, and transform giga-scale CSVs and raw feeds
- Normalize/denormalize for S3 “Landing”, “Clean”, “Curated” zones
- Enable downstream BI (Athena/Tableau) and ML (SageMaker) with clean, queryable data

---

## 📁 Repository Structure
```
ecommerce-etl-pipeline/
    ├── split_csv.py                  # Utility to split very large CSVs
    ├── requirements.txt              # Python requirements
    ├── LICENSE├── remove-files.txt   # Used for repo cleaning (Git history)
    ├── test_partX.csv, etc.          # Working data files (never tracked)
    ├── notebooks/                    # Analysis notebooks for EDA and ML
    ├── aws_glue_jobs/                # Glue/ETL scripts)
    ├── README.md
```
**Note:** All large/PII data files are excluded from git.  
See `.gitignore` for data/file hygiene rules.

---

## 🚀 Workflow

1. **Ingest Data**
   - Fetch data from public datasets, APIs (Amazon reviews, Google store, Bluesky), or partner uploads
2. **Split & Clean**
   - Use `split_csv.py` to partition massive CSVs for easy handling/S3 uploads
   - Remove duplicates, cleanse nulls/inconsistencies
3. **Stage to S3**
   - AWS CLI or SDK to upload to S3 Landing, Clean, then Curated zones
4. **Transform (Glue/Lambda)**
   - Use AWS Glue/Lambda/Glue Studio for denormalization, feature engineering, and joins
5. **Query & Visualize**
   - Query curated data in Athena, visualize insights in Tableau, BI
6. **Model (SageMaker)**
   - Leverage curated parquet data for AWS SageMaker ML workflows

---

## 🆕 Current Focus (Nov 2025)
- Solidify & document S3 bucket zone flows, Glue transforms
- Add sample Lambda functions for raw-to-parquet, event processing
- Deploy ML pipeline on SageMaker using productionized data splits
- Maintain robust `.gitignore` and repo hygiene for smooth cloud ops

---

## 🧰 Tech Stack
Python 3.10+, pandas, AWS CLI, AWS SDK (boto3), AWS S3, Glue, Lambda, Athena, SageMaker, PySpark, VS Code

---

## 📝 Project Status
✅ Automated large CSV splitting  
✅ AWS zoning and data flow tested  
🟦 Glue/Lambda transformation scripting  
🟦 EDA/ML samples for SageMaker integration (in progress)  
📈 Athena/Tableau insight examples (in progress)  
❌ No data files tracked in repo

---

## 👤 Contributors
Warren Jones, Fisayo Adeolu, Sekoria Johnson  
Earl G. Graves School of Business & Management, Morgan State University

---

## 📚 References
- [Google Merchandise Store](https://support.google.com/analytics/answer/7586738)
- [Amazon Review Polarity Dataset](https://paperswithcode.com/dataset/amazon-polarity)
- [Bluesky Firehose API](https://docs.bsky.app/docs/feed/getting-started)
- AWS S3, Lambda, Glue, SageMaker docs

---

All results are preliminary and intended for research/educational use.  
_Last updated: Nov 2025_
