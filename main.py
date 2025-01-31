import memcache


cache_client = memcache.Client([('127.0.0.1', 11211)])

def memorize(func):
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        result = cache_client.get(key)
        if result is None:
            result = func(*args, **kwargs)
            cache_client.set(key, result,30)
        return result
    return wrapper

@memorize
def number_fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return number_fibonacci(n - 1) + number_fibonacci(n - 2)


for i in range(1, 10000):  
    print(f"Fibonacci({i}) = {number_fibonacci(i)}")
