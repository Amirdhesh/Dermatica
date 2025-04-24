import cv2
import uvicorn
import json
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from PIL import Image
import numpy as np
from Model import answer_question, model_prediction,Model

app = FastAPI()

@app.on_event("startup")
async def load_data():
    print("Hello")
    with open("Skin_disease_categories.json", "r") as f:
        Model.skin_disease_categories = json.load(f)

    with open("Skin_disease_info.json", "r") as f:
        Model.skin_disease_info = json.load(f)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Prediction(BaseModel):
    disease : str
    comment : str


class Chat(BaseModel):
    message : str


@app.post("/api/model", status_code=200,response_model=Prediction)
async def model(file: UploadFile = File(...)):
        if not file.content_type.startswith("image/"):
            raise HTTPException(status_code=400, detail="File must be an image.")
        try:
            img = Image.open(file.file)
            # Convert PIL image to OpenCV format
            img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        except Exception:
            raise HTTPException(status_code=400, detail="Invalid image")

        # Pass the image to the model_prediction function
        response = model_prediction(img_cv)
        
        return response


@app.post("/api/chatbot", status_code=200,response_model=Chat)
def chatbot(chat: Chat):
     response = answer_question(chat.message)
     return Chat(message=response)
     

if __name__ == "__main__":
    uvicorn.run("main:app",reload=True)
