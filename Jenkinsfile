pipeline {
 agent {
  label "${params.SLAVE_LABEL}"
 }
 options {
  timestamps ()
 }
 stages {
  stage ('Assign Trigger') {
   steps {
    script {
     switch (WORKSPACE) {
      case ~/.*\\DEVELOP\\.*/:
       pTrigger = "DEVELOP"
       break
      case ~/.*\\MASTER\\.*/:
       pTrigger = "MASTER"
       break
      case ~/.*\\PLAYGROUND\\.*/:
       pTrigger = "PLAYGROUND"
       break
      case ~/.*\\SMOKE\\.*/:
       pTrigger = "SMOKE"
       break
      case ~/.*PULL_REQUEST_CHECKER.*/:
       pTrigger="PULL_REQUEST_CHECKER"
       break
      default:
       error("Undefined trigger type!")
       break
     }
    println pTrigger
    }
   }
  }
}
    }
