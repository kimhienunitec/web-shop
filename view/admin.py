from flask import render_template, request, redirect, jsonify, session, url_for, abort
from view import myapp
from model import account
import hashlib
import os


@myapp.route('/admin/', methods=['GET'])
def index():
    return render_template('/admin/index.html')