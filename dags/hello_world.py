from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta  # Import timedelta

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),  # Use timedelta here
}

# Define the DAG object
dag = DAG(
    'hello_world',
    default_args=default_args,
    description='A simple DAG that prints Hello, World!',
    schedule_interval='@daily',
)

# Define the tasks
task_hello_world = BashOperator(
    task_id='print_hello_world',
    bash_command='echo "Hello, World!"',
    dag=dag,
)

# Define task dependencies
task_hello_world
