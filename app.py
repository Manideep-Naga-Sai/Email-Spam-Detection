from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('models/spam_model.pkl', 'rb'))
vectorizer = pickle.load(open('models/vectorizer.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['message']
    data = vectorizer.transform([message])
    result = model.predict(data)

    if result[0] == 1:
        prediction = "Spam Message"
    else:
        prediction = "Not Spam"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
