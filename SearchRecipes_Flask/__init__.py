from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY']='cop4814'

from SearchRecipes_Flask import routes