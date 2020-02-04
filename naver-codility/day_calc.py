# Day와 더할 날짜 K가 주어지면 K일 후의 요일 찾기
# ex: Wed, 2 => Fri


def solution(S, K):
    days = ["Mon", "Tue", "Wed", "Thr", "Fri", "Sat", "Sun"]
    target = days.index(S) + K

    return days[target % 7]


print(solution("Sat", 23))
