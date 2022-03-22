pipeline  {
    agents any
    stages {
        stage('test') {
            steps {
                sh "bash flask-app/test_basic.sh"
            }
        }
    }
    post {
        always  {
            archiveArtifacts: "htmlcov/*"
        }
    }
}