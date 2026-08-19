#Database connection
import mysql.connector


def connect_db():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="EMPLOYEE"
    )

    return conn