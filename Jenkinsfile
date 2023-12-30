pipeline {
    agent any
    stages {
        stage ('version') {
            steps {
                sh 'python 3 --version'
            }
        }
        stage('hello'){
            steps {
                sh 'python 3 hello.py'
            }
        }
    }
}

