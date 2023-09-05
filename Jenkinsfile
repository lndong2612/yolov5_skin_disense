pipeline {
    agent any
    stages {
        stage('Init') {
            steps {
                echo 'Testing..'
                telegramSend(message: 'Building job: $PROJECT_NAME ... - Link: $BUILD_URL', chatId: -740504133)
            }
        }
        stage ('Deployments') {
            steps {
                echo 'Deploying to Production environment...'
                echo 'Copy project over SSH...'
                sshPublisher(publishers: [
                    sshPublisherDesc(
                        configName: 'swarm1',
                        transfers:
                            [sshTransfer(
                                cleanRemote: false,
                                excludes: '',
                                execCommand: "docker build -t registry.thinklabs.com.vn:5000/tclinicAiApi ./thinklabsdev/tclinicAiApiCI/ \
                                    && docker image push registry.thinklabs.com.vn:5000/tclinicAiApi \
                                    && docker service rm tclinicAi_api || true \
                                    && docker stack deploy -c ./thinklabsdev/tclinicAiApiCI/docker-compose.yml tclinicAi \
                                    && rm -rf ./thinklabsdev/tclinicAiApiCIB \
                                    && mv ./thinklabsdev/tclinicAiApiCI/ ./thinklabsdev/tclinicAiApiCIB",
                                execTimeout: 1800000,
                                flatten: false,
                                makeEmptyDirs: false,
                                noDefaultExcludes: false,
                                patternSeparator: '[, ]+',
                                remoteDirectory: './thinklabsdev/tclinicAiApiCI',
                                remoteDirectorySDF: false,
                                removePrefix: '',
                                sourceFiles: '*, classify/, data/, models/, segment/, utils/'
                            )],
                        usePromotionTimestamp: false,
                        useWorkspaceInPromotion: false,
                        verbose: false
                    )
                ])
                telegramSend(message: 'Building job: $PROJECT_NAME ... - Link: $BUILD_URL', chatId: -740504133)
            }
        }
    }
}
