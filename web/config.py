import os
from pathlib import Path


basedir = Path(__file__).resolve().parent.parent


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        f"sqlite:///{basedir.joinpath('ydan.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
