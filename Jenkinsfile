    pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh '''
                docker build -t mcmuds/task1jenkins .
                '''
            }

        }
        stage('Push') {
            steps {
                sh '''
                docker push mcmuds/task1jenkins
                '''
            }

        }
        stage('Deploy') {
            steps {
                sh '''
                docker run -d -p 80:5500 --name task1 mcmuds/task1jenkins
                '''
            }

        }

    }

}