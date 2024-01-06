
pipeline {
    agent any

    stages {
        stage('Checkout Codebase') {
            steps {
                cleanWs()
                git branch: 'main', url: 'https://github.com/Hofbauer-Michael/Python_Test_jenkins.git'
            }
        }
        stage('build') {
            steps {
                powershell 'pytest -v test.py -report'
            }
        }  
        stage('Built report') {
            steps {
                powershell '.mvnw clean install site surefire-report:target'
                powershell 'tree'
            }
        }                



    post {
        always{
            junit allowEmptyResults: true, testResults: 'target/surefire-reports/*.xml'

        }

    }
}
