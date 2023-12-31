pipeline

  agent {

    docker {

      image 'python:3.5.1'

    }

  }

  stages {

    stage ('Test1') {

      steps {

        sh 'py.test --junit-xml test-reports/results.xml sources/test_calc.py'

      }

    }

    stage ('Test') {

      steps {

        sh 'py.test --junit-xml test-reports/results.xml sources/test_calc.py'

      }

      post {

        always {

          xunit 'test-reports/results.xml'

        }

      }

    }

  }

}