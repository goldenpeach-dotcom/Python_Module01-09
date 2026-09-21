#!/usr/bin/env python3
"""
Full validation test suite for Module09 datasets.
Validates CSV, JSON, and Python data using your Pydantic models.
"""
import sys
import csv
import json
from pathlib import Path
from pydantic import ValidationError, BaseModel
from csv import DictReader
from typing import Optional, List, Dict, Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from ex0.space_station import SpaceStation  # noqa: E402
from ex1.alien_contact import AlienContact  # noqa: E402
from ex2.space_crew import SpaceMission  # noqa: E402

# Python データ（存在する場合のみ）
SPACE_STATIONS: Optional[List[Dict[str, Any]]]
try:
    from space_stations import SPACE_STATIONS
except ImportError:
    SPACE_STATIONS = None

ALIEN_CONTACTS: Optional[List[Dict[str, Any]]]
try:
    from alien_contacts import ALIEN_CONTACTS
except ImportError:
    ALIEN_CONTACTS = None

SPACE_MISSIONS: Optional[List[Dict[str, Any]]]
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
    py_list: Optional[List[Dict[str, Any]]],
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
