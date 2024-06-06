import oracledb

class DatabaseConnectionManager:
    def __init__(self):
        self.conn = None

    def database_connect(self):

        if self.conn is None:
            #create connection
            self.conn = oracledb.connect(user="hr", password="hr",
                                    host="localhost", port=1521, sid="orcl")
            print(self.conn.version)

        return  self.conn

    def close_database_coonection(self):
        print("inside close")
        if self.conn is not None:
            #close connection
            self.conn.close()
            print("connection closed")
            self.conn = None

    def run_sql(self,sql):
        print("inside run sql")
        cursor = self.conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
