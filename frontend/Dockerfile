# Image Node.js
FROM node:22-alpine

WORKDIR /app

# Installation des dépendances Node
COPY package*.json ./
RUN npm install

# Copie du code source
COPY . .

# Port de Vite
EXPOSE 5173

# Lancement de l'application avec accès externe
CMD ["npm", "run", "dev", "--", "--host"]
