# db-cli
Github repo 및 commit id 기반으로 AWS S3 로의 DB 백업/복원을 지원하는 CLI 이며,
개발용으로 데이터를 채운 DB 를 백업하거나 공유하는 것을 목적으로 개발함.

**Cookie cutter Django 의 local(dev)환경, Postgresql Docker 를 기준으로 동작함.**


## Prerequisite
* python >= 3.8
* aws cli
  * https://docs.aws.amazon.com/ko_kr/cli/latest/userguide/getting-started-install.html

## Installation
1. clone and register
```shell
git clone git@github.com:MDB-Inc/db-cli.git
db-cli/install.sh 
```
No further python package installation is required.

2. aws cli login
    * https://www.notion.so/mdbtech/AWS-cli-66da9526c2d34007aeea4a8d8f6dbe97?pvs=4
```shell
aws configure sso
```

3. settings.py
```python
AWS_PROFILE = "YourRole-123456789012"
BUCKET_NAME = "s3-bucket-name"
```
done!

## Usage
### push (local DB > S3)
`db push <db_container> [id (default: git_commit_id)] [options]`

* `db push <db_container>`
```shell
db push v3_postgres
```
  
* `db push <db_container>` equivalent to `db push <db_container> <git_commit_id>`
```shell
db push v3_postgres 12345678f23b688454f4a8a71e4d085b551e8943
```

* `db push <db_container> <custom_id>`
```shell
db push v3_postgres myfooid
```

### pull (S3 > local DB)
`db pull <db_container> [id (default: git_commit_id)] [options]`

* `db pull <db_container>`
```shell
db pull v3_postgres
```
  
* `db pull <db_container>` equivalent to `db pull <db_container> <git_commit_id>`
```shell
db pull v3_postgres 12345678f23b688454f4a8a71e4d085b551e8943
```

* `db pull <db_container> <custom_id>`
```shell
db pull v3_postgres myfooid
```

* `db pull <db_container> --latest` if you don't know the commit id and want to pull the latest backup
```shell
db pull v3_postgres --latest
```

## 주의사항
* git repo 명칭과 commit id 기반으로 동작하며, 현재 실행된 디렉터리의 git 정보를 기반으로 동작함.
* container 의 명칭과 작업 대상인 git repo 이 일치를 검증하지 않음.
