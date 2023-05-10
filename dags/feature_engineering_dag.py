import os
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash import BashOperator
import pyarrow.parquet as pq
import pandas as pd
from feature_engineering import stocks_cal, etfs_cal, stock_csv_to_parquet, etfs_csv_to_parquet


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime.now(),
    'retries': 0,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'feature_engineering_dag', 
    default_args=default_args, 
    description='Feature Engineering',
    schedule_interval=timedelta(days=1)
)


# Define the wait time
wait_time = timedelta(seconds=15)

stocks_cal = PythonOperator(
    task_id='stocks_cal',
    python_callable=stocks_cal,
    op_kwargs={'seconds': wait_time.seconds},
    dag=dag
)

etfs_cal = PythonOperator(
    task_id='etfs_cal',
    python_callable=etfs_cal,
    op_kwargs={'seconds': wait_time.seconds},
    dag=dag
)

aggregation_task = BashOperator(
    task_id='start',
    bash_command='date',
    start_date=default_args['start_date'],
    dag=dag
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

stocks_cal.set_upstream(aggregation_task)
etfs_cal.set_upstream(aggregation_task)
stock_csv_to_parquet.set_upstream(stocks_cal)
etfs_csv_to_parquet.set_upstream(etfs_cal)
