import requests
import mysql.connector
#imagen, nombre y habilidad
def get_pokemons():
    pokemons = []
    for id in range(1, 151):  # Rango desde 1 hasta 150 inclusive
        url = f'https://pokeapi.co/api/v2/pokemon/{id}'
        response = requests.get(url)
        if response.status_code == 200:
            pokemons.append(response.json())
        else:
            print(f'Error al obtener el Pokémon con ID {id}:', response.status_code)
    return pokemons
    
def insert_pokemons_to_mysql(pokemons):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='db_codigo'
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS tbl_pokemon(
                       id INT AUTO_INCREMENT PRIMARY KEY,
                       nombre VARCHAR(255),
                       habilidad VARCHAR(255)
                       )
                       """)
        
        for pokemon in pokemons:
            nombre = pokemon['name']
            habilidad = ", ".join([ability['ability']['name'] for ability in pokemon['abilities']])
            cursor.execute("""
                           INSERT INTO tbl_pokemon(nombre, habilidad)
                           VALUES(%s, %s)
                           """, (nombre, habilidad))
             
            connection.commit()
        print('Pokemons insertados exitosamente')
        
        cursor.close()
        connection.close()

pokemons = get_pokemons()
insert_pokemons_to_mysql(pokemons)