import os
from flask import Flask
from flask_cors import CORS
from database.database import init_database 
from config import database_file_path, init_sql
from services import results, graficos

app = Flask(__name__)
CORS(app)

@app.get('/graficos')
def get_graficos():
    return graficos.get_graphs_service()

@app.get('/execute')
def get_results():
    return results.results_to_json_service()

if __name__=='__main__':

    if not os.path.exists(database_file_path):
        init_database(database_file_path, init_sql)
    
    app.run(host='0.0.0.0', debug=True, port=5000)

