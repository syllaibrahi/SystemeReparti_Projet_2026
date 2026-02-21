from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
import logging

# Configuration du logging pour suivre les événements dans les logs Docker/Jenkins
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# --- Configuration de la Base de Données (Bonnes pratiques DevOps) ---
DB_USER = os.getenv('DB_USER', 'admin')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
DB_HOST = os.getenv('DB_HOST', 'postgres') # 'postgres' est le nom du service dans K8s
DB_NAME = os.getenv('DB_NAME', 'db_projet')

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- MODÈLES ---
class Utilisateur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

class Produit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    prix = db.Column(db.Float, nullable=False)

# --- INITIALISATION DE LA DB ---
@app.before_first_request
def create_tables():
    """Crée les tables si elles n'existent pas au premier lancement."""
    try:
        db.create_all()
        logger.info("Tables de la base de données créées ou déjà présentes.")
    except Exception as e:
        logger.error(f"Erreur lors de l'initialisation de la DB : {e}")

# --- ROUTES API ---

@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({
        "status": "online",
        "message": "L'API Backend Flask est opérationnelle sur le cluster !",
        "version": "2.1"
    }), 200

@app.route('/api/produits', methods=['GET', 'POST'])
def handle_produits():
    if request.method == 'POST':
        data = request.json
        nouveau_produit = Produit(nom=data['nom'], prix=data['prix'])
        db.session.add(nouveau_produit)
        db.session.commit()
        return jsonify({"message": "Produit ajouté avec succès !"}), 201
    
    # GET : Récupération depuis la DB réelle
    try:
        produits = Produit.query.all()
        return jsonify([{"id": p.id, "nom": p.nom, "prix": p.prix} for p in produits]), 200
    except:
        # Fallback (données fictives) si la DB n'est pas encore prête
        return jsonify([
            {"id": 1, "nom": "HP EliteBook (Demo)", "prix": 1200.50},
            {"id": 2, "nom": "Clavier Pro", "prix": 45.0}
        ]), 200

@app.route('/api/utilisateurs', methods=['GET'])
def get_utilisateurs():
    try:
        users = Utilisateur.query.all()
        return jsonify([{"id": u.id, "nom": u.nom, "email": u.email} for u in users]), 200
    except:
        return jsonify([{"id": 1, "nom": "Ibrahima (Admin)", "role": "DevOps"}]), 200

# Gestionnaire d'erreur global
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Route non trouvée"}), 404

if __name__ == '__main__':
    # host='0.0.0.0' est crucial pour être accessible depuis Docker/Kubernetes
    app.run(host='0.0.0.0', port=5000)