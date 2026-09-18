# Accessing the Mainframe — README

## Description

このプログラムは .env を使った環境変数管理を学ぶためのツールです。
python-dotenv を使って設定を読み込み、development / production の違いを出力します。

📦 Dependencies
python-dotenv==1.0.1

📁 Files
oracle.py

requirements.txt

.env.example

.gitignore（.env を除外するため）

⚙️ Configuration Variables
MATRIX_MODE

DATABASE_URL

API_KEY

LOG_LEVEL

ZION_ENDPOINT

### Usage

設定なしで実行
```
python3 oracle.py
```
→ Missing warnings を表示。

.env を使う場合
```
cp .env.example .env
```
 値を編集
```
python3 oracle.py
```
環境変数で上書き
```
MATRIX_MODE=production
API_KEY=secret123

python3 oracle.py
```
🔐 Security
.env は絶対に Git に含めない

.gitignore に .env を追加

本物の API キーは絶対に書かない