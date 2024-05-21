from flask import  jsonify, request
from app import app, get_metrics,get_metrics2,get_metrics1

@app.route('/api/metrics/<int:model_id>', methods=['POST'])
def api_metrics(model_id):
    data = request.get_json()
    age = data.get('age')
    education = data.get('education')
    sports = data.get('sports')
    y = data.get('y')
    if model_id == 1:
        accuracy = get_metrics(age, education, sports, y)
    elif model_id == 2:
        accuracy = get_metrics1(age, education, sports, y)
    elif model_id == 3:
        accuracy = get_metrics2(age, education, sports, y)
    return jsonify({'accuracy': accuracy})

