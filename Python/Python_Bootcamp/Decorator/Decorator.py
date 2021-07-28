def new_decorator(original_func):
    def wrap_func():
        print("Some extra code, before the original code")

        original_func()

        print("Some extra code, after the original code")

    return wrap_func


@new_decorator
def func_needs_decorator():
    print("I want to be decorated!")


# decorated_func = new_decorator(func_needs_decorator)
# decorated_func()

func_needs_decorator()
