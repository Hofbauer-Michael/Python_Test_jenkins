pipeline {
    agent any

    stages {
        stage('Environment Installation') {
            steps {
              powershell """
              pip install virtualenv==20.25.0
              python -m venv ${WORKSPACE}
              Scripts\\activate.ps1
              pip install virtualenv -r requirements.txt
              activate
              """
            }
        }
    }
}


