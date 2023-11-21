    pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh '''
                docker build -t mcmuds/task1-nginx-network-image nginx
                docker build -t mcmuds/task1-flask-app .
                '''
            }

        }
        stage('Push') {
            steps {
                sh '''
                docker push mcmuds/task1-nginx-network-image
                docker push mcmuds/task1-flask-app
                '''         
            }

        }
        stage('Deploy') {
            steps {
                sh '''
                docker stop net-task1 || true               
                docker stop net-app || true               
                docker rm net-task1 || true
                docker rm net-app || true
                docker run -d --name net-app mcmuds/task1-flask-app
                docker run -d -p 80:5500 --name net-task1 mcmuds/task1-nginx-network-image
                '''
            }

        }

    }

}