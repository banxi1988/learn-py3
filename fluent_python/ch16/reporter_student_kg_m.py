# coding: utf-8
from fluent_python.ch16.averager import averager, Result


def grouper(results, key):
    while True:
        results[key] = yield from averager()


def main(data):
    results = {}
    for key, values in data.items():
        group = grouper(results, key)
        next(group)  # 预激活生成器，这里是指子生成器
        for value in values:
            group.send(value)  # 传值给子生成器
        group.send(None)  # 让子生成器结束计算
    report(results)


def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(":")
        print(f"{result.count:2} {group:5} averaging {result.average:.2f} {unit}")


data = {
    "girls:kg": [40.9, 38.5, 44.3],
    "girls:m": [1.6, 1.51, 1.4],
    "boys:kg": [35.0, 60.8, 53.2],
    "boys:m": [1.7, 1.75, 1.73],
}
if __name__ == "__main__":
    main(data)
