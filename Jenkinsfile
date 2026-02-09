pipeline {
    agent any

    environment {
        AI_API_KEY = credentials('AI_API_KEY')
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Khalandar-web/customer-support-ai-saas.git'
            }
        }

        stage('Stop Existing Containers') {
            steps {
                sh 'docker-compose down || true'
            }
        }

        stage('Build Docker Images') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Run Containers') {
            steps {
                sh 'AI_API_KEY=$AI_API_KEY docker-compose up -d'
            }
        }
    }

    post {
        success {
            echo '✅ Deployment successful with secure API key'
        }
        failure {
            echo '❌ Deployment failed'
        }
    }
}
