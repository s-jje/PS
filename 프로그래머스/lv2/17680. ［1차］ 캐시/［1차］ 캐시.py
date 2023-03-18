from collections import deque


def solution(cache_size, cities):
    if cache_size == 0:
        return len(cities) * 5

    cache = deque(maxlen=cache_size)
    time = 0

    for c in cities:
        city = c.lower()

        if city in cache:
            cache.remove(city)
            cache.append(city)
            time += 1
        else:
            cache.append(city)
            time += 5

    return time