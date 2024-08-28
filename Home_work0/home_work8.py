from typing import Callable


def filter_by_type_decorator(type_to_remove: str):
    def decorator(func: Callable):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, list):
                if type_to_remove == 'str':
                    result = [item for item in result if not isinstance(item, str)]
                elif type_to_remove == 'int':
                    result = [item for item in result if not isinstance(item, int)]
                elif type_to_remove == 'float':
                    result = [item for item in result if not isinstance(item, float)]
            return result

        return wrapper

    return decorator
