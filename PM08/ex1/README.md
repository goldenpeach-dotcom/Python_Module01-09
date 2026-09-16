# Loading Programs — Exercise 1

このプログラムは、pip と Poetry の両方を使用した依存関係管理を実演し、  
pandas / numpy / matplotlib を用いた簡単なデータ分析と可視化を行います。

---

## Description

本プロジェクトでは、外部ライブラリを安全に読み込み、  
依存関係が不足している場合に適切なエラーを表示する「データ分析ツール」を構築します。

### 実装内容

- **pandas**：データ操作  
- **numpy**：行列データの生成（1000点のサンプルデータ）  
- **matplotlib**：可視化（PNG画像の生成）  
- **requests**：任意（外部 API からデータ取得する場合のみ）

### アルゴリズム概要

1. 依存関係チェック  
   - `importlib.import_module()` を使用し、各ライブラリの存在とバージョンを確認  
   - 不足している場合は pip / Poetry のインストール手順を表示

2. データ生成  
   - `numpy.random.randn(1000)` により行列データをシミュレート  
   - ハードコーディングされたリストや `range()` は禁止（PDF要件）

3. データ分析  
   - pandas の `DataFrame` と `describe()` を使用して統計情報を生成

4. 可視化  
   - matplotlib により折れ線グラフを描画  
   - `matrix_analysis.png` として保存

### 設計の正当化

- **依存関係管理の比較を明確に示すため**、pip と Poetry の両方に対応  
- **例外処理を導入し、環境による動作の違いを明確化**  
- **numpy を唯一のデータソースとすることで、要件の「シミュレーション」を厳密に遵守**

---

## Instruction

### 実行方法

#### 依存関係なしで実行（Missing を確認）

```bash
python3 loading.py
```

#### pipをインストールする

```bash
pip install -r requirements.txt
python3 loading.py

```

#### Poettryをインストールする

```bash
poetry install
poetry run python3 loading.py

```

### 出力例

LOADING STATUS: Loading programs...
Checking dependencies:
[OK] pandas (2.1.0)
[OK] numpy (1.25.0)
[OK] matplotlib (3.7.2)
Analyzing Matrix data...
Processing 1000 data points...
Generating visualization...
Analysis complete!
Results saved to: matrix_analysis.png

## Resources
pandas documentation

numpy documentation

matplotlib documentation

Python importlib — module loading

pip / Poetry — dependency management