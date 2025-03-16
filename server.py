from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Autoriser les requêtes depuis GitHub Pages

API_KEY = "04cb4ed4a8c73c7b33816cc58a5d59b44be08615"  # Remplace par ta vraie clé API LeakCheck

@app.route('/check-site', methods=['GET'])
def check_site():
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "URL requise"}), 400

    response = {"securityRating": "A", "threatType": "None"}
    return jsonify(response)

@app.route('/check-breach', methods=['GET'])
def check_breach():
    email = request.args.get("email")
    if not email:
        return jsonify({"error": "Email requis"}), 400

    url = f"https://leakcheck.io/api?key={API_KEY}&check={email}"
    response = requests.get(url)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Impossible de récupérer les données"}), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
