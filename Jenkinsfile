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
                docker push agray998/task1jenk
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