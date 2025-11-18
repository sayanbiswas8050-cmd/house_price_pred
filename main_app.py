from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from model.prediction import predict_output,MODEL_VERSION,model
  
app = FastAPI()

## human readable
@app.get("/")
def home():
    return {
        "message": "House prediction API"
        }
## machine readable
@app.get("/info")
def info():
    return {
        "status": "OK",
        "version":MODEL_VERSION,
        "model_loaded" : model is not None
        }

@app.post("/predict")
def predict_premium(data:UserInput):
    
    user_input = {
        "location":data.location,
        "BHK": data.BHK,
        "bath": data.bath,
        "total_sqft": data.total_sqft
    }
    try:
        prediction = predict_output(user_input)
        return JSONResponse(status_code=200,content={"prediction category":prediction})
    except Exception as e: 
        return JSONResponse(status_code=500,content=str(e))
