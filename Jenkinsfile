pipeline {
    agent none
    stages {
        stage('Test') {
            agent {
                docker {
                    image 'python:3'//select python 3
                }
            }
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
     				sh 'pip install django --user'//install django
              		sh 'python manage.py migrate'//creates the sqlite database
               		sh 'python manage.py test'//run test
  				}
            }
        }
        
    }
}