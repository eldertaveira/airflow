from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime
from airflow.utils.task_group import TaskGroup


dag = DAG('dag_task_group', description="juntando tasks",
          schedule_interval=None, start_date=datetime(2024,4,9),
          catchup=False)

tsk_group = TaskGroup("DI", dag=dag)

task1 = BashOperator(task_id='task1', bash_command = "sleep 5", dag=dag, task_group = tsk_group)
task2 = BashOperator(task_id='task2', bash_command = "sleep 5", dag=dag, task_group = tsk_group)
task3 = BashOperator(task_id='task3', bash_command = "sleep 5", dag=dag, task_group = tsk_group)
task4 = BashOperator(task_id='task4', bash_command = "sleep 5", dag=dag, task_group = tsk_group)

tsk_group = TaskGroup("BR", dag=dag)

task5 = BashOperator(task_id='task5', bash_command = "sleep 5", dag=dag, task_group = tsk_group)
task6 = BashOperator(task_id='task6', bash_command = "sleep 5", dag=dag, task_group = tsk_group)

tsk_group = TaskGroup("DW", dag=dag)

task7 = BashOperator(task_id='task7', bash_command = "sleep 5", dag=dag, task_group = tsk_group)
task8 = BashOperator(task_id='task8', bash_command = "sleep 5", dag=dag, task_group = tsk_group)
task9 = BashOperator(task_id='task9', bash_command = "sleep 5", dag=dag, task_group = tsk_group)


task1 >> task2 
task3 >> task4
[task2,task4] >> task5 >> task6
task6 >> tsk_group
