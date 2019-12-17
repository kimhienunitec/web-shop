from common import db


def checkLogin(username, password):
    return db.loadsingle("select * from taikhoan where tendangnhap = '{0}' and matkhau = '{1}'".format(username, password))

def add(query):
    return


def delete(query):
    return


def update(query):
    return


