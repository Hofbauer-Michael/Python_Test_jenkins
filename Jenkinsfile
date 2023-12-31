pipeline {
    agent any

    stages {
        stage('Installing packages') {
            steps {
                script {
                    bat 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Pytest') {
            steps {
                echo 'Hello World'
                echo 'Hello World1'
            }
        }

        
    }

}
