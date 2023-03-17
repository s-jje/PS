def solution(s):
    answer = 0
    if len(s) % 2 == 1:
        return answer

    stack = []
    for c in s:
        if len(stack) > 0 and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    if len(stack) == 0:
        answer = 1
    return answer