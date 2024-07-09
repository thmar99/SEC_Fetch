#test file

from mysql.connector import Error
import mysql.connector


def get_base(password, database):
    '''retrieves specified database. Requires a pre-established password and MySQL database
       Runs on local device'''
    print('\nconnecting to mysql server\n')
    try:
        mydb = mysql.connector.connect(host='localhost',user='root',password=password, database=database)
        print('\nmysql server connection succesful\n')
        return mydb
    except Error as e:
        print('mysql connection failed\n', e)
        return False
    return True

