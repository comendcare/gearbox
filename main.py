import os
import asyncio
from flask import Flask, jsonify, request
from pydantic import ValidationError
from models import TaskModel
from flask_cors import CORS, cross_origin

from facades.service_facade import ServiceFacade  # Import from facades package

app = Flask(__name__)
CORS(app,
     resources={r"/task": {"origins": ["https://livery.vercel.app", "https://www.scimantic.com/", "http://localhost:3000"]}},
     debug=os.environ.get('ENVIRONMENT') == 'development')
ai_facade = ServiceFacade()


@app.route('/task', methods=['POST'])
def task():
    request_data = request.get_json()

    try:
        validated_request_data = TaskModel(**request_data)
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400

    result = asyncio.run(ai_facade.perform_task(validated_request_data))

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=os.environ.get('ENVIRONMENT') == 'development')
