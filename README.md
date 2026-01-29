Architecture du Projet (Backend & Frontend)
1. Backend (API REST)

    Framework : Flask (Python 3.9).

    Fichier principal : backend/app.py.

    Rôle : Serveur d'API gérant la logique métier et les routes JSON.

    Port : 5000.

2. Frontend (Interface)

    Framework : React.js via Vite.

    Dossier : frontend/.

    Rôle : Interface utilisateur dynamique consommant l'API Backend.

    Port : 5173.

3. Communication (L'API)

    Format : JSON via requêtes HTTP.

    Protocole : REST (découplage total entre le client et le serveur).
