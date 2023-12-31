pipeline {
    agent any

    stages {
        stage('Environment Installation') {
            steps {
              virtualenv venv --distribute
              .venv/bin/activate
              powershell """

              pip install virtualenv==20.25.0
              python -m venv ${WORKSPACE}
              Scripts\\activate.ps1
              pip install -r requirements.txt
              activate
              """
            }
        }
    }
}


