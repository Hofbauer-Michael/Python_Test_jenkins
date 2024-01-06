
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
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
