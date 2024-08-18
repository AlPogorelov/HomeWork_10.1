from functools import wraps


def log(filename=None):
    def log_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """Функция проверяет если задана переменная filename то логи в файл, если нет то в консоль."""
            if filename:
                with open(filename, "r+") as file:
                    file.write(f"Function `{func.__name__}` start working.\n")
                    try:
                        result = func(*args, **kwargs)
                    except UnboundLocalError:
                        file.write(f"Function `{func.__name__}` error: UnboundLocalError.\n")
                    except TypeError:
                        file.write(f"Function `{func.__name__}` error: TypeError.\n")
                    else:
                        file.write(f"Result function `{func.__name__}`: {result}.\n")
                    file.write(f"Function `{func.__name__}` finish.\n")
            else:
                print(f"Function `{func.__name__}` start working.")
                try:
                    result = func(*args, **kwargs)
                except UnboundLocalError:
                    print(f"Function `{func.__name__}` error: UnboundLocalError.")
                except TypeError:
                    print(f"Function `{func.__name__}` error: TypeError.")
                else:
                    print(f"Result function `{func.__name__}`: {result}.")
                print(f"Function `{func.__name__}` finish.")
            return result

        return wrapper

    return log_decorator
