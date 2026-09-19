#!/usr/bin/env python3
"""
Test loader for Module09 models.
Loads data from data_generator.py and validates using your Pydantic models.
"""

from datetime import datetime
from data_generator import (
    DataConfig,
    SpaceStationGenerator,
    AlienContactGenerator,
    CrewMissionGenerator,
)

# あなたのモデルを import
from ex0.space_station import SpaceStation
from ex1.alien_contact import AlienContact
from ex2.space_crew import SpaceMission


def test_space_stations():
    print("\n=== Testing SpaceStation ===")
    config = DataConfig()
    gen = SpaceStationGenerator(config)
    stations = gen.generate_station_data(5)

    for i, st in enumerate(stations, start=1):
        try:
            model = SpaceStation(**st)
            print(f"[OK] Station {i}: {model.station_id} validated")
        except Exception as e:
            print(f"[ERROR] Station {i}: Validation failed → {e}")


def test_alien_contacts():
    print("\n=== Testing AlienContact ===")
    config = DataConfig()
    gen = AlienContactGenerator(config)
    contacts = gen.generate_contact_data(8)

    for i, ct in enumerate(contacts, start=1):
        try:
            model = AlienContact(**ct)
            print(f"[OK] Contact {i}: {model.contact_id} validated")
        except Exception as e:
            print(f"[ERROR] Contact {i}: Validation failed → {e}")


def test_space_missions():
    print("\n=== Testing SpaceMission ===")
    config = DataConfig()
    gen = CrewMissionGenerator(config)
    missions = gen.generate_mission_data(3)

    for i, ms in enumerate(missions, start=1):
        try:
            model = SpaceMission(**ms)
            print(f"[OK] Mission {i}: {model.mission_id} validated")
        except Exception as e:
            print(f"[ERROR] Mission {i}: Validation failed → {e}")


def main():
    print("🚀 Module09 Model Validation Test")
    print("=" * 50)

    test_space_stations()
    test_alien_contacts()
    test_space_missions()

    print("\nAll tests complete.")


if __name__ == "__main__":
    main()
