## 接続情報

### django
| 名前 | 値               |
| ---- | ---------------- |
| URL  | http://localhost |

### Postgres
| 名前     | 値            |
| -------- | ------------- |
| Hostname | postgres      |
| User     | postgres_user | 
| Pass     | postgres_pass |
| 初期DB   | postgres      | 

### pgAdmin
| 名前     | 値                    |
| -------- | --------------------- |
| URL      | http://localhost:8000 |
| Hostname | pgadmin4              |
| User     | pgadmin_user          | 
| Pass     | pgadmin_pass          |



## コマンド(ホスト側)

docker-compose build
    Dockerfileよりイメージを生成する、Dockerfileに変更を反映させる場合は再ビルドする必要がある
    オプションで「--no-cache」を付けると、前のキャッシュを使わずにビルドする

docker-compose up -d
    イメージよりコンテナを生成 & 起動、オプションで「-d」を付けることでバックグラウンドで実行
    バックグラウンドで起動しないと、コンテナを終了するまでpoweshellで他のコマンドが入力できなくなる
    オプションで「--build」を付けるとbuildも行う

docker-compose ps
    起動中のコンテナ一覧が表示される、状態確認に使う

docker-compose exec サービス名 bash
    コンテナの中に入る、サービス名は「docker-compose.yml」に記述した名前

docker-compose down
    イメージ、コンテナ、ボリューム、ネットワーク削除

docker-compose stop
    コンテナ停止

docker-compose down --rmi all --volumes --remove-orphans
    スーパー全削除

docker-compose logs サービス名
    コンテナのログが表示される、サービスを付けない場合、全コンテナのログが表示


## Django
* mysite直下のディレクトリで触るファイルアは二つだけ
    settings.py
        全体設定ファイル
    urls.py
        URLの設定ファイル

* プロジェクトにはアプリが最低1つ必要
    manage.pyがあるディレクトリで「python3 manage.py startapp アプリ名」
    アプリを作るとsettings.pyに登録する必要がある
