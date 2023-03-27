def solution(land):
    row_len = 4

    for i in range(1, len(land)):
        for j in range(row_len):
            land[i][j] += max(land[i - 1][(j + 1) % row_len], land[i - 1][(j + 2) % row_len], land[i - 1][(j + 3) % row_len])

    return max(land[-1])