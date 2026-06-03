from dataclasses import dataclass, asdict


@dataclass
class Alarm:
    id: int
    trigger_time: str
    label: str
    repeat: str = "none"
    enabled: bool = True

    def to_dict(self):
        return asdict(self)