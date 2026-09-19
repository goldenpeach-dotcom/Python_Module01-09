from pydantic import BaseModel, Field, model_validator
from datetime import datetime
from enum import Enum


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission(self):
        # 1. ミッションIDは M で始まる
        if not self.mission_id.startswith("M"):
            raise ValueError("mission_id must start with 'M'")

        # 2. 司令官または船長が最低1人必要
        has_leader = any(
            member.rank in {Rank.captain, Rank.commander}
            for member in self.crew
        )
        if not has_leader:
            raise ValueError("Mission must include at least one captain or commander")

        # 3. 長期ミッション（365日超）は経験5年以上が50%以上必要
        if self.duration_days > 365:
            experienced = sum(1 for m in self.crew if m.years_experience >= 5)
            if experienced < len(self.crew) * 0.5:
                raise ValueError(
                    "Long missions require at least 50% experienced crew (>=5 years)"
                )

        # 4. 全乗組員がアクティブであること
        inactive = [m.name for m in self.crew if not m.is_active]
        if inactive:
            raise ValueError(f"Inactive crew members found: {inactive}")

        return self
