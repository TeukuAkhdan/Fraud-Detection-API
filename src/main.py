from helper import splitNumCat, onehot
from fastapi import FastAPI, status, Response
import numpy as np
import uvicorn
from pydantic import BaseModel
import pandas as pd
import joblib
import logging

logger = logging.getLogger(__name__)

# params = load_params("config/config.yaml")
app = FastAPI(
    title="Machine Learning - Fraud detector API",
    description="ML API mendeteksi suatu transaksi kartu kredit penipuan atau tidak",
    version="0.0.1",
    debug=True
)



with open('models/tuning/XGB_model_final.pkl', "rb") as file:
    model = joblib.load(file)

# Set use_label_encoder=False



class DataValidation(BaseModel):
    step: int
    type: str
    amount: float
    oldbalanceOrg: float
    newbalanceOrig: float
    oldbalanceDest: float
    newbalanceDest: float

@app.get("/")
def home():
    return {
        "Message": "Machine learning API to detect credit fraud",
        "Health Check": "OK",
        "Version": "0.0.1"
    }

@app.post("/prediction", status_code=status.HTTP_201_CREATED)
def inference(data: DataValidation):
    try:
        features = data.dict()
        features = pd.DataFrame(features, index=[0])
        list_num, list_object = splitNumCat(features)
<<<<<<< HEAD
        encoder_col = {'type': ['CASH_IN', 'CASH_OUT', 'TRANSFER', 'PAYMENT', 'DEBIT']}
=======
        encoder_col = {'type': ['CASH_IN', 'CASH_OUT', 'DEBIT', 'PAYMENT', 'TRANSFER']}
>>>>>>> dc12d1b40bcfe7468f396524d77ce5f36ce07c40
        feature_clean = onehot(data=features, col_cat=list_object, col_num=list_num, encoder_col=encoder_col) 
        pred = model.predict(feature_clean)
        pred_prob = model.predict_proba(feature_clean)

        prob_nofraud = np.round(pred_prob[0, 0] * 100, 2)
        prob_fraud = np.round(pred_prob[0, 1] * 100, 2)

        if pred == 1:
            return {"Result": f"Transaction is potentially fraudulent with a probability of {prob_fraud}%"}
        else:
            return {"Result": f"Transaction is not potentially fraudulent with a probability of {prob_nofraud}%"}

    except Exception as e:
        logger.error(f"Error occurred during inference: {str(e)}")
        return {"error": "An error occurred during inference. Please check your input data."}