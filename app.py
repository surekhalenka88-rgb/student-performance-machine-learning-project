from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    math_score = float(request.form['math'])
    reading_score = float(request.form['reading'])

    prediction = model.predict([[math_score, reading_score]])

    return render_template(
        'index.html',
        result=round(prediction[0], 2)
    )

if __name__ == '__main__':
    app.run(debug=True)
    