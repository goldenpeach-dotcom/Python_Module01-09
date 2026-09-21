from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")

    try:
        ss = SpaceStation(
            station_id="ST01",
            name="Orbital One",
            crew_size=10,
            power_level=85.0,
            oxygen_level=92.0,
            last_maintenance=datetime.now(),
            notes="All systems nominal."
        )

        print("Valid station created:")
        print(f"ID: {ss.station_id}")
        print(f"Name: {ss.name}")
        print(f"Crew: {ss.crew_size} people")
        print(f"Power: {ss.power_level}%")
        print(f"Oxygen: {ss.oxygen_level}%")
        print(f"Status: {ss.is_operational}")

    except ValidationError as e:
        print("Unexpected validation error:", e)

    print("\nInvalid station example:")
    try:
        SpaceStation(
            station_id="BAD",
            name="TooManyCrew",
            crew_size=50,  # invalid
            power_level=50.0,
            oxygen_level=50.0,
            last_maintenance=datetime.now(),
            is_operational=False,
            notes=None,
        )
    except ValidationError as e:
        print("Validation error: ", e)


if __name__ == "__main__":
    main()
