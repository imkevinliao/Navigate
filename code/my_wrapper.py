import traceback
from time import time, sleep


def timer(func):
    """
    @timer
    def show(name):
        print(name)

    show = wrapper   <==>   show = timer(show)
    """

    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        args = "" if not args else args
        kwargs = "" if not kwargs else kwargs
        print(f"function {func.__name__} {args} {kwargs}, takes {end - start} seconds")
        return result

    return wrapper


def delay(seconds: int = 1):
    """
    such as:
    @delay(3)
    def show(name):
        print(name)
    default delay one second, when function start. such as: @delay()
    """

    def decorate(func):
        def wrapper(*args, **kwargs):
            sleep(seconds)
            result = func(*args, *kwargs)
            return result

        return wrapper

    return decorate


def error_handler(func):
    """
    @error_handler
    def demo():
        res = 1 / 0
        return res

    If the function run fails, will return str "error", so you can judge by this.

    res = demo()
    if res == "error":
        print("function run failed")
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"function {func.__name__} error")
            print(f"{e}\n{traceback.format_exc()}")
            return "error"
    return wrapper


def func_hint(func):
    """
    show func start and end in console
    """
    def wrapper(*args, **kwargs):
        h_str = f"*" * 10
        print(f"{h_str} {func.__name__} func start {h_str}")
        result = func(*args, **kwargs)
        print(f"{h_str} {func.__name__} func  end  {h_str}")
        return result

    return wrapper


@func_hint
def test_func_hint():
    print("do some thing")


if __name__ == '__main__':
    test_func_hint()
