# 目次
- [script](#script)
- [.env](#.env)
- [apiキーの取得](#apiキーの取得)
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

# リポジトリ

[https://github.com/progllama/hatena_log_history:embed:cite]