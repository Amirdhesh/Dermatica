from flask import Flask, render_template, request, jsonify
from PIL import Image
from Model import model_prediction
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/model", methods=["POST"])
def model():
        file = request.files["image"]
        img = Image.open(file)
        img.save("./image.jpg")
        response = model_prediction()
        print(response)
        if response['success']:
            return jsonify(response)
        else:
            return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
