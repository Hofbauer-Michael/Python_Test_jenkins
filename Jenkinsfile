
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                powershell 'Write-Output "Hello, World!"'
                powershell 'pytest -v test.py'
        
            }
        }
    }
}
