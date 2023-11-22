    pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh '''
                docker build -t agray998/task1jenk .
                '''
            }

        }
        stage('Push') {
            steps {
                sh '''
                docker push mcmuds/task1-flask-app
                '''         
            }

        }
        stage('Deploy') {
            steps {
                sh '''
                kubectl apply -f .
                '''
            }

        }

    }

}