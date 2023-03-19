def solution(elements):
    sequence_set = set(elements)

    for i in range(2, len(elements) + 1):
        for j in range(len(elements)):
            if j + i <= len(elements):
                sequence_set.add(sum(elements[j:j + i]))
            else:
                first_length = len(elements) - j
                second_end = i - first_length
                sequence_set.add(sum(elements[j:]) + sum(elements[:second_end]))

    return len(sequence_set)