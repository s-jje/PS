def solution(clothes):
    clothes_dict = {}
    for _, t in clothes:
        if not clothes_dict.get(t):
            clothes_dict[t] = 1
        else:
            clothes_dict[t] += 1

    answer = 1
    for n in clothes_dict.values():
        answer *= n + 1
    return answer - 1