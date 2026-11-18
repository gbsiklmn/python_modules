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
        return (rank, text)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, (int, float)):
                    return False
            return True
        return isinstance(data, (int, float))

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self.data.append(str(item))
        else:
            self.data.append(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, str):
                    return False
            return True
        return isinstance(data, str)

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for item in data:
                self.data.append(item)
        else:
            self.data.append(data)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for item in data:
                if not self._is_log(item):
                    return False
            return True
        return self._is_log(data)
    
    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            for item in data:
                self.data.append(f"{item['log_level']}: {item['log_message']}")
        else:
            self.data.append(f"{data['log_level']}: {data['log_message']}")


    def _is_log(self, item: Any) -> bool:
        if not isinstance(item, dict):
            return False
        for key, value in item.items():
            if not isinstance(key, str) or not isinstance(value, str):
                return False
        return True


def main() -> None:
    print("=== Code Nexus - Data Processor ===")
    print("\nTesting Numeric Processor...")
    num = NumericProcessor()
    print(f" Trying to validate input '42': {num.validate(42)}")
    print(f" Trying to validate input 'Hello': {num.validate('Hello')}")
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num.ingest("foo")
    except ValueError as e:
        print(f"Got exception: {e}")

    numbers = [1, 2, 3, 4, 5]
    print(f" Processing data: {numbers}")
    num.ingest(numbers)
    print("Extracting 3 values...")
    for _ in range(3):
        rank, value = num.output()
        print(f" Numeric value {rank}: {value}")

    print("\nTesting Text Processor...")
 
    tp = TextProcessor()
    print(f" Trying to validate input '42': {tp.validate(42)}")
    texts = ['Hello', 'Nexus', 'World']
    print(f" Processing data: {texts}")
    tp.ingest(texts)
    print("Extracting 1 value...")
    rank, value = tp.output()
    print(f" Text value {rank}: {value}")

    print("\nTesing Log Processor...")
    lp = LogProcessor()
    print(f" Trying to validate input 'Hello': {lp.validate('Hello')}")

    logs = [
    {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
    {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'},
    ]
    print(f" Processing data: {logs}")
    lp.ingest(logs)
    print("Extracting 2 values...")
    for _ in range(2):
        rank, value = lp.output()
        print(f"Loga entry {rank}: {value}")


if __name__ == "__main__":
    main()
