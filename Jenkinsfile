pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
                echo 'Hello World1'
                bat 'pytest test.py'

            }
        }
    }
}
