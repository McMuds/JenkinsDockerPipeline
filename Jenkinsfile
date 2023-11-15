    pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh '''
                docker build -t mcmuds/task1-nginx-network-image .
                '''
            }

        }
        stage('Push') {
            steps {
                sh '''
                docker push mcmuds/task1-nginx-network-image
                '''         
            }

        }
        stage('Deploy') {
            steps {
                sh '''
                docker stop net-task1 || true               
                docker rm net-task1 || true
                docker run -d -p 80:5500 --name net-task1 mcmuds/task1-nginx-network-image
                '''
            }

        }

    }

}