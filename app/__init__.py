# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.template_folder = "../templates"  # 添加这一行
db = SQLAlchemy(app)

from app import routes
