pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
                echo 'Hello World1'
                sh 'test-reports/results.xml sources/test.py'

            }
        }
    }
}
