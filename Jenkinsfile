pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devops-lab:latest .'
            }
        }

        stage('Run Tests in Container') {
            steps {
                sh 'docker run --rm devops-lab:latest pytest'
            }
        }
    }
}