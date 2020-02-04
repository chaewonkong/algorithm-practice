import heapq


def solution(stock, dates, supplies, k):
    answer = 0
    h = []
    start = 0

    while stock < k:

        for i in range(start, len(dates)):
            if dates[i] <= stock:
                heapq.heappush(h, (-supplies[i], supplies[i]))
                start = i + 1
            else:
                break

        stock += heapq.heappop(h)[1]
        answer += 1

    return answer


print(solution(4, [4, 10, 15], [20, 5, 10], 30))
