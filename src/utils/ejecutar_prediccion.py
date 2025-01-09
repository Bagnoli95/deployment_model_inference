import logging
import numpy as np
from sklearn.discriminant_analysis import StandardScaler

from utils.schemas import PredictionRequest 

# Configurar el logger
logger = logging.getLogger(__name__)

def predecir(model, request: PredictionRequest):
    # Convertir los datos del request en un array numpy
    data = np.array([[request.Education,
                    request.Income,
                    request.Kidhome,
                    request.Teenhome,
                    request.Recency,
                    request.Wines,
                    request.Fruits,
                    request.Meat,
                    request.Fish,
                    request.Sweets,
                    request.Gold,
                    request.NumDealsPurchases,
                    request.NumWebPurchases,
                    request.NumCatalogPurchases,
                    request.NumStorePurchases,
                    request.NumWebVisitsMonth,
                    request.AcceptedCmp3,
                    request.AcceptedCmp4,
                    request.AcceptedCmp5,
                    request.AcceptedCmp1,
                    request.AcceptedCmp2,
                    request.Complain,
                    request.Response,
                    request.Edad,
                    request.En_Convivenvia,
                    request.Hijos,
                    request.Tamanho_familiar,
                    request.Es_Padre,
                    request.Clusters]])
    
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)
    
    print(f"Datos para predicción: data: {data}")
    print(f"Datos para predicción: data_scaled: {data_scaled}")

    # Realizar la predicción
    prediction = model.predict(data_scaled)
    print(f"Resultado de la predicción: {prediction}")
    
    return prediction
