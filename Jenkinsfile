
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
    }

    post {
        always{
            junit allowEmptyResults: true, testResults: 'target/surefire-reports/*.xml'

        }

    }
}
