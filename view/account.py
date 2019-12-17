from flask import render_template, request, redirect, jsonify, session, url_for, abort
from view import myapp
from model import account
from flask_menu import Menu, register_menu
import hashlib
import os



myapp.secret_key=os.urandom(24)


@myapp.route('/login/', methods = ['GET'])
def login():
    return render_template('/account/login.html')


@myapp.route('/login/', methods=['POST'])
def  postlogin():
    _username=request.form.get('username')
    _password=request.form.get('password')
    _password_cryption = (hashlib.md5(_password.encode())).hexdigest()
    try:
        data = account.checkLogin(_username, _password_cryption)
        if data != None:
            if data[1] == _username and data[8] == _password_cryption:
                if data[7] == 1:
                    session['username'] = _username
                    return redirect('http://127.0.0.1:5000/home')
                elif data[7] == 2:
                    return redirect('http://127.0.0.1:5000/admin')
        else:
            _result = "Đăng nhập sai, xin vui lòng thử lại"
            return render_template('/account/login.html', result=_result)
    except(ValueError, KeyError, TypeError) as error:
        print (error)
