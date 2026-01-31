# Image légère de Python
FROM python:3.11-slim

# Dossier de travail dans le conteneur
WORKDIR /app

# ... (votre code précédent)
COPY requirements.txt .

# On met à jour pip et on installe avec un timeout plus long
RUN pip install --no-cache-dir --default-timeout=1000 -r requirements.txt

# ... (le reste)
# Copie du reste du code backend
COPY . .

# Port de Flask
EXPOSE 5000

# Lancement du serveur
CMD ["python", "app.py"]
