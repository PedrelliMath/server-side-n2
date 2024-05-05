import sqlite3
from exceptions.exceptions import VectorNotFound, SqliteError
from utils.utils import convert_vector_to_text
from models.vector import Vetor

def init_database(database_file_path, init_sql):
    try:
        with sqlite3.connect(database_file_path) as conn:
            cursor = conn.cursor()
            with open(init_sql, 'r') as arquivo_sql:
                sql = arquivo_sql.read()
            cursor.executescript(sql)
            conn.commit()
    except sqlite3.Error as e:
        print(f'Error while executing init sql: {e}')
        raise SqliteError
    except FileNotFoundError as e:
        print(f'Error while executing init sql: {e}')
        raise SqliteError

def database_insert_vector(vector: Vetor, database_file_path):
    insert_random_vector_sql = """
        INSERT INTO VetorRandomizado (vetor_values) VALUES (?);
    """
    insert_vector_description_sql = """
        INSERT INTO VetorRandomizadoDescricao (id_vetor_randomizado, nome_vetor, descricao)
        VALUES (?, ?, ?)
    """
    try:
        with sqlite3.connect(database_file_path) as conn:
            cursor = conn.cursor()
            cursor.execute(insert_random_vector_sql, (convert_vector_to_text(vector),))
            vetor_id = cursor.lastrowid
            cursor.execute(insert_vector_description_sql, (vetor_id, vector.name, vector.description))
            conn.commit()
            print(f'Success while inserting vector')
    except sqlite3.Error as e:
        print(f'SQLite Error while inserting vector: {e}')
        raise SqliteError
    except Exception as e:
        print(f'Unexpected error while inserting vector: {e}')
        raise SqliteError

def database_get_vector(database_file_path):
    get_random_vector_sql = """
        SELECT VetorRandomizado.id, VetorRandomizado.vetor_values, 
               VetorRandomizadoDescricao.nome_vetor, VetorRandomizadoDescricao.descricao
        FROM VetorRandomizado
        JOIN VetorRandomizadoDescricao ON VetorRandomizado.id = VetorRandomizadoDescricao.id_vetor_randomizado
        ORDER BY VetorRandomizado.id DESC
        LIMIT 3;
    """
    try:
        with sqlite3.connect(database_file_path) as conn:
            cursor = conn.cursor()
            cursor.execute(get_random_vector_sql)
            vector = cursor.fetchall()
            if vector:
                print('Success while find vector')
                return vector
            else:
                raise VectorNotFound
            
    except sqlite3.Error as e:
        print(f'SQLite Error while finding vector: {e}')
        raise SqliteError
    except VectorNotFound:
        print(f'No vector found')
        raise VectorNotFound
    except Exception as e:
        print(f'Unexpected error while finding vector: {e}')
        raise SqliteError