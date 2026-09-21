from typing_extensions import Self
from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from enum import Enum


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: str | None = Field(None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def validate_contact(self) -> Self:
        # 1. コンタクトIDは「AC」で始まる必要がある
        if not self.contact_id.startswith("AC"):
            raise ValueError("contact_id must start with 'AC'")

        # 2. 物理的接触は検証済みでなければならない
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError(
                "Physical contact reports must be verified"
            )

        # 3. テレパシーは目撃者が3人以上必要
        if (
            self.contact_type == ContactType.telepathic
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )

        # 4. 強い信号（> 7.0）は message_received が必須
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (>7.0) "
                "must include a received message"
            )

        return self


def main() -> None:
    print("Alien Contact Log Validation")

    try:
        ac = AlienContact(
            contact_id="AC12345",
            timestamp=datetime.now(),
            location="Sector 7",
            contact_type=ContactType.radio,
            signal_strength=5.5,
            duration_minutes=30,
            witness_count=4,
            message_received="Hello from beyond.",
            is_verified=True
        )

        print("Valid contact report:")
        print(f"ID: {ac.contact_id}")
        print(f"Type: {ac.contact_type.value}")
        print(f"Location: {ac.location}")
        print(f"Signal: {ac.signal_strength}")
        print(f"Duration: {ac.duration_minutes} minutes")
        print(f"Witnesses: {ac.witness_count}")
        print(f"Message: '{ac.message_received}'")

    except ValidationError as e:
        print("Unexpected validation error:", e)

    print("\nExpected validation error:")
    try:
        AlienContact(
            contact_id="AC99999",
            timestamp=datetime.now(),
            location="Sector X",
            contact_type=ContactType.telepathic,
            signal_strength=8.0,
            duration_minutes=10,
            witness_count=1,  # invalid
            message_received="Mind link established.",
            is_verified=True
        )
    except ValidationError as e:
        for err in e.errors():
            print(err["msg"])


if __name__ == "__main__":
    main()
