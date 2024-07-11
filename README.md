# db-cli
db-cli

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

## AWS Cli 설치 필요
* `aws configure sso` 를 통한 로그인 필요
* 이후 `--profile` 인자를 settings.py `AWS_PROFILE`에 세팅 필요함.
* aws cli 로그인은 아래 링크 참조
https://www.notion.so/mdbtech/AWS-cli-66da9526c2d34007aeea4a8d8f6dbe97?pvs=4

## 주의사항
* git repo 명칭과 commit id 기반으로 동작하며, 현재 실행된 디렉터리의 git 정보를 기반으로 동작함.
* container 의 명칭과 작업 대상인 git repo 이 일치를 검증하지 않음.
