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
4. Orchestration avec Kubernetes (Minikube)

Le projet a été migré vers un cluster Kubernetes pour garantir la haute disponibilité, la scalabilité et la persistance des données.
 Concepts Clés implémentés :
- Deployments : Gestion automatisée des répliques pour le Frontend, le Backend et la Base de données.
 - Services : 
     `NodePort` : Pour l'accès externe (Frontend & API).
     `ClusterIP` : Pour la communication sécurisée interne vers la base de données.
- Persistance (PVC) : Utilisation d'un PersistentVolumeClaim de 1Go pour garantir que les données de la base de données ne sont pas perdues lors d'un redémarrage des Pods.



 Architecture du Cluster  

| Microservice | Identifiants / Config | Objet Kubernetes | Statut |
| :--- | :--- | :--- | :--- |
| **Frontend** | Port 5173 | Deployment & Service |  Running |
| **Backend** | Port 5000 | Deployment & Service |  Running |
| **PostgreSQL** | DB: `ibrahima_db` / User: `ibrahima` | Deployment & Service |  Running |
| **Stockage** | `postgres-pvc` (1Gi) | PersistentVolumeClaim |  Bound |

 Commandes de Déploiement

1. **Initialisation de l'environnement :**
   ```bash
   minikube start
   eval $(minikube docker-env)

    Déploiement de la base de données (Persistance incluse) :
    Bash

    kubectl apply -f k8s/db-deployment.yaml

    Déploiement de l'application (Backend & Frontend) :
    Bash

    kubectl apply -f k8s/backend-deployment.yaml
    kubectl apply -f k8s/frontend-deployment.yaml

    Vérification de l'état du système :
    Bash

    kubectl get pods,pvc,svc

🔗 Accès à l'application

Pour récupérer les URLs d'accès sur l'EliteBook :

    Frontend : minikube service frontend-service --url

    API Backend : minikube service backend-service --url