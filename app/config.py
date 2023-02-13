"""Configuration file."""

from os import environ


class Config(object):
    """Classe de donnees de configuration"""
    DEBUG = True if environ.get('DEBUG') == 'True' else False
    APP_PORT = int(environ.get('APP_PORT', 8888))
    OPERAND_LIST = ['+', '-', '*', 'div']