def solution(s):
    count, zeros = 0, 0
    while len(s) > 1:
        count += 1
        num = s.count('1')
        zeros += len(s) - num
        s = bin(num)[2:]
    return [count, zeros]