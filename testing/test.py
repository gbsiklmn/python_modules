from abc import ABC, abstractmethod
from typing import Any

class DataProcessor(ABC):
    def __init__(self) -> None:
        self.data: list[str] = []
        self._rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: Any) -> None:
        ...

    def output(self) -> tuple[int, str]:
        text = self.data.pop(0)
        rank = self._rank
        self._rank += 1
        return(rank, text)

class Dummy(DataProcessor):
    def validate(self, data: Any) -> bool:
        return True

    def ingest(self, data: Any) -> None:
        self.data.append(str(data))


p1 = Dummy()
p2 = Dummy()
p1.ingest(10)
p1.ingest(20)
p2.ingest("hi")
print(p1.data)
print(p2.data)
print(p1.output())
print(p2.output())