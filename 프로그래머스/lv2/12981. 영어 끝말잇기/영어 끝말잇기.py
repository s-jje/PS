def solution(n, words):
    words_dict = {word: 0 for word in words}
    words_dict[words[0]] += 1
    
    for i in range(1, len(words)):
        words_dict[words[i]] += 1
        if words[i - 1][-1] != words[i][0] or words_dict[words[i]] > 1:
            return [i % n + 1, i // n + 1]

    return [0, 0]