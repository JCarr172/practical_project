pipeline{
        agent any
        environment {
            app_version = 'v1'
            rollback = 'false'
            TEST_DATABASE_URI = credentials('TEST_DATABASE_URI')
            TEST_SECRET = credentials('TEST_SECRET')
            DATABASE_URI = credentials('DATABASE_URI')
            SECRET = credentials('SECRET')
            DOCKER_USER = credentials('DOCKER_USR')
            DOCKER_PSWD = credentials('DOCKER_PSWD')
            }
        stages{
            stage('Run pytest'){
                steps{
                    script{
                            sh 'bash scripts/testing.sh'
                            }
                        }
                    }
            stage('Build and Push'){
                steps{
                    script{
                            sh 'bash scripts/build-push.sh'
                            }
                        }
                    }
            stage('Ansible Configuration'){
                steps{
                    script{
                            sh 'bash scripts/install-ansible.sh'
                            }
                        }
                    }
            stage('Install docker and set up swarm'){
                steps{
                    script{
                            sh 'ansible-playbook -i inventory.yaml playbook.yaml'
                            }
                        }
                    }
        }
}