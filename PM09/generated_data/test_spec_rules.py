"""
Spec-driven boundary tests for Module 09.

For every constraint in the subject, check:
  - the boundary value itself is ACCEPTED
  - one step beyond the boundary is REJECTED
For every business rule, check one accepted and one rejected case.
The rejection reasons (field + message) are printed so you can verify
that each case fails for the INTENDED reason.
"""
import sys
from pathlib import Path
from typing import Any

from pydantic import BaseModel, ValidationError

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from ex0.space_station import SpaceStation  # noqa: E402
from ex1.alien_contact import AlienContact  # noqa: E402
from ex2.space_crew import SpaceMission  # noqa: E402

Rec = dict[str, Any]
Case = tuple[str, Rec]  # (label, fields to override in the base record)


# -------------------------
# Base records (all valid)
# -------------------------

BASE_STATION: Rec = {
    "station_id": "ISS001",
    "name": "Test Station",
    "crew_size": 5,
    "power_level": 80.0,
    "oxygen_level": 95.0,
    "last_maintenance": "2024-01-15T10:30:00",
    "is_operational": True,
    "notes": None,
}

BASE_CONTACT: Rec = {
    "contact_id": "AC_2024_001",
    "timestamp": "2024-01-15T14:30:00",
    "location": "Area 51, Nevada",
    "contact_type": "radio",
    "signal_strength": 5.0,
    "duration_minutes": 45,
    "witness_count": 5,
    "message_received": None,
    "is_verified": False,
}


def member(**kw: Any) -> Rec:
    rec: Rec = {
        "member_id": "CM001",
        "name": "Sarah Connor",
        "rank": "captain",
        "age": 40,
        "specialization": "Navigation",
        "years_experience": 10,
        "is_active": True,
    }
    rec.update(kw)
    return rec


def crew_of(n: int, experienced: int | None = None) -> list[Rec]:
    """First member is a captain. `experienced` = how many have 5+ years."""
    if experienced is None:
        experienced = n
    return [
        member(
            member_id=f"CM{i:03d}",
            rank="captain" if i == 0 else "officer",
            years_experience=10 if i < experienced else 0,
        )
        for i in range(n)
    ]


BASE_MISSION: Rec = {
    "mission_id": "M2024_MARS",
    "mission_name": "Mars Research Mission",
    "destination": "Mars",
    "launch_date": "2024-03-01T00:00:00",
    "duration_days": 100,
    "crew": crew_of(3),
    "mission_status": "planned",
    "budget_millions": 1000.0,
}


# -------------------------
# Runner
# -------------------------

def show(e: ValidationError) -> None:
    for err in e.errors():
        print(f"         -> {err['loc']}: {err['msg']}")


def run_group(
    title: str,
    model: type[BaseModel],
    base: Rec,
    valid: list[Case],
    invalid: list[Case],
) -> int:
    print(f"\n=== {title} ===")
    fails = 0
    for label, changes in valid:
        try:
            model.model_validate({**base, **changes})
            print(f"[OK]   accepts: {label}")
        except ValidationError as e:
            fails += 1
            print(f"[FAIL] should accept: {label}")
            show(e)
    for label, changes in invalid:
        try:
            model.model_validate({**base, **changes})
            fails += 1
            print(f"[FAIL] should reject: {label}")
        except ValidationError as e:
            print(f"[OK]   rejects: {label}")
            show(e)
    return fails


def check_default(
    model: type[BaseModel], base: Rec, field: str, expected: Any
) -> int:
    rec = {k: v for k, v in base.items() if k != field}
    try:
        actual = getattr(model.model_validate(rec), field)
    except ValidationError as e:
        print(f"[FAIL] default of {field}: validation error")
        show(e)
        return 1
    if actual == expected:
        print(f"[OK]   default {field} = {expected!r}")
        return 0
    print(f"[FAIL] default {field}: expected {expected!r}, got {actual!r}")
    return 1


# -------------------------
# Cases
# -------------------------

STATION_VALID: list[Case] = [
    ("station_id 3 chars", {"station_id": "ABC"}),
    ("station_id 10 chars", {"station_id": "A" * 10}),
    ("name 1 char", {"name": "A"}),
    ("name 50 chars", {"name": "A" * 50}),
    ("crew_size 1", {"crew_size": 1}),
    ("crew_size 20", {"crew_size": 20}),
    ("power_level 0.0", {"power_level": 0.0}),
    ("power_level 100.0", {"power_level": 100.0}),
    ("oxygen_level 0.0", {"oxygen_level": 0.0}),
    ("oxygen_level 100.0", {"oxygen_level": 100.0}),
    ("notes None", {"notes": None}),
    ("notes 200 chars", {"notes": "a" * 200}),
]

