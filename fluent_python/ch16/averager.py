# coding: utf-8

import typing


class Result(typing.NamedTuple):
    count: int
    average: float


def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)

