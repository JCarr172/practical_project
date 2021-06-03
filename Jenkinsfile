pipeline{
        agent any
        environment {
            app_version = 'v1'
            rollback = 'false'
            TEST_DATABASE_URI = credentials('TEST_DATABASE_URI')
            TEST_SECRET = credentials('TEST_SECRET')
            DOCKER_LOGIN = credentials('docker-hub-credentials')
            }
        stages{
            stage('Run pytest'){
                steps{
                    script{
                            sh 'bash scripts/testing.sh'
                            }
                        }
                    }
        }
        stages{
            stage('Build and Push'){
                steps{
                    script{
                            sh 'bash scripts/build-push.sh'
                            }
                        }
                    }
        }
        stages{
            stage('Ansible Configuration'){
                steps{
                    script{
                            sh 'bash scripts/install-ansible.sh'
                            }
                        }
                    }
        }
        stages{
            stage('Install docker and set up swarm'){
                steps{
                    script{
                            sh 'ansible-playbook -i inventory.yaml playbook.yaml'
                            }
                        }
                    }
        }
}