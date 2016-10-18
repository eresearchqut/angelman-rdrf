#!groovy

node {
    env.DOCKER_USE_HUB = 1
    def deployable_branches = ["master", "next_release"]

    stage('Checkout') {
        checkout scm

        // rdrf git submodule clone is over ssh, project checkout above is over https 
        withCredentials([[$class: 'FileBinding', credentialsId: 'ccgbuildbot_gh_ssh', variable: 'SSH_KEY']]) {
            sh('''
                eval `ssh-agent`
                ssh-add $SSH_KEY
                git submodule update --init
            ''')
        }

    }

    stage('Docker dev build') {
        echo "Branch is: ${env.BRANCH_NAME}"
        echo "Build is: ${env.BUILD_NUMBER}"
        wrap([$class: 'AnsiColorBuildWrapper', 'colorMapName': 'XTerm']) {
            sh './develop.sh docker_warm_cache'
            sh './develop.sh dev_build'
            sh './develop.sh check_migrations'
        }
    }

    stage('Unit tests') {
        wrap([$class: 'AnsiColorBuildWrapper', 'colorMapName': 'XTerm']) {
            sh './develop.sh runtests'
        }
        step([$class: 'JUnitResultArchiver', testResults: '**/data/tests/*.xml'])
    }

    stage('Lettuce tests') {
        wrap([$class: 'AnsiColorBuildWrapper', 'colorMapName': 'XTerm']) {
            sh './develop.sh dev_lettuce'
        }
        step([$class: 'JUnitResultArchiver', testResults: '**/data/selenium/*.xml'])
        step([$class: 'ArtifactArchiver', artifacts: '**/data/selenium/*.png', fingerprint: true])
    }

    if (deployable_branches.contains(env.BRANCH_NAME)) {

        stage('Docker prod build') {
            wrap([$class: 'AnsiColorBuildWrapper', 'colorMapName': 'XTerm']) {
                sh './develop.sh prod_build'
            }
        }

        stage('Publish docker image') {
            withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'dockerbot',
                              usernameVariable: 'DOCKER_USERNAME',
                              passwordVariable: 'DOCKER_PASSWORD']]) {
                wrap([$class: 'AnsiColorBuildWrapper', 'colorMapName': 'XTerm']) {
                    sh './develop.sh ci_docker_login'
                    sh './develop.sh publish_docker_image'
                }
            }
        }
    }
}
