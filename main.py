
from flask import Flask, jsonify, request
from facades.service_facade import ServiceFacade  # Import from facades package

app = Flask(__name__)
ai_facade = ServiceFacade()


@app.route('/task', methods=['POST'])
def task():
    request_data = request.get_json()
    task_type = request_data.get('type')
    task_data = request_data.get('data')

    result = ai_facade.perform_task(task_type, task_data)

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
