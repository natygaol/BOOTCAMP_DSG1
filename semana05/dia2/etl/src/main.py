from prefect import flow
from tasks.task_extract import(
    task_extract_dni,
    task_extract_csv
)

PATH_CSV = './resources/alumnos.csv'

@flow(name='ETL APIPERU')
def main_flow():
    lista_alumnos = task_extract_csv(PATH_CSV)
    for tupla_alumno in lista_alumnos:
        data_dnis = task_extract_dni(tupla_alumno)
        print(data_dnis)


if __name__ == '__main__':
    main_flow()