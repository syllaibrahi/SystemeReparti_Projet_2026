 Système Réparti : Ma Boutique Répartie

Ce projet consiste en la conception et le déploiement d'une architecture microservices moderne, intégrant un frontend React, un backend Flask et une base de données PostgreSQL.

 Architecture du Projet

1. Backend (API REST)
- Framework : Flask (Python 3.11-slim).
- Modèles : Gestion des `Produits` et des `Utilisateurs`.
- Rôle : Serveur d'API gérant la logique métier et l'accès aux données.
- Port : `5000`.

2. Frontend (Interface Utilisateur)
- Framework : React.js via Vite.
- Dossier : `frontend/`.
- Rôle : Interface dynamique consommant l'API Backend pour afficher les produits.
- Port : `5173`.

3. Communication & Conteneurisation
- Format : JSON via requêtes HTTP (REST).
- Docker : Utilisation de Dockerfiles optimisés pour chaque service.
- Orchestration : Docker Compose pour lier le frontend, le backend et la base de données.

Routes de l'API (Mise à jour)

| Route | Méthode | Description | Statut |
| :--- | :--- | :--- | :--- |
| `/api/produits` | GET | Liste des produits (Ordinateurs, Claviers, etc.) | Validé |
| `/api/utilisateurs` | GET | Liste des utilisateurs (Admin, User) | Validé |
| `/api/info` | GET | Informations système et version |  Validé |

---
  Installation et Lancement (Local)

1.Prérequis : Docker et Docker Compose installés.
2. Lancer le projet :
   ```bash
   docker compose up --build -d
