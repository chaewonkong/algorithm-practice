INF = 1000000


def solution(A):
    exists = [0] * INF
    for item in A:
        if item > 0:
            exists[item-1] = 1
    for i in range(INF):
        if exists[i] == 0:
            return i+1


print(solution([1, 3, 6, 4, 1, 2]))
