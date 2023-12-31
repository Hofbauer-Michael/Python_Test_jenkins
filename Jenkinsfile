pipeline {
    agent {

    stages {
        stage('Test') {
            steps {
              sh """
              python --version
              python ./test.py
              """
            }
        }
    }
}
