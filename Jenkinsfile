pipeline  {
    agent any
    stages {
        stage('test') {
            steps {
                sh "python3 tests/test_app.py"
            }
        }
    }
    post {
        always  {
            archiveArtifacts artifacts: "htmlcov/*"
        }
    }
}