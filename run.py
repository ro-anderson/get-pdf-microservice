from app import application
import os

if __name__ == "__main__":
    application.run(host=os.getenv(key='FLASK_IP'), port=os.getenv(key='FLASK_PORT'))
