import memcache


cache = memcache.Client(['127.0.0.1:11211'], debug=0)

for cache_key in cache.keys():
    print(cache_key)

# def cache (func):
#     cache = memcache.Client(['127.0.0.1:11211'], debug=0)
#     def wrapper(*args, **kwargs):
#         key = str(args) + str(kwargs)
#         result = cache.get(key)
#         if result is None:
#             result = func(*args, **kwargs)
#             cache.set(key, result)
#         return result

#     return wrapper

# @cache
# def number_fibonaci(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     else:
#         return number_fibonaci(n - 1) + number_fibonaci(n - 2)
    
# for i in range(1,100000):
#     print(number_fibonaci(i))