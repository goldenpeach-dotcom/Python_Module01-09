#!/usr/bin/env python3
"""
Validate exported datasets using your Pydantic models.
"""

import json
from pathlib import Path

# あなたのモデル
from ex0.space_station import SpaceStation
from ex1.alien_contact import AlienContact
from ex2.space_crew import SpaceMission


def load_json(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def validate_space_stations(path: Path):
    print("\n=== Validating exported space stations ===")
    data = load_json(path)

    for i, item in enumerate(data, start=1):
        try:
            model = SpaceStation(**item)
            print(f"[OK] Station {i}: {model.station_id}")
        except Exception as e:
            print(f"[ERROR] Station {i}: {e}")


def validate_alien_contacts(path: Path):
    print("\n=== Validating exported alien contacts ===")
    data = load_json(path)

    for i, item in enumerate(data, start=1):
        try:
            model = AlienContact(**item)
            print(f"[OK] Contact {i}: {model.contact_id}")
        except Exception as e:
            print(f"[ERROR] Contact {i}: {e}")


def validate_space_missions(path: Path):
    print("\n=== Validating exported space missions ===")
    data = load_json(path)

    for i, item in enumerate(data, start=1):
        try:
            model = SpaceMission(**item)
            print(f"[OK] Mission {i}: {model.mission_id}")
        except Exception as e:
            print(f"[ERROR] Mission {i}: {e}")


def main():
    base = Path("generated_data")

    validate_space_stations(base / "space_stations.json")
    validate_alien_contacts(base / "alien_contacts.json")
    validate_space_missions(base / "space_missions.json")

    print("\nValidation complete.")


if __name__ == "__main__":
    main()
