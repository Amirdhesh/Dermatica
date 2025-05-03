import joblib
import numpy as np
import cv2
import os
import json
from dotenv import load_dotenv
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.models import load_model
from fastapi import HTTPException
from Model.LLM import LLM
from Model.SkinDisease import Categories, Classes

load_dotenv()

le=joblib.load(os.environ.get("PKL_FILE"))
model = load_model(os.environ.get("H5_FILE"))

def model_prediction(img):

    try:

        classes = Classes()
        skin_disease_categories = Categories()

        # Resize and preprocess the image
        img = cv2.resize(img, (224,224))
        img = preprocess_input(np.array([img]))

        # Predict the class
        predictions = model.predict(img)
        predicted_class_index = np.argmax(predictions)
        output = le.classes_[predicted_class_index]
        

        # Get disease and comment
        disease = skin_disease_categories[output]
        comment = LLM(message = disease, mode = "model")
        return {"disease":disease,"comment":comment}
      
    except Exception:
        raise HTTPException(status_code = 500, detail = "Model not working.")
        