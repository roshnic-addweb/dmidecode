from flask import Flask, json, render_template
import requests
app = Flask(__name__)


@app.route("/")
def hello():

    help_json = requests.get('http://127.0.0.1:5000/help')
    help_dict = json.load(help_json)
    return help_dict


if '__name__' == '__main__':
    app.route(debug=True, host="0.0.0.0", port=9109)

