def solution(s):
    set_list = sorted([[int(e) for e in _set_str.replace('{', '').replace('}', '').split(',')] for _set_str in s[1:-1].split('},')], key=len)

    answer = []
    for _set in set_list:
        _set = [e for e in _set if e not in answer]
        answer.append(_set.pop())

    return answer