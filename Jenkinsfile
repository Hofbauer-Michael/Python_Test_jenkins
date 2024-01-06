pipeline {
 agent any

 stages {
  stage ('Assign Test Type') {
   steps {
    script {
     if (pTrigger != "PULL_REQUEST_CHECKER") {
      switch (WORKSPACE) {
       case ~/.*\\FUNCTIONAL\\.*/:
        pTestType = "FUNCTIONAL"
        break
       case ~/.*\\STRESS\\.*/:
        pTestType = "STRESS"
        break
       case ~/.*\\ROBUSTNESS\\.*/:
        pTestType = "ROBUSTNESS"
        break
       default:
        pTestType = "UNASSIGNED"
        break
      }
     println pTestType
     }
    }
   }
  }
    }
