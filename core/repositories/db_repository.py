import mysql.connector

class DbConnection():

    def __init__(self, connection_info):
        self.db = mysql.connector.connect(connection_info)

    def create_cursor(self):
        self.db_cursor = self.db.cursor()

    def execute(self, sql):
        try:
            self.db.execute(sql)
            return True
        except:
            return False

    def commit(self):
        self.db.commit()
        return True
