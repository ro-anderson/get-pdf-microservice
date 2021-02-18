# Statement for enabling the development environment
import json
import os


def Env_setup():

    # Tentar Ler arquivo config.json
    try:
        with open('config/config.json') as json_file:
            data = json.load(json_file)
            for env_var in data:
                os.environ[env_var] = str(data[env_var])
    except:
        pass
