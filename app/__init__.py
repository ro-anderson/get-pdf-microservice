from flask import Flask
from flask_restx import Api
import config.config as config
import os


application = Flask(__name__)
application.config.from_object('config')

# Configurations
config.Env_setup()

api = Api(
    title='Invoice Digitizer'
)

# Init app
api.init_app(application)

from app.invoice_digitizer.routes import api as invoice_digitizer
api.add_namespace(invoice_digitizer, path='/invoice-digitizer')

if __name__ == "__main__":
    application.run(host=os.getenv(key='FLASK_IP'), port=os.getenv(key='FLASK_PORT'))
