from prefect import flow
from tasks.task_extract import(
    task_extract_dni
)

@flow(name='ETL APIPERU')
def main_flow():
    dnis = ['41776223','41273345']
    for dni in dnis:
        data_dnis = task_extract_dni(dni)
        print(data_dnis)


if __name__ == '__main__':
    main_flow()