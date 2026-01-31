from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app) # Autorise le frontend à appeler l'API

# --- Configuration de la Base de Données ---
# On utilise des variables d'environnement (bonne pratique DevOps)  
DB_USER = os.getenv('DB_USER', 'admin')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
DB_HOST = os.getenv('DB_HOST', 'localhost') # Sera 'db' plus tard avec Docker
DB_NAME = os.getenv('DB_NAME', 'db_projet')

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- MODÈLES (Conformément à l'énoncé) [ 
class Utilisateur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

class Produit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    prix = db.Column(db.Float, nullable=False)

# --- ROUTES API ---

@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({"message": "L'API Backend est opérationnelle !"})

@app.route('/api/produits', methods=['GET'])
def get_produits():
    # Pour l'instant on renvoie une liste fictive avant de configurer PostgreSQL
    produits = [
        {"id": 1, "nom": "Ordinateur", "prix": 1200.50},
        {"id": 2, "nom": "Clavier", "prix": 45.0}
    ]
    return jsonify(produits)

@app.route('/api/utilisateurs', methods=['GET'])
def get_utilisateurs():
    # Remplace par ton vrai modèle si le nom diffère (ex: User.query.all())
    # Ici on simule une réponse pour valider la route
    utilisateurs = [
        {"id": 1, "nom": "Ibrahima", "role": "Admin"},
        {"id": 2, "nom": "abdou", "role": "User"}
    ]
    return jsonify(utilisateurs), 200

if __name__ == '__main__':
    # host='0.0.0.0' est crucial pour être accessible depuis Docker/Kubernetes [cite: 7, 8]
    app.run(host='0.0.0.0', port=5000, debug=True)