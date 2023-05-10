import os
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash import BashOperator
import pyarrow.csv as pv
import pyarrow.parquet as pq
import pandas as pd
from processing import data_tranformation, stock_csv_to_parquet, etfs_csv_to_parquet

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime.now(),
    'retries': 2,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'data_processing_dag', 
    default_args=default_args, 
    description='ETL process',
    schedule_interval=timedelta(days=1)
    )

download_dataset = BashOperator(
    task_id='download_dataset',
    bash_command="scripts/download.sh",
    dag=dag
)

# Define the wait time
wait_time = timedelta(seconds=15)

process_dataset = PythonOperator(
    task_id='process_dataset',
    python_callable=data_tranformation,
    op_kwargs={'seconds': wait_time.seconds},
    dag=dag
)

csv_parquet = BashOperator(
    task_id='start',
    bash_command='date'
)

stock_csv_to_parquet = PythonOperator(
    task_id='stock_csv_to_parquet',
    python_callable=stock_csv_to_parquet,
    op_kwargs={'seconds': wait_time.seconds},
    dag=dag
)

etfs_csv_to_parquet = PythonOperator(
    task_id='etfs_csv_to_parquet',
    python_callable=etfs_csv_to_parquet,
    op_kwargs={'seconds': wait_time.seconds},
    dag=dag
)

download_dataset >> process_dataset >> [stock_csv_to_parquet, etfs_csv_to_parquet]
