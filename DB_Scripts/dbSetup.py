import os
import mysql.connector

def run_sql_script(cursor, filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        sql = file.read()
    print(f"Running SQL script: {filepath}")
    for result in cursor.execute(sql, multi=True):
        pass

def run_all_scripts_from_folder(cursor, folder_path):
    if not os.path.exists(folder_path):
        print(f"Folder not found, skipping: {folder_path}")
        return
    for root, _, files in os.walk(folder_path):  # Recursively walk through subfolders
        for file in sorted(files):
            if file.endswith(".sql"):
                run_sql_script(cursor, os.path.join(root, file))

def initialize_database(config):
    mysql_config = config['mySql']

    # Connect without specifying database first
    mydb = mysql.connector.connect(
        host=mysql_config['host'],
        user=mysql_config['user'],
        password=mysql_config['password']
    )
    cursor = mydb.cursor()

    # Create database if it does not exist
    db_name = mysql_config['database']
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
    mydb.commit()
    cursor.close()
    mydb.close()

    # Connect to MySQL with database specified in config
    mydb = mysql.connector.connect(
        host=mysql_config['host'],
        user=mysql_config['user'],
        password=mysql_config['password'],
        database=mysql_config['database']
    )
    cursor = mydb.cursor()

    scripts_base_path = os.path.abspath("DB_Scripts")

    # Run all scripts under Repo/Schema and Repo/Data recursively
    folders_to_run = [
        os.path.join(scripts_base_path, "Repo", "Schema"),
        os.path.join(scripts_base_path, "Repo", "Data"),
    ]

    for folder in folders_to_run:
        run_all_scripts_from_folder(cursor, folder)

    mydb.commit()  # Commit after running all scripts
    return mydb, cursor
