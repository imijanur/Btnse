from flask import Flask
from nsetools import Nse
from nsepy import history_data

app = Flask(__name__)

@app.route('/')
def home():
    return "deploy"

if __name__ = "__main__" :
    app.run()
