def solution(arr):
    n = arr[0]
    for i in range(1, len(arr)):
        n = lcm(n, arr[i])
    return n


def gdc(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        c = a % b
        a, b = b, c
    return a


def lcm(a, b):
    return a * b / gdc(a, b)