from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def hello():
    env_variable_value = os.getenv('ENV_VARIABLE_VALUE', 200)
    return f"<html><body><h1>Hello, This is New & Latest Flask Application! Environment Variable value = {env_variable_value}</h1></body></html>\n"