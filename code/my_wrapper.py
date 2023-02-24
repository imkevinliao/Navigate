import traceback
import time
import functools
import inspect
import collections


def timer(func):
    """
    calculates the time it takes to run the function.
    for example:
    @timer
    def show(name):
        print(name)
    show("kevin")
    """
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Run function {func.__name__} takes {end - start} seconds")
        return result
    
    return wrapper


def delay(seconds: int = 1):
    """
    default delay one second, when function start.
    for example:
    @delay(3)
    def show(name):
        print(name)
    show("kevin")
    """
    
    def decorate(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            time.sleep(seconds)
            result = func(*args, *kwargs)
            return result
        
        return wrapper
    
    return decorate


def error_handler(func):
    """
    If the function run fails, will return str "error", so you can judge by this if you need.
    for example:
    @error_handler
    def error_demo():
        return 1 / 0
    result = error_demo()
    if "error" == result:
        print("function run failed")
    """
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"{e}\n{traceback.format_exc()}")
            return "error"
    
    return wrapper


def func_hint(func):
    """
    prompt function start and end execution
    for example:
    @func_hint
    def show(name):
        print(name)
    show("kevin")
    """
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        prompter = "*"
        length = 15
        hint_str = prompter * length
        print(f"{hint_str} {func.__name__} start {hint_str}")
        result = func(*args, **kwargs)
        print(f"{hint_str} {func.__name__}  end  {hint_str}")
        return result
    
    return wrapper


def param_check(func):
    """
    函数参数检查装饰器，需要配合函数注解表达式（Function Annotations）使用
    for example:
    @param_check
    def show(x: int, y: float, z: str):
        print(f"{x}:{type(x)}")
        print(f"{y}:{type(y)}")
        print(f"{z}:{type(z)}")
    show(1, 2, 3)
    ------
    result:
    func <show> argument y must be <class 'float'>,but got <class 'int'>,value 2
    func <show> argument z must be <class 'str'>,but got <class 'int'>,value 3
    """
    # 获取函数定义的参数
    sig = inspect.signature(func)
    parameters = sig.parameters  # 参数有序字典
    arg_keys = tuple(parameters.keys())  # 参数名称
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        CheckItem = collections.namedtuple('CheckItem', ('anno', 'arg_name', 'value'))
        check_list = []
        
        # collect args   *args 传入的参数以及对应的函数参数注解
        for i, value in enumerate(args):
            arg_name = arg_keys[i]
            anno = parameters[arg_name].annotation
            check_list.append(CheckItem(anno, arg_name, value))
        
        # collect kwargs  **kwargs 传入的参数以及对应的函数参数注解
        for arg_name, value in kwargs.items():
            anno = parameters[arg_name].annotation
            check_list.append(CheckItem(anno, arg_name, value))
        
        # check type
        errors = []
        for item in check_list:
            if not isinstance(item.value, item.anno):
                error = f'func <{func.__name__}> argument {item.arg_name} must be {item.anno},' \
                        f'but got {type(item.value)},value {item.value} '
                errors.append(error)
        if errors:
            raise TypeError("\n" + "\n".join(errors))
        return func(*args, **kwargs)
    
    return wrapper

if __name__ == '__main__':
    ...
