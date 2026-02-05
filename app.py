import json
import os
import sqlite3

# from openai import OpenAI


def get_path(fname):
    fdir = os.path.dirname(__file__)
    return os.path.join(fdir, fname)

def get_api_key(path):
    configPath = get_path(path)

    with open(configPath) as configFile:
        config = json.load(configFile)

    return config["openaiKey"]  



# set up sqlite database
sqliteDbPath = get_path("aidb.sqlite")
setupSqlPath = get_path("setup.sql")
setupSqlDataPath = get_path("setupData.sql")

if os.path.exists(sqliteDbPath):
    os.remove(sqliteDbPath)
    
con = sqlite3.connect(sqliteDbPath)
cursor = con.cursor()

with (
    open(setupSqlPath) as setupSqlFile,
    open(setupSqlDataPath) as setupSqlDataFile
):

    setup_sql_script = setupSqlFile.read()
    setup_data_script = setupSqlDataFile.read()

# execute setup files
cursor.executescript(setup_sql_script) # setup tables and keys
cursor.executescript(setup_data_script) # setup tables and keys

def runSql(query):
    result = cursor.execute(query).fetchall()
    return result

api_key = get_api_key("config.json")
    