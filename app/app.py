#configura la aplicacion
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return("Hello word")



