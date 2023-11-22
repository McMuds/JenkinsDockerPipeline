    pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh '''
                docker pull agray998/task1jenk
                docker tag agray998/task1jenk mcmuds/task1-app
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
                sleep 60
                kubectl get services
                '''
            }

        }

    }

}