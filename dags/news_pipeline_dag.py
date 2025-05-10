from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import sys
import os

# Debugging - print current directory and Python path
print(f"Current directory: {os.getcwd()}")
print(f"Python path before: {sys.path}")

# Add parent directory to Python path for container environment
sys.path.insert(0, '/opt/airflow')
print(f"Python path after: {sys.path}")

# Try importing with explicit debugging
try:
    from scripts.collect_data import collect_news_data
    from scripts.preprocess_data import preprocess_data
    from scripts.train_model import train_model
    from scripts.test_model import test_model
    print("Successfully imported all modules")
except ImportError as e:
    print(f"Import error: {e}")
    # List directories for debugging
    print(f"Files in /opt/airflow: {os.listdir('/opt/airflow')}")
    if os.path.exists('/opt/airflow/scripts'):
        print(f"Files in scripts dir: {os.listdir('/opt/airflow/scripts')}")
    raise

# Define default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Create the DAG
dag = DAG(
    'news_data_pipeline',
    default_args=default_args,
    description='A pipeline for collecting, processing, and modeling news data',
    schedule=timedelta(days=1),
    start_date=datetime(2025, 5, 1),
    catchup=False,
    tags=['news', 'data', 'pipeline'],
)

# Task 1: Collect news data
collect_data_task = PythonOperator(
    task_id='collect_news_data',
    python_callable=collect_news_data,
    dag=dag,
)

# Task 2: Preprocess data
preprocess_data_task = PythonOperator(
    task_id='preprocess_data',
    python_callable=preprocess_data,
    dag=dag,
)

# Task 3: Train model
train_model_task = PythonOperator(
    task_id='train_model',
    python_callable=train_model,
    dag=dag,
)

# Task 4: Test model
test_model_task = PythonOperator(
    task_id='test_model',
    python_callable=test_model,
    dag=dag,
)


# Define task dependencies 
collect_data_task >> preprocess_data_task >> train_model_task >> test_model_task