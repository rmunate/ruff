from typing import reveal_type

type T[X] = list[X]

class X[T]:
    x: list[T]

def y(x: X[int]) -> None:
    reveal_type(x)
