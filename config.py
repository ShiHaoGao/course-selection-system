# config.py
import os


class Config:
    SECRET_KEY = "your_random_secret_key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
