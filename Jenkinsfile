pipeline {
    agent any

    stages {
        stage('Installing packages') {
            steps {
                    git branch: 'main', url:  'pip install -r requirements.txt'
                
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
