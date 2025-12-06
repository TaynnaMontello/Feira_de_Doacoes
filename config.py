import os

class Config:
    SECRET_KEY = "chave-super-secreta"
    SQLALCHEMY_DATABASE_URI = "sqlite:///meubanco.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
