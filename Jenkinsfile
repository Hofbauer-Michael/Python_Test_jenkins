
pipeline {
    agent any

    stages {
        stage('Checkout Codebase') {
            steps {
                cleanWs()
                git branch: 'main', url: 'https://github.com/Hofbauer-Michael/Python_Test_jenkins.git'
                

        
            }
        }
        stage('test') {
            steps {
                powershell 'pytest -v test.py'
                

        
            }
        }
    }
}
