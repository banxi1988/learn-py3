def make_averager():
    series = []

    def averager(value):
        series.append(value)
        total = sum(series)
        return total / len(series)

    return averager


def make_o1_averager():
    total = 0
    count = 0

    def averager(value):
        nonlocal total, count
        total += value
        count += 1
        return total / count

    return averager


def test_on1_average():
    avg = make_averager()
    assert avg(10) == 10
    assert avg(12) == 11
    assert avg(14) == 12

    avg2 = make_o1_averager()
    assert avg2(10) == 10
    assert avg2(12) == 11
    assert avg2(14) == 12
