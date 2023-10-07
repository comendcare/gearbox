from flask import Flask, jsonify, request
from pydantic import ValidationError
from models import TaskModel


from facades.service_facade import ServiceFacade  # Import from facades package

app = Flask(__name__)
ai_facade = ServiceFacade()


@app.route('/task', methods=['POST'])
def task():
    request_data = request.get_json()

    try:
        validated_request_data = TaskModel(**request_data)
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400

    result = ai_facade.perform_task(validated_request_data)

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
