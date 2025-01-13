---
title:  "좌표변환 - ci/cd 구축"
layout: single
categories:
  - sideproject
tags:
  - ci/cd
  - codeDeploy
  - aws
---


## 환경
### aws
- ec2 ubuntu 온프레미스
- s3
- CodeDeploy

## 간략한 배포과정
1. git push 및 pull requests 시 gitAction 트리거 실행
2. build된 소스 코드를 zip파일로 묶어 s3에 업로드
3. CodeDeploy에 의해 압축해제와 `appspec.yml` 설정된 명령 실행


## 상세과정
### 1. iam 계정 생성
![createIam1](https://github.com/user-attachments/assets/4613c3f6-706c-43c9-827e-894b59a0ef29)

![createIam2](https://github.com/user-attachments/assets/039b3127-0b72-496d-8ef5-bdb5e0c686ff)

아래 권한 추가한다.

- AmazonEC2FullAccess
- AmazonS3FullAccess
- AWSCodeDeployDeployerAccess
- AWSCodeDeployFullAccess
- AWSCodeDeployRole
- EC2InstanceConnect

![addAuth](https://github.com/user-attachments/assets/18a4f210-1864-475a-9db6-0258292fec1e)

추가로 CodeDeploy에서 사용할 역활을 추가한다.

![codedeploy](https://github.com/user-attachments/assets/bc3131f9-9444-433b-b270-fb6b7eac701d)


### 2. ec2, s3 생성
ec2와 s3를 만드는 방법은 다른 블로그를 확인하기를 바란다.

### 3. CodeDeploy 생성

서비스 역활을 위의 s3deploymet의 ARN으로 지정한다.

추가적으로 ec2의 태그 설정을 통해 완성한다.

![CodeDeploy](https://github.com/user-attachments/assets/232e2730-7a97-474d-ba9d-276fa543748c)



### 4. ec2 CodeDeploy Agent 설치
설치 관련 공식문서를 보고 따라하자

https://docs.aws.amazon.com/ko_kr/codedeploy/latest/userguide/codedeploy-agent-operations-install-ubuntu.html

이와 같이 `active` 되어 있다면 성공이다.

![ec2CodeDeployAgent](https://github.com/user-attachments/assets/6ebc6d9f-cd36-40eb-89e1-f4e556c5ec55)


### 5. gitAction 설정
- gitAction `.yml`파일을 생성한다.
- aws에서 iam 사용자에서 엑세스 키를 만들어 github에 연동한다.

![awsAccessTokenSetting](https://github.com/user-attachments/assets/ec0eb967-1ced-48ff-80c6-949f546f302a)

```yml
name: deployment-project

on:
  pull_request:
    branches: [ "main" ]
# bucket region 설정
env:
  AWS_REGION: ap-northeast-2
  S3_BUCKET_NAME: excel-bucket-s3
  CODE_DEPLOY_APPLICATION_NAME: excel-deploy
  CODE_DEPLOY_DEPLOYMENT_GROUP_NAME: excel-deploy-group

jobs:
  deploy:
    name: Deploy
    runs-on: ubuntu-latest 
    environment: production

    steps:
    # (1) 기본 체크아웃
    - name: Checkout
      uses: actions/checkout@v3

    # (2) JDK 17 세팅
    - name: Set up JDK 17
      uses: actions/setup-java@v4.6.0
      with:
        distribution: 'temurin'
        java-version: '17'
    # (3) gradle permission and build
    - name: Setup Gradle
      uses: gradle/actions/setup-gradle@v3
    - name: Grant execute permission for gradlew
      run: chmod +x gradlew
    - name: Build with Gradle Wrapper
      run: ./gradlew clean build -x test


    # (4) AWS 인증 (IAM 사용자 Access Key, Secret Key 활용)
    - name: Configure AWS credentials
      uses: aws-actions/configure-aws-credentials@v1
      with:
        aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
        aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        aws-region: ${{ env.AWS_REGION }}

    # (5) 빌드 결과물을 S3 버킷에 업로드
    - name: Upload to AWS S3
      run: |
        aws deploy push \
          --application-name ${{ env.CODE_DEPLOY_APPLICATION_NAME }} \
          --ignore-hidden-files \
          --s3-location s3://$S3_BUCKET_NAME/$GITHUB_SHA.zip \
          --source .
    # (6) S3 버킷에 있는 파일을 대상으로 CodeDeploy 실행
    - name: Deploy to AWS EC2 from S3
      run: |
        aws deploy create-deployment \
          --application-name ${{ env.CODE_DEPLOY_APPLICATION_NAME }} \
          --deployment-config-name CodeDeployDefault.AllAtOnce \
          --deployment-group-name ${{ env.CODE_DEPLOY_DEPLOYMENT_GROUP_NAME }} \
          --s3-location bucket=$S3_BUCKET_NAME,key=$GITHUB_SHA.zip,bundleType=zip
```

### 6. appspec.yml, start.sh, stop.sh 작성
### appspec.yml
```yml
version: 0.0
os: linux
files:
  - source: /
    destination: /home/ubuntu/build
    overwrite: yes

permissions:
  - object: /
    pattern: "**"
    owner: ubuntu
    group: ubuntu
hooks:
  AfterInstall:
    - location: script/stop.sh
      timeout: 60
      runas: root
  ApplicationStart:
    - location: script/start.sh
      timeout: 60
      runas: root
```

### start.sh
```shell
#!/bin/bash

ROOT_DIRECTORY=/home/ubuntu/build

APP_NAME=consumer-*.*.*-SNAPSHOT
JAR_NAME=$(ls $ROOT_DIRECTORY/build/libs/ | grep '.jar' | tail -n 1)
JAR_PATH=$ROOT_DIRECTORY/build/libs/$JAR_NAME

CURRENT_PID=$(pgrep consumer)

if [ -z "$CURRENT_PID" ]; then
    echo "NOT RUNNING"
else
    echo "> kill -9 $CURRENT_PID"
    kill -15 $CURRENT_PID
    sleep 5
fi

echo "> $JAR_PATH 에 실행권한 추가"
chmod +x $JAR_PATH

echo "> $JAR_PATH 배포"
nohup java -jar -Duser.timezone=Asia/Seoul $JAR_PATH 1>/dev/null 2>&1 &
```

### stop.sh
```shell
#!/bin/bash

CURRENT_PID=$(pgrep consumer)

if [ -z $CURRENT_PID ]; then
        echo "no started"
else
        kill -9 $CURRENT_PID
fi
```


## 결과확인

### gitAction
![gitActionSuccess](https://github.com/user-attachments/assets/c0ef2fe4-e0e0-4842-888b-c970181cd52a)


### CodeDeploy
![CodeDeploySucess](https://github.com/user-attachments/assets/6d166e71-0332-4ee6-81f7-f0a6a8798277)

### CodeDeploy Log확인

```shell
# script 실행 echo 로그
$ cd /opt/codedeploy-agent/deployment-root/deployment-logs
$ vi codedeploy-agent-deployments.log

# CodeDeploy 실행 로그
$ cd /var/log/aws/codedeploy-agent
$ vi codedeploy-agent.log
```