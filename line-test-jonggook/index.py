"""
반환되는 두 정수 값의 합은 주어진 목표 정수 값과 동일해야 함.
반드시 O(n) 이하로 풀어야됨.

"""


def solution(arr, target):
    dic = {}

    for i in range(len(arr)):
        sub = target - arr[i]
        if sub in dic.keys():
            return [dic[sub], i]
        dic[arr[i]] = i
    return None


print(solution([2, 5, 7, 11, 15, 4], 9))
