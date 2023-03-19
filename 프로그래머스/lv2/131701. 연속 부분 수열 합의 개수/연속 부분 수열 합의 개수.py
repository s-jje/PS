def solution(elements):
    sequence_set = set(elements)
    length = len(elements)

    for i in range(length):
        partial_sum = 0
        for j in range(i, i + length):
            partial_sum += elements[j % length]
            sequence_set.add(partial_sum)

    return len(sequence_set)