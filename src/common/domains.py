import dataclasses
from typing import Any


@dataclasses.dataclass
class BaseDomain:
    def to_dict(self) -> dict[str, Any]:
        return dataclasses.asdict(self)
