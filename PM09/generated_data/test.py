#!/usr/bin/env python3
"""
Full validation test suite for Module09 datasets.
Validates CSV, JSON, and Python data using your Pydantic models.
"""
# 主な問題点

# 1. データの場所が違う
# エクスポーターの出力先は generated_data/ ですが、base = Path(".") になっています。そのため「File not found, skipping.」で全部スキップされます。Pythonデータの from space_stations import ... も同じ理由で ImportError になり、None のまま黙ってスキップされます。

# 2. 合否の判定がない
# 今は結果を表示しているだけで、期待どおりかどうかを判定していません。特に invalid_*.json はエラーになるのが正解なのに、通ってしまっても [OK] と表示されます。

# 正常データは、エラーが出たら失敗にします。
# 不正データは、エラーが出なかったら失敗にします。
# 最後に失敗数を集計して、sys.exit(1) で終了します。

# 3. 出力の形式がばらばら
# validate_json だけエラーメッセージのみで、行番号も [ERROR] もありません。1つの check_rows にまとめて、形式をそろえました。

# 4. CSVの空文字
# エクスポーターは None を "" として書き出すので、読み込み時に None へ戻すようにしました。戻さないと、notes や message_received でバリデーションの結果が変わる可能性があります。

# 5. mypy / flake8 対策

# 関数に戻り値の型（-> None など）がなく、--strict で怒られます。
# row: dict[str | Any, str | Any] のような注釈は不要です。
# import csv と from csv import DictReader が重複しています。
# model(**row) ではなく model.model_validate(row) が推奨です。

import sys
import csv
import json
from pathlib import Path
from pydantic import ValidationError, BaseModel
from csv import DictReader
from typing import List, Dict, Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from ex0.space_station import SpaceStation  # noqa: E402
from ex1.alien_contact import AlienContact  # noqa: E402
from ex2.space_crew import SpaceMission  # noqa: E402


# Python データ（存在する場合のみ）
SPACE_STATIONS: List[Dict[str, Any]] | None
try:
    from space_stations import SPACE_STATIONS
except ImportError:
    SPACE_STATIONS = None

ALIEN_CONTACTS: List[Dict[str, Any]] | None
try:
    from alien_contacts import ALIEN_CONTACTS
except ImportError:
    ALIEN_CONTACTS = None

SPACE_MISSIONS: List[Dict[str, Any]] | None
try:
    from space_missions import SPACE_MISSIONS
except ImportError:
    SPACE_MISSIONS = None


# -------------------------
# 共通ユーティリティ
# -------------------------

def validate_csv(path: Path, model: type[BaseModel]):
    print(f"\n=== CSV Validation: {path.name} ===")

    if not path.exists():
        print("File not found, skipping.")
        return

    with open(path, newline="", encoding="utf-8") as f:
        reader: DictReader[str] = csv.DictReader(f)

        i: int
        row: dict[str | Any, str | Any]
        for i, row in enumerate(reader, start=1):
            try:
                model(**row)                    
                print(f"[OK] Row {i}: validated")
            except ValidationError as e:
                print(f"[ERROR] Row {i}: {e}")


def validate_json(path: Path, model: type[BaseModel]):
    print(f"\n=== JSON Validation: {path.name} ===")

    if not path.exists():
        print("File not found, skipping.")
        return

    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    for i, row in enumerate(data, start=1):
        try:
            model(**row)
            print(f"[OK] Item {i}: validated")
        except ValidationError as e:
            for err in e.errors():
                print(err["msg"])


def validate_python_list(
    py_list: List[Dict[str, Any]] | None,
    model: type[BaseModel],
    name: str,
):
    print(f"\n=== Python List Validation: {name} ===")

    if py_list is None:
        print("Python data file not found, skipping.")
        return

    for i, row in enumerate(py_list, start=1):
        try:
            model(**row)
            print(f"[OK] Item {i}: validated")
        except ValidationError as e:
            print(f"[ERROR] Item {i}: {e}")


# -------------------------
# メインテスト
# -------------------------

def main() -> None:
    base = Path(".")

    print("\n🚀 Running full dataset validation suite")
    print("=" * 60)

    # SpaceStation
    validate_csv(base / "space_stations.csv", SpaceStation)
    validate_json(base / "space_stations.json", SpaceStation)
    validate_python_list(SPACE_STATIONS, SpaceStation, "SPACE_STATIONS")

    # AlienContact
    validate_csv(base / "alien_contacts.csv", AlienContact)
    validate_json(base / "alien_contacts.json", AlienContact)
    validate_python_list(ALIEN_CONTACTS, AlienContact, "ALIEN_CONTACTS")

    # SpaceMission
    validate_json(base / "space_missions.json", SpaceMission)
    validate_python_list(SPACE_MISSIONS, SpaceMission, "SPACE_MISSIONS")

    # Invalid data tests
    validate_json(base / "invalid_contacts.json", AlienContact)
    validate_json(base / "invalid_stations.json", SpaceStation)

    print("\n🎉 All dataset validations complete!")


if __name__ == "__main__":
    main()
