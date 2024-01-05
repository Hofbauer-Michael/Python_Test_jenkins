
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                git 'https://github.com/Hofbauer-Michael/Python_Test_jenkins.git'
            }
        }
        stage('Test') {
            steps {
                echo 'Test Stage'
            }
        }                
        stage('deploy') {
            steps {
                echo 'Deploy Stage'
        
            }
        }
    }
}
