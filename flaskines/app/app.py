from flask import Flask
from app.utils.db import db
from app.routes.routes import users
app = Flask(__name__)



app.register_blueprint(users)

