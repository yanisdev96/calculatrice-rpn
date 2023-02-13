"""Application factory."""
from .config import Config
from flask import Flask
from flask_restx import Api
from .api.operand import api as op_api
from .api.stack import api as stack_api


def create_app():
    """Instantiation de l'application Rest avec flask"""
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['ERROR_404_HELP'] = False

    # Definition de point d'etre principal de l'API
    app_restx = Api(
        app,
        version='1.0',
        title='RPN Api',
        description='calculatrice RPN (notation polonaise inversée)',
        doc="/",
        prefix="/",
    )
    # importation des APIs
    app_restx.add_namespace(op_api)
    app_restx.add_namespace(stack_api)
    return app
