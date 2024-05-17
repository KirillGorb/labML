import pickle
import numpy as np
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

loaded_model_knn = pickle.load(open('model/AI.ist', 'rb'))
loaded_model_Log = pickle.load(open('model2/Iris_pickle_file.pkl', 'rb'))
loaded_model_Tree = pickle.load(open('model3/AI.ist', 'rb'))


def m1(age, education, sports):
    X_new = np.array([[int(age)]])
    pred = loaded_model_knn.predict(X_new)
    return "Ответ: " + str(pred[0])


def m2(age, education, sports):
    X_new = np.array([[int(age), int(education), int(sports)]])
    pred = loaded_model_Log.predict(X_new)
    return "Ответ: " + str(pred[0])


def m3(age, education, sports):
    X_new = np.array([[int(age), int(education), int(sports)]])
    pred = loaded_model_Tree.predict(X_new)
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
        if id == 1:
            rez = m1(age, education, sports)
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


if __name__ == "__main__":
    app.run(debug=True)