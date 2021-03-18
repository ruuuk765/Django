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
    down前にdocker-compose.ymlファイルを編集した場合、以前のコンテナが残る。「--remove-orphans」はそれも削除する

docker-compose logs サービス名
    コンテナのログが表示される、サービスを付けない場合、全コンテナのログが表示
    VSCodeのDockerの拡張機能をインストールすると、コンテナ右クリック→「View Logs」で見れる
    「logs -f」を付けるとリアルタイムでログが表示される(followの略)

## Django
* mysite直下のディレクトリで触るファイルアは二つだけ
    * settings.py
        * 全体設定ファイル
    * urls.py
        * URLの設定ファイル

* プロジェクトにはアプリが最低1つ必要
    * manage.pyがあるディレクトリで「python3 manage.py startapp アプリ名」
    * アプリを作るとsettings.pyに登録する必要がある

## .gitignore反映されない
$ git rm -r --cached . //ファイル全体キャッシュ削除

## MEMO
* FTPサーバーもDockerで作れる、用途は今のところ思いつかない
* docker-compose stop は個別にコンテナを止めるときに使う
    * 共有コンテナでpostgresとmysqlがあるが、mysqlは使わないなどのときstop
* ファイル共有は今だ謎、COPYもMKDIRもできるらしいが要検証
* restartもttyもコンテナが予期せず停止しないようなおまじない
* depends_on は書かないと環境変数(id、passの設定)ができない？おまじない