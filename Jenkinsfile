pipeline {
    agent {

    stages {
        stage('Environment Installation') {
            steps {
              powershell """
              pip install -m venv virtualenv==16.5.0
              python -m venv ${WORKSPACE}
              Scripts\\activate.ps1
              pip install -r requirements.txt
              deactivate
              """
            }
        }
    }
}
