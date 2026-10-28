pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    environment {
        IMAGE_NAME = 'devops-mastery-app'
        IMAGE_TAG = "jenkins-${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                sh '''
                    python3 -m venv .jenkins-venv
                    . .jenkins-venv/bin/activate
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                    pip install pytest
                    python -m pytest -v
                '''
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .'
            }
        }

        stage('Verify') {
            steps {
                sh '''
                    docker image inspect ${IMAGE_NAME}:${IMAGE_TAG}
                    echo "Docker image built and verified successfully."
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed. Check the stage logs for details.'
        }
        always {
            echo 'Pipeline execution finished.'
        }
    }
}
