"""
Dataset validation test suite for Module 09.

- Valid datasets (CSV / JSON / Python) must pass the models.
- Invalid datasets and custom edge cases must be rejected.
- Exits with status 1 if any result is unexpected.
"""
import copy
import csv
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any

from pydantic import BaseModel, ValidationError

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
DATA_DIR = ROOT / "generated_data"  # where the exporter wrote its files

from ex0.space_station import SpaceStation  # noqa: E402
from ex1.alien_contact import AlienContact  # noqa: E402
from ex2.space_crew import SpaceMission  # noqa: E402

Rows = list[dict[str, Any]]


# -------------------------
# Loaders
# -------------------------

def load_json(path: Path) -> Rows | None:
    if not path.exists():
        return None
    with open(path, encoding="utf-8") as f:
        data: Rows = json.load(f)
    return data


def load_csv(path: Path) -> Rows | None:
    if not path.exists():
        return None
    with open(path, newline="", encoding="utf-8") as f:
        # The exporter writes None as "", so convert it back.
        return [
            {k: (v if v != "" else None) for k, v in row.items()}
            for row in csv.DictReader(f)
        ]


def load_python(path: Path, var_name: str) -> Rows | None:
    if not path.exists():
        return None
    spec = importlib.util.spec_from_file_location(path.stem, path)
    if spec is None or spec.loader is None:
        return None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    data: Rows = getattr(module, var_name)
    return data


# -------------------------
# Core check
# -------------------------

def check_rows(
    label: str,
    rows: Rows | None,
    model: type[BaseModel],
    expect_valid: bool,
) -> int:
    """Validate every row. Return the number of unexpected results."""
    kind = "valid" if expect_valid else "invalid"
    print(f"\n=== {label} (expect {kind}) ===")

    if rows is None:
        print("[MISSING] data not found")
        return 1

    failures = 0
    for i, row in enumerate(rows, start=1):
        try:
            model.model_validate(row)
        except ValidationError as e:
            if expect_valid:
                failures += 1
                print(f"[FAIL] Row {i}: unexpected error")
            else:
                print(f"[OK]   Row {i}: rejected as expected")
            for err in e.errors():
                print(f"         {err['loc']}: {err['msg']}")
        else:
            if expect_valid:
                print(f"[OK]   Row {i}: validated")
            else:
                failures += 1
                print(f"[FAIL] Row {i}: should have been rejected")
    return failures


# -------------------------
# Custom edge cases (adjust to the subject's rules)
# -------------------------

def station_cases(base: dict[str, Any]) -> Rows:
    cases = []
    for changes in (
        {"crew_size": 0},
        {"crew_size": 21},
        {"oxygen_level": 150.0},
        {"power_level": -1.0},
        {"station_id": "TS"},
        {"name": ""},
    ):
        rec = copy.deepcopy(base)
        rec.update(changes)
        cases.append(rec)
    return cases


def contact_cases(base: dict[str, Any]) -> Rows:
    cases = []
    for changes in (
        {"contact_id": "XX_2024_001"},
        {"signal_strength": 11.0},
        {"contact_type": "telepathic", "witness_count": 1},
        {"contact_type": "physical", "is_verified": False},
    ):
        rec = copy.deepcopy(base)
        rec.update(changes)
        cases.append(rec)
    return cases


def mission_cases(base: dict[str, Any]) -> Rows:
    no_commander = copy.deepcopy(base)
    for member in no_commander["crew"]:
        member["rank"] = "cadet"

    inactive = copy.deepcopy(base)
    inactive["crew"][0]["is_active"] = False

    long_inexperienced = copy.deepcopy(base)
    long_inexperienced["duration_days"] = 500
    for member in long_inexperienced["crew"]:
        member["years_experience"] = 0
    long_inexperienced["crew"][0]["rank"] = "captain"

    bad_id = copy.deepcopy(base)
    bad_id["mission_id"] = "X2024_MARS"

    return [no_commander, inactive, long_inexperienced, bad_id]


def run_edge_cases(
    label: str,
    valid_rows: Rows | None,
    builder: Any,
    model: type[BaseModel],
) -> int:
    if not valid_rows:
        print(f"\n=== {label} ===\n[MISSING] no base record available")
        return 1
    return check_rows(label, builder(valid_rows[0]), model, False)


# -------------------------
# Main
# -------------------------

def main() -> int:
    failures = 0
    print("\n=== Running full dataset validation suite ===")
    print("=" * 60)

    stations_json = load_json(DATA_DIR / "space_stations.json")
    contacts_json = load_json(DATA_DIR / "alien_contacts.json")
    missions_json = load_json(DATA_DIR / "space_missions.json")

    # --- Valid data ---
    sources: list[tuple[str, Rows | None, type[BaseModel]]] = [
        ("Stations CSV", load_csv(DATA_DIR / "space_stations.csv"),
         SpaceStation),
        ("Stations JSON", stations_json, SpaceStation),
        ("Stations Python",
         load_python(DATA_DIR / "space_stations.py", "SPACE_STATIONS"),
         SpaceStation),
        ("Contacts CSV", load_csv(DATA_DIR / "alien_contacts.csv"),
         AlienContact),
        ("Contacts JSON", contacts_json, AlienContact),
        ("Contacts Python",
         load_python(DATA_DIR / "alien_contacts.py", "ALIEN_CONTACTS"),
         AlienContact),
        ("Missions JSON", missions_json, SpaceMission),
        ("Missions Python",
         load_python(DATA_DIR / "space_missions.py", "SPACE_MISSIONS"),
         SpaceMission),
    ]
    for label, rows, model in sources:
        failures += check_rows(label, rows, model, True)

    # --- Invalid data provided by the school ---
    failures += check_rows(
        "invalid_stations.json",
        load_json(DATA_DIR / "invalid_stations.json"),
        SpaceStation,
        False,
    )
    failures += check_rows(
        "invalid_contacts.json",
        load_json(DATA_DIR / "invalid_contacts.json"),
        AlienContact,
        False,
    )

    # --- Our own edge cases ---
    failures += run_edge_cases(
        "Custom station cases", stations_json, station_cases, SpaceStation)
    failures += run_edge_cases(
        "Custom contact cases", contacts_json, contact_cases, AlienContact)
    failures += run_edge_cases(
        "Custom mission cases", missions_json, mission_cases, SpaceMission)

    print("\n" + "=" * 60)
    if failures:
        print(f"{failures} unexpected result(s)")
    else:
        print("All results as expected!")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
