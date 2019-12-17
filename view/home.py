from flask import render_template, request, redirect, jsonify, session, url_for
from view import myapp


@myapp.route('/', methods=['GET'])
def home():
    return render_template('/home/index.html')