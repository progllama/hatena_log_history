# Table of Content
- [環境の作成](#環境の作成)
- [環境の削除](#環境の削除)
- [環境の有効化](#環境の有効化)
- [環境の無効化](#環境の無効化)
- [パッケージのインストール](#パッケージのインストール)
- [パッケージのアンインストール](#パッケージのアンインストール)
- [依存ライブラリを出力](#依存ライブラリを出力)
- [依存ライブラリのインストール](#依存ライブラリのインストール)
- [etc](#etc)

# 環境の作成

```python3 -m venv 環境名```

ex.
```python3 -m venv env```

環境名はenvがスタンダード。

# 環境の削除
```rm -rf 環境名```
.ex
```rm -rf env```

# 環境の有効化
```source 環境名/bin/activate```

ex.
```source env/bin/activate```

# 環境の無効化
```deactivate```

# パッケージのインストール
```pip install パッケージ```
```pip install requests```

# パッケージのアンインストール
```pip uninstall パッケージ```
```pip uninstall requests```

# 依存ライブラリを出力
```pip freeze > requirements.txt```

# 依存ライブラリのインストール
```pip install -r requirements.txt```

# etc
gitでは作った環境はgitignoreで無視してrequirements.txtで管理する