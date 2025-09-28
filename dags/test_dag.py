from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def hello_world():
    """Print a hello message."""
    print("Hello from test DAG!")


with DAG(
    "test_dag",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@once",
    catchup=False,
) as dag:
    task = PythonOperator(
        task_id="hello_world_task",
        python_callable=hello_world,
    )
# test workflow login
# test workflow login
