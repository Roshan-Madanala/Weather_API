pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Roshan-Madanala/Weather_API.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest test_weather_api.py --maxfail=1 --disable-warnings --html=report.html'
            }
        }

        stage('Publish Report') {
            steps {
                publishHTML([
                    reportDir: '.',
                    reportFiles: 'report.html',
                    reportName: 'PyTest Report'
                ])
            }
        }
    }
}
