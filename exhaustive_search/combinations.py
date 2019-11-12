# Combinations
# 0부터 연속한 m개의 정수 중 n개를 뽑는 모든 경우


def get_all_combinations(m, n):
    population = list(range(m))
    combination_list = list()
    selected_list = list()
    is_consumed = [0] * m

    def find_combination(selected_list, count_left):
        if count_left == 0:
            return combination_list.append(selected_list.copy())

        start = selected_list[-1] + 1 if selected_list else 0

        for i in range(start, m):
            if i == 0 or population[i] != population[i-1] or is_consumed[i-1]:
                selected_list.append(i)
                is_consumed[i] = 1
                find_combination(selected_list, count_left-1)
                selected_list.pop()
                is_consumed[i] = 1

    find_combination(selected_list, n)
    return combination_list


if __name__ == "__main__":
    m, n = map(int, input().split())
    print(get_all_combinations(m, n))

#


def get_all_combinations(arr, N):
    """Return all combinations of N number item from given arr"""
    combinations = []
    picked = []
    used = [0] * len(arr)

    def find(picked, topick):
        """get combinations by recursion"""
        if topick == 0:
            ret = [arr[i] for i in picked]
            # used라는 리스트를 만들고 거기에 사용 여부를 담으면 O(1)로 접근 가능하다
            combinations.append(ret)
            return
        start = picked[-1] + 1 if picked else 0
        for i in range(start, len(arr)):
            if i == 0 or arr[i] != arr[i-1] or used[i-1]:
                picked.append(i)
                used[i] = 1
                find(picked, topick-1)
                picked.pop()
                used[i] = 0

    find(picked, N)
    return combinations
