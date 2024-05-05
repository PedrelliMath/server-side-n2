import os

main_folder = os.path.dirname(os.path.abspath(__file__))
init_sql = os.path.join(main_folder, '..', 'schema.sql')
database_file_path = os.path.join(main_folder, 'database.db')
