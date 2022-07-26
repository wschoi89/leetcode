import time


def my_timer(func):
    def wrapper(s):
        t_start = time.perf_counter()
        print(func(s))
        print(f" {func.__name__} 실행 시간: {time.perf_counter() - t_start}")
    return wrapper