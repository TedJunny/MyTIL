import time


def timer_decorator(function):
    def wrapper(*args, **kwargs):
        start = time.time()

        function(args)

        func_duration = time.time() - start

        return func_duration

    return wrapper


@timer_decorator
def tuple_iteration(num_tuple: tuple):
    for num in num_tuple:
        pass


@timer_decorator
def set_iteration(num_set: set):
    for num in num_set:
        pass


@timer_decorator
def str_iteration(num_str: str):
    for num in num_str:
        pass


print(tuple_iteration(tuple([num for num in range(10000000)])))
