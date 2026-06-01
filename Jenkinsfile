pipeline {
  agent {
    docker {
      label 'docker-agent-01'
      image 'python:3.11-slim'
    }
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
        sh "echo 'Workspace: ${env.WORKSPACE}'"
      }
    }

    stage('Install Dependencies') {
      steps {
        sh 'pip install -r requirements.txt --quiet'
      }
    }

    stage('Test') {
      steps {
        sh 'pytest tests/ -v'
      }
    }
  }

  post {
    success {
      echo 'All tests passed — pipeline green'
    }
    failure {
      echo 'Tests failed — check console output above'
    }
  }
}
