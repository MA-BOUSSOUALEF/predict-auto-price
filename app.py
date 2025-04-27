from flask import Flask, request, jsonify
import requests
import os
from flask_cors import CORS  # Importer CORS

app = Flask(__name__)
CORS(app)  # Appliquer CORS à toutes les routes

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Récupérer les données envoyées dans la requête POST
        user_data = request.json

        # URL de l'API
        url = os.getenv("API_URL", "http://default-url.com/score")
        api_key = os.getenv("API_KEY", "default-api-key")

        # En-têtes pour la requête API
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        # Envoi de la requête POST à l'API
        response = requests.post(url, headers=headers, json=user_data)

        # Vérification de la réponse de l'API
        if response.status_code == 200:
            return jsonify(response.json())  # Retourner la réponse JSON
        else:
            return jsonify({"error": "Erreur lors de la prédiction", "details": response.text}), response.status_code

    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Erreur réseau", "details": str(e)}), 500
    except Exception as e:
        return jsonify({"error": "Erreur inconnue", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
