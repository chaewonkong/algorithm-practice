# 주어진 int N의 특정 자리수에 5를 추가하여(더하는거 아니고 자릿수 늘리는거임) 최대의 N 만들기
# 268 => 5268
# 670 => 6750


MINIMUM = -99999


def solution(N):

    is_negative = False

    if N < 0:
        is_negative = True

    num_list = [int(n) for n in str(abs(N))]
    length = len(num_list)
    maximum = MINIMUM

    for i in range(length+1):
        tmp = num_list.copy()
        targets = [-1 for _ in range(length+1)]
        targets[i] = 5
        for i in range(length + 1):
            if targets[i] == -1:
                targets[i] = tmp.pop(0)

        mul = 1
        new_num = 0
        while targets:
            new_num += mul*targets.pop()
            mul *= 10

        if is_negative:
            new_num = -new_num
        if new_num > maximum:
            maximum = new_num

    return maximum


print(solution(0))
