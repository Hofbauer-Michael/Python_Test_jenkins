pipeline

  agent {

    docker {

      image 'python:3.5.1'

    }

  }

  stages {

    stage ('Build') {

      steps {

        sh 'python -m py_compile sources/add2vals.py sources/calc.py'

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