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
5. Automatisation avec Ansible

L'infrastructure du projet est entièrement automatisée grâce à Ansible, permettant une configuration rapide, reproductible et sans erreur sur n'importe quel poste Linux (Infrastructure as Code).
Objectifs de l'automatisation :

    Vérification d'environnement : Contrôle automatique de la présence de Docker, Minikube et Kubectl sur l'HP EliteBook.

    Gestion de la configuration : Installation automatique des dépendances système (Java, outils réseau).

    Idempotence : Le playbook vérifie l'état actuel et n'applique les changements que si nécessaire.

Configuration Ansible
Élément	Description	Fichier	Statut
Playbook	Logique de déploiement et d'installation	ansible/playbook.yml	Validé
Inventaire	Cible le localhost pour une exécution locale	ansible/hosts.ini	Validé
Vérification	Mode Simulation (--check)	Commande Ansible	Validé
Commande d'exécution

cd ansible/
ansible-playbook -i hosts.ini playbook.yml --check -K

6. Pipeline CI/CD avec Jenkins

Le cycle de vie de l'application est géré par un pipeline d'Intégration et de Déploiement Continus (CI/CD) via Jenkins, assurant que chaque modification de code est testée et déployée automatiquement.
Pipeline Stages (Cycle de vie) :

    Checkout Code : Récupération de la dernière version du code depuis GitHub.

    Build Images : Construction des images Docker pour le Frontend et le Backend.

    Infrastructure Check : Validation de l'état du cluster Kubernetes.

    Deploy to K8s : Mise à jour automatique des Pods avec les nouvelles images.

    Validation : Vérification finale du statut "Running" des services.

Configuration du Pipeline
Composant	Détails	Fichier	Statut
Pipeline Script	Définition des étapes (Declarative Pipeline)	Jenkinsfile	Prêt
Automation	Déploiement automatique sur Minikube	Script Shell K8s	Prêt
Visualisation	Jenkins Stage View	Interface Web	Validé
Visualisation du déploiement final

Une fois le pipeline terminé, l'état global du système peut être vérifié avec :

  kubectl get all
 Conclusion de l'Architecture

L'ensemble de ces 6 étapes transforme le projet ELITE-MARKET d'une simple application locale en un système réparti professionnel, prêt pour l'échelle industrielle avec une gestion automatisée du code à la production.