def solution(s):
    s = s.split(' ')
    s = [w.capitalize() for w in s]
    return ' '.join(s)
