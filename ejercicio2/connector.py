import mysql.connector


class ConnectorDatabase:

    def __init__(self, host, user, password, database):
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=int(3307)
        )

    def execute_and_fetchone(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.cursor()
        cursor.close()
        return result

    def execute_and_commit(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            cursor.close()
        except Exception as e:
            print(e)
            self.connection.rollback()