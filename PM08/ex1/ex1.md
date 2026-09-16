＜numpy＞
高速な数値計算をするためのライブラリ

Python のリストより 100倍以上高速

行列（Matrix）やベクトル（Vector）を扱うための基本ツール

PM08 の「Matrix データ生成」は numpy.random.randn() を使う

C言語で実装されているので高速

多次元配列（ndarray）を扱える

線形代数、統計、乱数生成が強い

pandas や matplotlib の 土台になっている
numpy公式ドキュメント
https://numpy.org/doc/

＜pandas＞
表形式データ（Excelみたいなもの）を扱うライブラリ

行と列を持つ DataFrame が中心

データ分析の世界では「必須スキル」

CSV / Excel / SQL などのデータを簡単に扱える

統計情報を一瞬で出せる（df.describe()）

行列のフィルタリング、集計、結合が簡単

numpy と完全連携している

✔ PM08 で使う機能
pd.DataFrame({"values": data})  
→ numpy の配列を表形式に変換

df.describe()  
→ 平均、標準偏差、最小値、最大値などを自動計算

公式ドキュメント
https://pandas.pydata.org/docs/

＜matplotlib＞
✔ 何をするライブラリ？
グラフを描くためのライブラリ

折れ線グラフ、棒グラフ、散布図など何でも描ける

pandas と組み合わせると最強

Python の標準的な可視化ツール

PNG や PDF に保存できる

pandas の df.plot() が内部で matplotlib を使う

✔ PM08 で使う機能
df["values"].plot(kind="line")  
→ 折れ線グラフを描く

fig.savefig("matrix_analysis.png")  
→ PNG ファイルとして保存
公式ドキュメント
https://matplotlib.org/stable/

🍀 4. requests（リクエスツ） — HTTP 通信ライブラリ
✔ 何をするライブラリ？
Web API にアクセスするためのライブラリ

HTTP GET / POST を簡単に送れる

JSON データを取得するのに便利

✔ 何がすごい？
Python で最も使われている HTTP クライアント

エラー処理が簡単

外部データを取得するのに必須

✔ PM08 で使う機能
ex1 では 必須ではない

「外部 API からデータを取得する場合のみ使ってよい」と PDFに書いてある（）

✔ 公式ドキュメント
https://requests.readthedocs.io/en/latest/

| ライブラリ | 役割 | PM08で使う機能 |
| --- | --- | --- |
| **numpy** | 数値計算・行列生成 | ``random.randn()`` |
| **pandas** | データ分析・表形式データ | ``DataFrame``, ``describe()`` |
| **matplotlib** | グラフ描画 | ``plot()``, ``savefig()`` |
| **requests** | Web APIアクセス | 必須ではない |