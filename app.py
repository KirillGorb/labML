import pickle
import numpy as np
from flask import Flask, jsonify, request, render_template, url_for, redirect
from sklearn.metrics import classification_report, accuracy_score

app = Flask(__name__)

loaded_model_knn = pickle.load(open('model/AI.ist', 'rb'))
loaded_model_Log = pickle.load(open('model2/AI.ist', 'rb'))
loaded_model_Tree = pickle.load(open('model3/AI.ist', 'rb'))

app.a = 0
app.e = 0
app.s = 0
app.rez = 0
app.id = 0


def get_metrics(a, e, s, y):
    x_new = np.array([[int(a), int(e), int(s)]])
    y_pred = loaded_model_knn.predict(x_new)
    y_true = np.array([int(y)])
    return accuracy_score(y_true, y_pred)


def get_metrics1(a, e, s, y):
    x_new = np.array([[int(a), int(e), int(s)]])
    y_pred = loaded_model_Log.predict(x_new)
    y_true = np.array([int(y)])
    return accuracy_score(y_true, y_pred)


def get_metrics2(a, e, s, y):
    x_new = np.array([[int(a), int(e), int(s)]])
    y_pred = loaded_model_Tree.predict(x_new)
    y_true = np.array([int(y)])
    return classification_report(y_true, y_pred)


def m(age, education, sports):
    x_new = np.array([[int(age), int(education), int(sports)]])
    pred = loaded_model_knn.predict(x_new)
    app.ar = x_new
    app.rez = pred[0]
    return "Ответ: " + str(pred[0])


def m2(age, education, sports):
    x_new = np.array([[int(age), int(education), int(sports)]])
    pred = loaded_model_Log.predict(x_new)
    app.rez = pred[0]
    return "Ответ: " + str(pred[0])


def m3(age, education, sports):
    x_new = np.array([[int(age), int(education), int(sports)]])
    pred = loaded_model_Tree.predict(x_new)
    app.ar = x_new
    app.rez = pred[0]
    return "Ответ: " + str(pred[0])


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/into/<int:id>', methods=['POST', 'GET'])
def into(id):
    if request.method == "POST":
        age = request.form['age']
        education = request.form['education']
        sports = request.form['sports']
        rez = ""

        app.id = id
        app.a = age
        app.e = education
        app.s = sports

        if id == 1:
            rez = m(age, education, sports)
        elif id == 2:
            rez = m2(age, education, sports)
        elif id == 3:
            rez = m3(age, education, sports)
        return redirect(url_for('lab', rez=rez))
    else:
        return render_template("into.html")


@app.route('/lab/<string:rez>')
def lab(rez):
    return render_template("lab.html", rez=rez)


@app.route('/metrics')
def metrics():
    if app.id == 1:
        rems = get_metrics(app.a,app.e, app.s, app.rez)
        return render_template("metrics.html", rmse=rems)
    elif app.id == 2:
        rems = get_metrics1(app.a, app.e, app.s, app.rez)
        return render_template("metrics.html", rmse=rems)
    elif app.id == 3:
        rems = get_metrics2(app.a, app.e, app.s, app.rez)
        return render_template("metrics.html", rmse=rems)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.route('/api/predict/<int:model_id>', methods=['POST'])
def api_predict(model_id):
    data = request.get_json()
    age = data.get('age')
    education = data.get('education')
    sports = data.get('sports')
    prediction = ""
    if model_id == 1:
        prediction = m(age, education, sports)
    elif model_id == 2:
        prediction = m2(age, education, sports)
    elif model_id == 3:
        prediction = m3(age, education, sports)
    return jsonify({'prediction': prediction})


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


if __name__ == "__main__":
    app.run(debug=True)