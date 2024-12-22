from typing import TypeVar, Generator

T = TypeVar("T")


def split_every(items: list[T], n: int) -> Generator[list[T], None, None]:
    # looping till length l
    for i in range(0, len(items), n):
        yield items[i : i + n]
