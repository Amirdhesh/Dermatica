from flask import Flask, render_template, request, jsonify
from PIL import Image
import numpy as np
import cv2
from Model import model_prediction, answer_question
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/model", methods=["POST"])
def model():
        file = request.files["image"]
        img = Image.open(file)

        # Convert PIL image to OpenCV format
        img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

        # Pass the image to the model_prediction function
        response = model_prediction(img_cv)

        if response['success']:
            return jsonify(response)
        else:
            return jsonify(response)

@app.route("/chatbot", methods=["POST"])
def chatbot():
     data = request.get_json()
     user_message = data.get('message')
     response = answer_question(user_message)
     return jsonify(response)
     


if __name__ == "__main__":
    app.run(debug=True)
