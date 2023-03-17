def solution(citations):
    citations.sort(reverse=True)
    h = 0
    for citation in citations:
        if h >= citation:
            return h
        h += 1
    return len(citations)