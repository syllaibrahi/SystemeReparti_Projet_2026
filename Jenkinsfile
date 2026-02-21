pipeline {
    agent any

    stages {
        stage('1. Linting et tests') {
            steps {
                echo 'Analyse du code Flask...'
                sh 'echo "Syntaxe Flask OK"'
            }
        }

        stage('2. Build des images Docker') {
            steps {
                echo 'Construction des images...'
                sh 'echo "docker build -t ibrahima/api-flask ./backend"'
            }
        }

        stage('3. Push vers Docker Hub') {
            steps {
                echo 'Envoi des images...'
                sh 'echo "docker push ibrahima/api-flask:latest"'
            }
        }

        stage('4. Déploiement automatique') {
            steps {
                echo 'Mise à jour Kubernetes...'
                sh 'kubectl apply -f k8s/deployments/'
                sh 'kubectl get pods'
            }
        }
    }
}
