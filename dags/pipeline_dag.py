from datetime import datetime
from airflow import DAG
from airflow.operators.dagrun_operator import TriggerDagRunOperator

dag = DAG(
    dag_id='trigger_dags_in_order',
    description='Trigger three DAGs in order',
    start_date=datetime.now(),
    schedule_interval=None
)

data_processing_op = TriggerDagRunOperator(
    task_id='trigger_data_processing_dag',
    trigger_dag_id='data_processing_dag',
    dag=dag
)

feature_engineering_op = TriggerDagRunOperator(
    task_id='trigger_feature_engineering_dag',
    trigger_dag_id='feature_engineering_dag',
    dag=dag
)

machine_learning_op = TriggerDagRunOperator(
    task_id='trigger_machine_learning_dag',
    trigger_dag_id='machine_learning_dag',
    dag=dag
)

# Set the order of the tasks
data_processing_op >> feature_engineering_op >> machine_learning_op
