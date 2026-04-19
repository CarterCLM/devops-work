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
                sh '''
                docker build -t devops-lab:${BUILD_NUMBER} .
                docker tag devops-lab:${BUILD_NUMBER} devops-lab:latest
                '''
            }
        }

        stage('Run Tests in Container') {
            steps {
                sh '''
                docker run --rm devops-lab:${BUILD_NUMBER} pytest
                '''
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                docker stop devops-app || true
                docker rm devops-app || true

                docker ps -q --filter "publish=5001" | xargs -r docker stop
                docker ps -aq --filter "publish=5001" | xargs -r docker rm

                docker run -d -p 5001:5000 --name devops-app devops-lab:latest
                '''
            }
        }
        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                    echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                    docker tag devops-lab:latest clmcarter84/devops-lab:latest
                    docker push clmcarter84/devops-lab:latest
                    '''
                }
            }
        }
    }
}