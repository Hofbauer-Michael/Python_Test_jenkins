pipeline

  agent {

    docker {

      image 'python:3.5.1'

    }

  }



    stage ('Test') {

      steps {

        sh 'py.test --junit-xml test-reports/results.xml sources/test.py'

      }

      post {

        always {

          xunit 'test-reports/results.xml'

        }

      }

    }

  }

}