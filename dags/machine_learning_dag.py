import os
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import pandas as pd
from prediction_model import machine_learning


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime.now(),
    'retries': 0,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'machine_learning_dag', 
    default_args=default_args, 
    description='Machine Learning',
    schedule_interval=timedelta(days=1)
    )

# Define the wait time
wait_time = timedelta(seconds=15)

machine_learning = PythonOperator(
    task_id='machine_learning',
    python_callable=machine_learning,
    op_kwargs={'seconds': wait_time.seconds},
    dag=dag
)

machine_learning
