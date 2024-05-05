from utils.utils import convert_text_to_vector, create_vector, randomize_vector, heap_sort, random_index
from database.database import database_get_vector, database_insert_vector
from exceptions.exceptions import SqliteError, VectorNotFound
from config import database_file_path
from http import HTTPStatus
from flask import jsonify
from models.vector import Vetor

def results_to_json_service():

    response_list = []

    try:
        for i in range(3):
            vector, time_to_create = create_vector(
                50000,
                f'Vetor {i + 1}',
                f'Este e o Vetor {i + 1} de 50 mil posicoes'
            )
            random_vector, time_to_randomize = randomize_vector(vector, random_index(len(vector.values)))
            database_insert_vector(random_vector, database_file_path)

            response = {
            'vector_name': random_vector.name,
            'vector_description': random_vector.description,
            'times':{
                'create_time':time_to_create,
                'randomize_time':time_to_randomize,
                },
            }

            response_list.append(response)
    except Exception as e:
        return jsonify({'error':f'an unexpected error occurred: {e}'}), HTTPStatus.INTERNAL_SERVER_ERROR

    try:
        db_random_vector = database_get_vector(database_file_path)
    except SqliteError:
        return jsonify({'error':'erro ao buscar o vetor no banco'}), HTTPStatus.INTERNAL_SERVER_ERROR
    except VectorNotFound:
        return jsonify({'error':'no vectors found in database'}), HTTPStatus.NO_CONTENT
    except Exception:
        return jsonify({'error':'an unexpected error occurred'}), HTTPStatus.INTERNAL_SERVER_ERROR
    

    for i in range(3):
        random_vector = Vetor(db_random_vector[i][2], db_random_vector[i][3], db_random_vector[i][1])

        sorted_vector, sort_time = heap_sort(convert_text_to_vector(random_vector.values))
        response_list[i]['times']['sort_time'] = sort_time

    return jsonify(response_list), HTTPStatus.OK


    


        