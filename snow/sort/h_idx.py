def solution(citations):
    citations.sort()

    answer = 0
    start = 0
    end = len(citations)
    mid = (start + end) // 2 + 1

    while start < mid and end > mid:
        if is_possible(mid, citations):
            answer = max(mid, answer)
            start = mid+1
            mid = (start + end) // 2
        else:
            end = mid
            mid = (start + end) // 2

    if is_possible(mid, citations):
        answer = max(answer, mid)
    return answer


def is_possible(target, citations):
    return len(list(filter(lambda x: x >= target, citations))) >= target


"""Best Solved
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0
"""


print(solution([6, 0, 3, 1, 5]))
print(solution([3, 3]))
print(solution([1000, 999, 998]))
print(solution([1000, 999, 998, 997]))
print(solution([2, 1, 0]))
