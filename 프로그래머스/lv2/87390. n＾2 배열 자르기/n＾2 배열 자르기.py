def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        row, col, = i // n + 1, i % n + 1
        answer.append(max(row, col))
    return answer