pipeline  {
    agent any
    stages {
        stage('test') {
            steps {
                sh "bash flask-app/test_basic.sh"
            }
        }
    }
    post {
        always  {
            archiveArtifacts artifacts: "htmlcov/*"
        }
    }
}