STATION_INVALID: list[Case] = [
    ("station_id 2 chars", {"station_id": "AB"}),
    ("station_id 11 chars", {"station_id": "A" * 11}),
    ("name empty", {"name": ""}),
    ("name 51 chars", {"name": "A" * 51}),
    ("crew_size 0", {"crew_size": 0}),
    ("crew_size 21", {"crew_size": 21}),
    ("power_level -0.1", {"power_level": -0.1}),
    ("power_level 100.1", {"power_level": 100.1}),
    ("oxygen_level -0.1", {"oxygen_level": -0.1}),
    ("oxygen_level 100.1", {"oxygen_level": 100.1}),
    ("notes 201 chars", {"notes": "a" * 201}),
    ("last_maintenance not a date", {"last_maintenance": "not a date"}),
]

CONTACT_VALID: list[Case] = [
    ("contact_id 5 chars", {"contact_id": "AC123"}),
    ("contact_id 15 chars", {"contact_id": "AC" + "1" * 13}),
    ("location 3 chars", {"location": "ABC"}),
    ("location 100 chars", {"location": "A" * 100}),
    ("signal 0.0", {"signal_strength": 0.0}),
    ("signal 10.0 (with message)",
     {"signal_strength": 10.0, "message_received": "hello"}),
    ("duration 1", {"duration_minutes": 1}),
    ("duration 1440", {"duration_minutes": 1440}),
    ("witness_count 1", {"witness_count": 1}),
    ("witness_count 100", {"witness_count": 100}),
    ("message 500 chars", {"message_received": "m" * 500}),
    ("contact_type visual", {"contact_type": "visual"}),
    # business rules: accepted side
    ("physical + verified",
     {"contact_type": "physical", "is_verified": True}),
    ("telepathic with exactly 3 witnesses",
     {"contact_type": "telepathic", "witness_count": 3}),
    ("signal exactly 7.0 without message", {"signal_strength": 7.0}),
    ("signal 7.1 with message",
     {"signal_strength": 7.1, "message_received": "hello"}),
]

CONTACT_INVALID: list[Case] = [
    ("contact_id 4 chars", {"contact_id": "AC12"}),
    ("contact_id 16 chars", {"contact_id": "AC" + "1" * 14}),
    ("location 2 chars", {"location": "AB"}),
    ("location 101 chars", {"location": "A" * 101}),
    ("signal -0.1", {"signal_strength": -0.1}),
    ("signal 10.1 (with message)",
     {"signal_strength": 10.1, "message_received": "hello"}),
    ("duration 0", {"duration_minutes": 0}),
    ("duration 1441", {"duration_minutes": 1441}),
    ("witness_count 0", {"witness_count": 0}),
    ("witness_count 101", {"witness_count": 101}),
    ("message 501 chars", {"message_received": "m" * 501}),
    ("contact_type unknown", {"contact_type": "plasma"}),
    # business rules: rejected side (everything else valid!)
    ("contact_id without AC prefix", {"contact_id": "XX_2024_001"}),
    ("physical but not verified",
     {"contact_type": "physical", "is_verified": False}),
    ("telepathic with 2 witnesses",
     {"contact_type": "telepathic", "witness_count": 2}),
    ("signal 7.1 without message", {"signal_strength": 7.1}),
]

MISSION_VALID: list[Case] = [
    ("mission_id 5 chars", {"mission_id": "M2024"}),
    ("mission_id 15 chars", {"mission_id": "M" + "1" * 14}),
    ("mission_name 3 chars", {"mission_name": "ABC"}),
    ("mission_name 100 chars", {"mission_name": "A" * 100}),
    ("destination 3 chars", {"destination": "ABC"}),
    ("destination 50 chars", {"destination": "A" * 50}),
    ("duration 1", {"duration_days": 1}),
    ("duration 3650", {"duration_days": 3650}),
    ("budget 1.0", {"budget_millions": 1.0}),
    ("budget 10000.0", {"budget_millions": 10000.0}),
    ("crew of 1 (captain only)", {"crew": crew_of(1)}),
    ("crew of 12", {"crew": crew_of(12)}),
    # business rules: accepted side
    ("commander only (no captain)",
     {"crew": [member(rank="commander")]}),
    ("365 days, nobody experienced (not 'long')",
     {"duration_days": 365, "crew": crew_of(3, experienced=0)}),
    ("366 days, exactly 50% experienced (2/4)",
     {"duration_days": 366, "crew": crew_of(4, experienced=2)}),
    ("366 days, 2/3 experienced",
     {"duration_days": 366, "crew": crew_of(3, experienced=2)}),
    ("366 days, 2/4 have exactly 5 years",
     {"duration_days": 366, "crew": [
     member(years_experience=5), member(member_id="CM002", rank="officer", years_experience=5),
     member(member_id="CM003", rank="officer", years_experience=0),
     member(member_id="CM004", rank="officer", years_experience=0)]}),
]

