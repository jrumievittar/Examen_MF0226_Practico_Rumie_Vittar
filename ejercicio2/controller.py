from flask import Flask, jsonify


class Routes:
    def __init__(self, app):
        self.repository = app
        self.repository = Flask(__name__)

        @self.app.route('/v1/student/<int:student_id>', methods=['GET'])
        def get_student_id:
            :
                result = self.repository.get_student_by_id()
                return jsonify(result), 200
            except Exception as e:
                print(e)

