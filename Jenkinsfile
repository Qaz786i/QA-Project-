pipeline {
    agents any
    stages {
        stage('test') {
            steps {
                sh "bash test_basic.sh"
            }
        }
    }
    post {
        always{
            archiveArtifcats: "htmlcov/*"
        }
    }
}