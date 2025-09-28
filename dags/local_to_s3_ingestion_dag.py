from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from modules.ingestion import upload_file_to_s3

with DAG(
    "local_to_s3_ingestion",
    start_date=datetime(2025, 9, 28),
    schedule_interval=None,
    catchup=False,
) as dag:
    
    upload_task = PythonOperator(
        task_id="upload_file",
        python_callable=upload_file_to_s3,
        op_kwargs={
            "file_path": "data/orders_data.parquet",
            "bucket_name": "e-commerce-bucket-2025",
            "s3_key": "folder/in/bucket/file.csv",
        },
    )

    upload_task
