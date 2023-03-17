def solution(n):
    binary = str(bin(n)[2:])
    ones = binary.count('1')
    while True:
        n += 1
        if str(bin(n)[2:]).count('1') == ones:
            return n