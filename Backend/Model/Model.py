import joblib
import numpy as np
import cv2
import os
import json
from dotenv import load_dotenv
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.models import load_model
from fastapi import HTTPException

load_dotenv()

le=joblib.load(os.environ.get("PKL_FILE"))
model = load_model(os.environ.get("H5_FILE"))

skin_disease_categories ={}
skin_disease_info={}

def model_prediction(img):

    try:

        classes = ['Acne and Rosacea Photos',
        'Actinic Keratosis Basal Cell Carcinoma and other Malignant Lesions',
        'Atopic Dermatitis Photos', 'Bullous Disease Photos',
        'Cellulitis Impetigo and other Bacterial Infections',
        'Eczema Photos', 'Exanthems and Drug Eruptions',
        'Hair Loss Photos Alopecia and other Hair Diseases',
        'Herpes HPV and other STDs Photos',
        'Light Diseases and Disorders of Pigmentation',
        'Lupus and other Connective Tissue diseases',
        'Melanoma Skin Cancer Nevi and Moles',
        'Nail Fungus and other Nail Disease',
        'Poison Ivy Photos and other Contact Dermatitis',
        'Psoriasis pictures Lichen Planus and related diseases',
        'Scabies Lyme Disease and other Infestations and Bites',
        'Seborrheic Keratoses and other Benign Tumors', 'Systemic Disease',
        'Tinea Ringworm Candidiasis and other Fungal Infections',
        'Urticaria Hives', 'Vascular Tumors', 'Vasculitis Photos',
        'Warts Molluscum and other Viral Infections']

        # Resize and preprocess the image
        img = cv2.resize(img, (224,224))
        img = preprocess_input(np.array([img]))

        # Predict the class
        predictions = model.predict(img)
        predicted_class_index = np.argmax(predictions)
        output = le.classes_[predicted_class_index]
        

        # Get disease and comment
        disease = skin_disease_categories[output]
        comment = skin_disease_info[output]
        return {"disease":disease,"comment":comment}
      
    except Exception:
        raise HTTPException(status_code = 500, detail = "Model not working.")
        