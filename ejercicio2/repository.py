class Repository:
    def __init__(self, connector_database):
        self.connector = connector_database

    def get_student_by_id(self, id):
        query = "SELECT * FROM movies WHERE id = {}".format(id)
        result = self.connector.connect(query)
        return result
