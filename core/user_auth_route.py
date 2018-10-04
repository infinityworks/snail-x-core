from core import app
from flask import render_template, request


@app.route('/login')
def login():
    return "logged in"
