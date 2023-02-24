from flask import Flask, request,jsonify,render_template
import joblib
import pandas as pd
import json
import random

# create the app
app = Flask(__name__)


@app.route('/get',methods=['GET','POST'])
def getBotResponse():
    responses = joblib.load("labelencoder/responses.pkl")
    vectorizer = joblib.load("vectorizer/text_vectorizer.pkl")
    model = joblib.load("model/chatbot_model.pkl")
    le = joblib.load("labelencoder/le.pkl")
    usertext = request.args.get('msg')
    chat = pd.Series(usertext)
    X_test_dtm1 = vectorizer.transform(chat)
    y_pred_class1 = model.predict(X_test_dtm1)
    z = le.inverse_transform([y_pred_class1[0]])
    reply = random.choice(responses[z[0]][0])

    return  reply

@app.route('/')
def home():
    return render_template('index.html')


if __name__ =='__main__':
    app.run()

