import time

def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper



@cache
def log_running_funtion(a, b):
    time.sleep(4)
    return a + b

print(log_running_funtion(2, 3))
print(log_running_funtion(2, 3))
print(log_running_funtion(4, 3))