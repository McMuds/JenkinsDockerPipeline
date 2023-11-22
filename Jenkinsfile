    pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh '''
                docker build -t mcmuds/task1-app .
                '''
            }

        }
        stage('Push') {
            steps {
                sh '''
                docker push mcmuds/task1-app
                '''         
            }

        }
        stage('Deploy') {
            steps {
                sh '''
                kubectl apply -f .
                kubectl get services
                '''
            }

        }

    }

}