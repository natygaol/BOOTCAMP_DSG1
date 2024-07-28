import mysql.connector
from config import Config
from prefect import task

config = Config()

conn = mysql.connector.connect(
            user=config.mysql_user,
            password=config.mysql_password,
            host=config.mysql_host,
            database=config.mysql_database
        )


@task(name='carga de info en bd')
def task_load_rucs(rucs):
    try:
        cursor = conn.cursor()

        query_drop = "drop table if exists tbl_ruc"
        cursor.execute(query_drop)
        conn.commit()

        query_table = """
        create table if not exists tbl_ruc(
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre_o_razon_social VARCHAR(80),
        direccion VARCHAR(255),
        estado VARCHAR(20),
        condicion VARCHAR(20),
        departamento VARCHAR(30),
        celular VARCHAR(20),
        fecha_creacion DATETIME default CURRENT_TIMESTAMP)
        """

        cursor.execute(query_table)
        conn.commit()

        query_insert = """
        insert into tbl_ruc(nombre_o_razon_social,direccion,estado,condicion,departamento,celular)
        values(%s,%s,%s,%s,%s,%s)
        """

        for ruc in rucs:
            cursor.execute(query_insert,ruc)

        conn.commit()
        cursor.close()
        conn.close()
        print('datos guardados en bd...')

    except mysql.connector.Error as err:
        print(err)