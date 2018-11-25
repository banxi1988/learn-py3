# coding: utf-8
from fluent_python.ch16.averager import averager, Result


def test_averager():
    coro_avg = averager()
    next(coro_avg)  # 预激活生成器
    coro_avg.send(10)
    coro_avg.send(20)
    coro_avg.send(30)
    try:
        coro_avg.send(None)  # 结束执行
    except StopIteration as si:
        print(si)
        assert si.value == Result(3, 20)

