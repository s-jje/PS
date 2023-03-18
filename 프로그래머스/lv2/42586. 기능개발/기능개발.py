from collections import deque


def solution(progresses, speeds):
    answer = []
    
    progresses = deque(progresses)
    speeds = deque(speeds)

    while progresses:
        progresses = deque(sum(e) for e in zip(progresses, speeds))
        count = 0

        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            count += 1

        if count > 0:
            answer.append(count)

    return answer