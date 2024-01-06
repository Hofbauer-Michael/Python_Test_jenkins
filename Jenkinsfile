pipeline {
 agent any

 
 options {
  timestamps ()
 }
 stages {
  stage ('Assign Trigger') {
   steps {
    script {
     switch (WORKSPACE) {
      case ~/.*\\DEVELOP\\.*/:
  
       break
      case ~/.*\\MASTER\\.*/:

       break
      case ~/.*\\PLAYGROUND\\.*/:

       break
      case ~/.*\\SMOKE\\.*/:

       break
      case ~/.*PULL_REQUEST_CHECKER.*/:

       break
      default:
       error("Undefined trigger type!")
       break
     }

    }
   }
  }
}
    }
