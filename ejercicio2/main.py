import mysql.connector
from flask import Flask


if __name__ == '__main__':
    app = Flask(__name__)

    repository = Repository()

    routes = Routes()