MISSION_INVALID: list[Case] = [
    ("mission_id 4 chars", {"mission_id": "M202"}),
    ("mission_id 16 chars", {"mission_id": "M" + "1" * 15}),
    ("mission_name 2 chars", {"mission_name": "AB"}),
    ("destination 2 chars", {"destination": "AB"}),
    ("duration 0", {"duration_days": 0}),
    ("duration 3651", {"duration_days": 3651}),
    ("budget 0.9", {"budget_millions": 0.9}),
    ("budget 10000.1", {"budget_millions": 10000.1}),
    ("crew empty", {"crew": []}),
    ("crew of 13", {"crew": crew_of(13)}),
    # business rules: rejected side
    ("mission_id without M prefix", {"mission_id": "X2024_MARS"}),
    ("no commander or captain",
     {"crew": [member(rank="officer"), member(member_id="CM002",
                                              rank="cadet")]}),
    ("inactive crew member",
     {"crew": [member(), member(member_id="CM002", is_active=False)]}),
    ("366 days, 1/4 experienced",
     {"duration_days": 366, "crew": crew_of(4, experienced=1)}),
    ("366 days, 1/3 experienced (33%)",
     {"duration_days": 366, "crew": crew_of(3, experienced=1)}),
    ("366 days, 2/4 have only 4 years",
     {"duration_days": 366, "crew": [
     member(years_experience=4), member(member_id="CM002", rank="officer", years_experience=4),
     member(member_id="CM003", rank="officer", years_experience=0),
     member(member_id="CM004", rank="officer", years_experience=0)]}),
    # CrewMember field constraints
    ("member age 17", {"crew": [member(age=17)]}),
    ("member age 81", {"crew": [member(age=81)]}),
    ("member_id 2 chars", {"crew": [member(member_id="CM")]}),
    ("member_id 11 chars", {"crew": [member(member_id="A" * 11)]}),
    ("member name 1 char", {"crew": [member(name="A")]}),
    ("specialization 2 chars", {"crew": [member(specialization="AB")]}),
    ("specialization 31 chars",
     {"crew": [member(specialization="A" * 31)]}),
    ("years_experience -1", {"crew": [member(years_experience=-1)]}),
    ("years_experience 51", {"crew": [member(years_experience=51)]}),
    ("rank unknown", {"crew": [member(rank="admiral")]}),
]

# CrewMember boundaries that must be ACCEPTED
MEMBER_VALID_BOUNDARIES: list[Case] = [
    ("member age 18", {"crew": [member(age=18)]}),
    ("member age 80", {"crew": [member(age=80)]}),
    ("member_id 3 chars", {"crew": [member(member_id="CM1")]}),
    ("member_id 10 chars", {"crew": [member(member_id="A" * 10)]}),
    ("member name 2 chars", {"crew": [member(name="Al")]}),
    ("member name 50 chars", {"crew": [member(name="A" * 50)]}),
    ("specialization 3 chars", {"crew": [member(specialization="ABC")]}),
    ("specialization 30 chars",
     {"crew": [member(specialization="A" * 30)]}),
    ("years_experience 0", {"crew": [member(years_experience=0)]}),
    ("years_experience 50", {"crew": [member(years_experience=50)]}),
]


def main() -> int:
    fails = 0
    print("\n🧪 Spec-driven boundary tests")
    print("=" * 60)

    fails += run_group("SpaceStation", SpaceStation, BASE_STATION,
                       STATION_VALID, STATION_INVALID)
    fails += check_default(SpaceStation, BASE_STATION, "is_operational", True)

    fails += run_group("AlienContact", AlienContact, BASE_CONTACT,
                       CONTACT_VALID, CONTACT_INVALID)
    fails += check_default(AlienContact, BASE_CONTACT, "is_verified", False)

    fails += run_group("SpaceMission", SpaceMission, BASE_MISSION,
                       MISSION_VALID + MEMBER_VALID_BOUNDARIES,
                       MISSION_INVALID)
    fails += check_default(SpaceMission, BASE_MISSION, "mission_status",
                           "planned")

    print("\n" + "=" * 60)
    if fails:
        print(f"❌ {fails} unexpected result(s)")
    else:
        print("🎉 All results as expected!")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
