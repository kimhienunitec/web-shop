import pyodbc as db

connection = 'Driver={ODBC Driver 11 for SQL Server};Server=DESKTOP-V2G1671\MSSQLSERVER2014;Database=DUAN_PYTHON_SHOP;uid=sa;pwd=Continue19'
# Create connect to database in sql server

def loadsingle(query):
    mydb = db.connect(connection)
    mycursor = mydb.cursor()
    mycursor.execute(query)
    rowdata = mycursor.fetchone()
    mycursor.close()
    return rowdata

def loadlist(query):
    mydb = db.connect(connection)
    mycursor = mydb.cursor()
    mycursor.execute(query)
    rowdata = mycursor.fetchall()
    mycursor.close()
    return rowdata

def delete(table, column, value):
    query="delete from {0} where {1} = {2}".format(table, column, value)
    mydb=db.connect(connection)
    mycursor=mydb.cursor()
    mycursor.execute(query)
    mycursor.close()
    return




