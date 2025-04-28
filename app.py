from flask import Flask, request, jsonify
import requests
import os
from flask_cors import CORS  

app = Flask(__name__)
CORS(app) 

@app.route('/predict', methods=['POST'])
def predict():
    try:
        user_data = request.json

        url = os.getenv("API_URL", "http://default-url.com/score")
        api_key = os.getenv("API_KEY", "default-api-key")

       
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        response = requests.post(url, headers=headers, json=user_data)

        # Vérification de la réponse de l'API
        if response.status_code == 200:
            return jsonify(response.json())  
        else:
            return jsonify({"error": "Erreur lors de la prédiction", "details": response.text}), response.status_code

    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Erreur réseau", "details": str(e)}), 500
    except Exception as e:
        return jsonify({"error": "Erreur inconnue", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
