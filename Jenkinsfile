pipeline{
    agent any
    stages{
        stage("SCM Checkout"){
            steps{
                git branch: 'main', url: 'https://github.com/Nag5115/assignment'
            }
        }
        stage("Script Execution"){
            steps{
                sh "python word-char-task.py"
            }
        }
        stage("Display of Output"){
            steps{
                sh "cat word-char-count-descend.txt"
            }
        }
        stage("Storing the Output back to repo"){
            steps{
                script {
                    catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE'){
                        withCredentials([usernamePassword(credentialsId: 'user_id')]){
                            sh "git rm --cached word-char-count-descend.txt"
							sh "git add word-char-count-descend.txt"
                            sh "git commit -m 'Updating Output back to repo'"
                            sh "git push"
                        }
                    }
                }
            }
        }
    }
}
