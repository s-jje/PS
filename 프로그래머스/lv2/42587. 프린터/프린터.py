from collections import deque


def solution(priorities, location):
    queue = deque(list(enumerate(priorities)))
    answer = 0

    while queue:
        top = queue.popleft()

        if queue and top[1] < max(queue, key=lambda x: x[1])[1]:
            queue.append(top)
        else:
            answer += 1
            if top[0] == location:
                return answer