# coding: utf-8

from queue import PriorityQueue
from typing import NamedTuple


class Event(NamedTuple):
    time: int  # 事件发生时间
    proc: int  # 出租车编号
    action: str  # 描述活动的字符串


def taxi_process(ident, trips, start_time=0):
    """每次改变状态时，创建事件，然后把控制树交给仿真器 """
    time = yield Event(start_time, ident, "离开车库")
    for i in range(trips):
        time = yield Event(time, ident, "拉到客人")
        time = yield Event(time, ident, "客人下车")
    yield Event(time, ident, "回家")


def compute_duration(pre_action: str) -> int:
    return 3


class Simulator:
    def __init__(self, procs_map: dict):
        self.events = PriorityQueue()
        self.procs = dict(procs_map)

    def run(self, end_time):
        """排定并显示事件，直到时间结束"""

        # 排定各辆出租车的第一个事件
        for _, proc in sorted(self.procs.items()):
            first_event = next(proc)
            self.events.put(first_event)

        # 仿真系统的主循环
        sim_time = 0
        while sim_time < end_time:
            if self.events.empty():
                print("*** end of events ***")
                break

            current_event = self.events.get()
            sim_time, proc_id, pre_action = current_event
            print("taxi:", proc_id, proc_id * "    ", current_event)
            active_proc = self.procs[proc_id]
            next_time = sim_time + compute_duration(pre_action)
            try:
                next_event = active_proc.send(next_time)
            except StopIteration:
                del self.procs[proc_id]
            else:
                self.events.put(next_event)
        else:
            msg = (
                f"*** end of simulation time: {self.events.qsize()} events pending ***"
            )
            print(msg)


DEPARTURE_INTERVAL = 5


def main():
    num_taxis = 3
    taxis = {
        i: taxi_process(i, (i + 1) * 2, i * DEPARTURE_INTERVAL)
        for i in range(num_taxis)
    }
    sim = Simulator(taxis)
    sim.run(30)


if __name__ == "__main__":
    main()
