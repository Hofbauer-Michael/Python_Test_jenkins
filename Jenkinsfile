pipeline {
    agent any

    stages {
        stage('Installing packages') {
            steps {
                    git branch: 'main', url: 'https://github.com/Hofbauer-Michael/Python_Test_jenkins.git'
                    sh 'python3 ops.py'
                    sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                    sh 'python3 test.py'
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
