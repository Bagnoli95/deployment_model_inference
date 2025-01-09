import sys
import os
import logging

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
from utils.schemas import PredictionRequest 

# Configurar el log
logger = logging.getLogger(__name__)

# Agregar la raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.ejecutar_prediccion import predecir
from utils.model_loader import load_model

# Ruta del modelo
model_path = "../models/trained_model_2025-01-08.joblib"
logger.info(f"Model path: {model_path}")

# Intentar cargar el modelo
try:
    model = load_model(model_path)
    logger.info("Modelo cargado exitosamente")
except Exception as e:
    logger.error(f"Error al cargar el modelo: {e}")
    raise



# Inicializar la aplicación FastAPI
app = FastAPI()

@app.get("/model")
async def root():
    return {"message": "Hello World"}

@app.post("/model/predict")
async def inferir(request: PredictionRequest):
    try:
        logger.info(f"Solicitud recibida: {request}")

        prediction = predecir(model, request)

        return {"prediction": prediction.tolist()}
    
    except Exception as e:
        logger.error(f"Error durante la predicción: {e}")
        raise HTTPException(status_code=500, detail=f"Error durante la predicción: {e}")
    
@app.post("/model/test")
async def test():
    return {"message": "Test successful"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=4579)
