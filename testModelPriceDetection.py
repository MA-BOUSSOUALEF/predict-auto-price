import requests
import json

# Ton endpoint
url = "http://124fa2c7-a362-45ca-a73d-c35d8571af50.francecentral.azurecontainer.io/score"

# Ta clé API
api_key = "LvIWawQKK66JnVvzwbaAJP8HSrDf7kHF"

# Tes données à envoyer (format correct)
payload = {
    "Inputs": {
        "WebServiceInput0": [
            {
               "symboling": 3,
            "make": "alfa-romero",
            "fuel-type": "gas",
            "aspiration": "std",
            "num-of-doors": "two",
            "body-style": "convertible",
            "drive-wheels": "rwd",
            "engine-location": "front",
            "wheel-base": 88.6,
            "length": 168.8,
            "width": 64.1,
            "height": 48.8,
            "curb-weight": 2548,
            "engine-type": "dohc",
            "num-of-cylinders": "four",
            "engine-size": 130,
            "fuel-system": "mpfi",
            "bore": 3.47,
            "stroke": 2.68,
            "compression-ratio": 9.0,
            "horsepower": 190,
            "peak-rpm": 5000,
            "city-mpg": 21,
            "highway-mpg": 27
            }
        ]
    }
}

# Entêtes avec la clé d'API
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Envoi de la requête POST
response = requests.post(url, headers=headers, json=payload)

# Affiche la réponse
print(response.status_code)
print(response.json())
