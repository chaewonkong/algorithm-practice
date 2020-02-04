def solution(heights):
    ret = []

    while heights:
        target = heights.pop()
        tmp = -1

        for i in range(len(heights)-1, -1, -1):
            if heights[i] > target:
                tmp = i
                break
        ret.append(tmp+1) if tmp != -1 else ret.append(0)

    return list(reversed(ret))


# solution([6, 9, 5, 7, 4])
print(solution([6, 9, 5, 7, 4]))
print(solution([3, 9, 9, 3, 5, 7, 2]))
print(solution([1, 5, 3, 6, 7, 6, 5]))
