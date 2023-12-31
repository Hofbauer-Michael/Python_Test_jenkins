pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
                sh 'py.test --junit-xml test-reports/results.xml sources/test_calc.py'
            }
        }
    }
}
