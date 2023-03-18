def solution(s):
    set_list = sorted([set_str.split(',') for set_str in s[2:-2].split('},{')], key=len)

    answer = []
    for set_i in set_list:
        for es in set_i:
            e = int(es)
            if e not in answer:
                answer.append(e)

    return answer