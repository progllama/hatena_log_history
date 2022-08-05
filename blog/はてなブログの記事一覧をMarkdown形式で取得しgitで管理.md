# 目次
- [script](#script)
- [.env](#.env)
- [apiキーの取得](#apiキーの取得)
- [github actionを使って自動化](#githubactionを使って自動化)
- [リポジトリ](#リポジトリ)

# script
```hatena_client.py
import os
import requests
import xmltodict as XTD
from dotenv import load_dotenv

# .envの読み込み
load_dotenv()

# .envに記載してある設定の読み込み
HATENA_ID = os.environ.get("HATENA_ID")
PASSWORD = os.environ.get("PASSWORD")
BLOG_ID = os.environ.get("BLOG_ID")

# urlの定義
url = f"https://blog.hatena.ne.jp/{HATENA_ID}/{BLOG_ID}/atom/entry"

# リクエストの送信
response = requests.get(url, auth=(HATENA_ID, PASSWORD))

# response.textでボディが取得できるので、それをxmlからdictに変換するライブラリでdictに変換
xml = XTD.parse(response.text)

# dictをイテレートし必要な情報を取得し書き込む
for entry in xml["feed"]["entry"]:
    title = entry["title"].replace(" ", "")
    fname = "blog/" + title +".md"
    with open(fname, "w") as f:
        f.write(entry["content"]["#text"])
```

# .env
```
HATENA_ID=good-yuuta
PASSWORD=abcdefg12345
BLOG_ID=good-yuuta.hatenablog.com
```

# apiキーの取得

まずhttps://blog.hatena.ne.jp/my/config/detailに行く
APIキーという項目があるのでそこからアカウント設定に移動
そこでもAPIキーという項目があるのでそこから作る。
再度同じページに行くとAPIキーが表示されるのでそれを利用する。

# githubactionを使って自動化
```
name: Backup article
on:
  schedule:
    - cron: "0 0 * * *"
  push:

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python: ["3.10"]

    steps:
      - uses: actions/checkout@v2
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python }}
      - name: get backup
        run: |
          python -m pip install -r requirements.txt
          python hatena_client.py
        env:
          HATENA_ID: ${{ secrets.HATENA_ID }}
          PASSWORD: ${{ secrets.PASSWORD }}
          BLOG_ID: ${{ secrets.BLOG_ID }}
      - name: Commit files
        run: |
          git config --local user.email "progllama.rust@gmail.com"
          git config --local user.name "llama"
          git add .
          git commit -m "Add changes" -a
          git push
```
python環境のセットアップは[こちら](https://docs.github.com/ja/actions/automating-builds-and-tests/building-and-testing-python)を参考

[秘密情報の設定](https://good-yuuta.hatenablog.com/entry/2022/08/04/235543?_ga=2.194778541.1259619272.1659535935-1524494941.1630950902)

現時点の課題は変更がない場合にステータスがエラーになってしまうこと。

# リポジトリ

[https://github.com/progllama/hatena_log_history:embed:cite]