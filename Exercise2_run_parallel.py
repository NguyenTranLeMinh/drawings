from airflow.models import DAG
from airflow.operators.bash import BashOperator

from datetime import datetime

default_args = {
    "start_date": datetime(2022, 1, 1)
}

with DAG('parallel_dag',
        default_args=default_args, 
        schedule_interval="@daily",
        catchup=False) as dag:
    task_1 = BashOperator(
        task_id='task_1',
        bash_command='sleep 3'
    )

    task_2 = BashOperator(
        task_id='task_2',
        bash_command='sleep 3'
    )

    task_3 = BashOperator(
        task_id='task_3',
        bash_command='sleep 3'
    )

    task_4 = BashOperator(
        task_id='task_4',
        bash_command='sleep 3'
    )

    task_1 >> [task_2, task_3] >> task_4