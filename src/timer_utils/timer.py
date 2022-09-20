import time


class Timer:
    initial_time = time.perf_counter()

    @staticmethod
    def get_current_time():
        return round(time.perf_counter() - Timer.initial_time, 2)

    @staticmethod
    def get_total_time(init_time: float, final_time: float):
        return round(final_time - init_time, 2)
