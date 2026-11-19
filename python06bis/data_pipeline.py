from abc import ABC, abstractmethod
from typing import Any, Protocol


class DataProcessor(ABC):
    name: str = "Data Processor"

    def __init__(self) -> None:
        self.data: list[str] = []
        self._rank: int = 0
        self._total: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: Any) -> None:
        ...

    def _store(self, item: str) -> None:
        self.data.append(item)
        self._total += 1

    def output(self) -> tuple[int, str]:
        if not self.data:
            raise IndexError("No data left on processor")
        text = self.data.pop(0)
        rank = self._rank
        self._rank += 1
        return (rank, text)

    def total(self) -> int:
        return self._total

    def remaining(self) -> int:
        return len(self.data)


class NumericProcessor(DataProcessor):
    name = "Numeric Processor"

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
                self._store(str(item))
        else:
            self._store(str(data))


class TextProcessor(DataProcessor):
    name = "Text Processor"

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
                self._store(item)
        else:
            self._store(data)


class LogProcessor(DataProcessor):
    name = "Log Processor"

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
                self._store(f"{item['log_level']}: {item['log_message']}")
        else:
            self._store(f"{data['log_level']}: {data['log_message']}")

    def _is_log(self, item: Any) -> bool:
        if not isinstance(item, dict):
            return False
        if "log_level" not in item or "log_message" not in item:
            return False
        for key, value in item.items():
            if not isinstance(key, str) or not isinstance(value, str):
                return False
        return True


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            handled = False
            for proc in self._processors:
                if proc.validate(element):
                    try:
                        proc.ingest(element)
                        handled = True
                    except (ValueError, KeyError, TypeError) as e:
                        print(f"DataStream error - {proc.name}: {e}")
                        handled = True
                    break
            if not handled:
                print("DataStream error - "
                      f"Can't process element in stream: {element}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            print(f"{proc.name}: total {proc.total()} items processed, "
                  f"remaining {proc.remaining()} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            batch: list[tuple[int, str]] = []
            for _ in range(nb):
                if proc.remaining() == 0:
                    break
                batch.append(proc.output())
            plugin.process_output(batch)


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        values: list[str] = []
        for rank, value in data:
            values.append(value)
        print(",".join(values))


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        pairs: list[str] = []
        for rank, value in data:
            pairs.append(f'"item_{rank}": "{value}"')
        print("{"+", ".join(pairs) + "}")


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===")

    print("\nInitialize Data Stream...\n")
    stream = DataStream()
    stream.print_processors_stats()

    print("\nRegistering Processors\n")
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    batch1: list[Any] = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {'log_level': 'WARNING',
             'log_message': 'Telnet access! Use ssh instead'},
            {'log_level': 'INFO', 'log_message': 'User wil is connected'},
        ],
        42,
        ['Hi', 'five'],
    ]
    print(f"Send first batch of data on stream: {batch1}\n")
    stream.process_stream(batch1)
    stream.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CSVExportPlugin())
    print()
    stream.print_processors_stats()

    batch2: list[Any] = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [
            {'log_level': 'ERROR', 'log_message': '500 server crash'},
            {'log_level': 'NOTICE',
             'log_message': 'Certificate expires in 10 days'},
        ],
        [32, 42, 64, 84, 128, 168],
        'World hello',
    ]
    print(f"\nSend another batch of data: {batch2}\n")
    stream.process_stream(batch2)
    stream.print_processors_stats()
    print("\nSend 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JSONExportPlugin())
    print()
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
