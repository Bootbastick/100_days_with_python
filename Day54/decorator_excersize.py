import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(function):
    def wrapper():
        starting_time = time.time()
        function()
        ending_time = time.time()
        time_needed = ending_time - starting_time
        print(f"time needed to run the {function.__name__} function: {time_needed}")
    return wrapper

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
