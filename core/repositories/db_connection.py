import mysql.connector


class DbConnector():

    def dev_env(self):
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="mysqlpasswd",
            database="snailRacing"
        )

    def prod_env(self):
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="mysqlpasswd",
            database="snailRacing"
        )

    def test_env(self):
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="mysqlpasswd",
            database="snailRacing"
        )