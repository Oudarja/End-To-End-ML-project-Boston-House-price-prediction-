import pickle
from fastapi import FastAPI
from model import HouseFeatures 
import numpy as np
import pandas as pd


app = FastAPI(title="House Price Prediction API",
              description="An API to predict house prices based on various features.",)


@app.post("/predict")
def predict_house_price(features: HouseFeatures):
    # Load the pre-trained model
    model = pickle.load(open("notebook/regressor_model.pkl", "rb"))
    # load scaler
    scaler = pickle.load(open("notebook/scaler.pkl", "rb"))
    # Prepare the input data
    # dataframe why? 
    # because model expect 2d array
    # converting pydantic model to dataframe
    input_data = pd.DataFrame([features.dict()])
    # scale or preprocess input_data if necessary
    # For example, if you used StandardScaler for training, you should use it here
    input_data = scaler.transform(input_data)
    # Make a prediction
    prediction = model.predict(input_data)

    # 0 index to get the single prediction value
    # Return the prediction as a JSON response
    # why prediction[0]?
    # because prediction is an array and we want the single value
    # if only prediction is passed it creates issue in json serialization
    # json serialization means converting python object to json format
    return {"predicted_price": prediction[0]}




# command to run the app
# uvicorn app:app --reload
