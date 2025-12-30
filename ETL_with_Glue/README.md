# Event-Driven CSV ETL Pipeline — AWS Glue & Lambda

## Objective

Design and implement an event-driven ETL pipeline on AWS where CSV files uploaded to Amazon S3 are automatically processed using AWS Glue, orchestrated by AWS Lambda, and stored back in S3 in analytics-optimized Parquet format.

## Architecture Overview

- Source: CSV files (support ticket data)
- Raw storage: Amazon S3 — `support_ticket/raw/`
- Processing engine: AWS Glue (script-based ETL job)
- Orchestration: AWS Lambda
- Trigger: S3 Event Notification
- Processed storage: Amazon S3 — `support_ticket/processed/` (Parquet)

Flow:

CSV files
  ↓
S3 (`support_ticket/raw/`)
  ↓ (S3 event notification)
AWS Lambda
  ↓ (trigger)
AWS Glue ETL job
  ↓
S3 (`support_ticket/processed/` — Parquet)

## Implementation Details

1. CSV ingestion & ETL (AWS Glue)
   - Read CSV files from S3.
   - Apply transformations: data cleaning, schema handling, and column-level transformations.

2. Glue job script conversion
   - Convert visual Glue job into a script-based Glue ETL job for automation and reusability.

3. Lambda-based Glue job trigger
   - Lambda detects new CSV uploads and triggers the Glue job programmatically.

4. Event-driven ingestion (S3 notifications)
   - Configure S3 event notifications with prefix filtering on `support_ticket/raw/` to invoke Lambda selectively.

5. Processed data storage
   - Write transformed output in Parquet format to `support_ticket/processed/` for analytics.

## S3 Folder Structure
```
support_ticket/
├── raw/
│   └── support_ticket_data.csv
└── processed/
    └── support_ticket_data.parquet
```

## Key Learnings

- Building event-driven data pipelines on AWS
- Developing and scripting AWS Glue ETL jobs
- Orchestrating Glue with AWS Lambda
- Using S3 prefix-based event notifications
- Converting CSV to Parquet and optimizing for analytics

## Tech Stack

- Amazon S3
- AWS Glue
- AWS Lambda
- Python
- Parquet
- Amazon CloudWatch

## Future Enhancements

- Integrate AWS Glue Data Catalog
- Add schema validation and data quality checks
- Implement Parquet partitioning
- Add retry and failure handling mechanisms
- Enable querying with Amazon Athena