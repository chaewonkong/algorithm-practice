# Advanced Combinations
# Get all combinations of selecting n number of items from given population


def get_all_combinations(population, n):
    m = len(population)
    combinations = list()
    selected_idx = list()
    consumed = [0 for _ in range(m)]

    def find(selected, count_left):
        if count_left == 0:
            return combinations.append([population[i] for i in selected_idx])
        start = selected_idx[-1] + 1 if selected_idx else 0

        for i in range(start, m):
            # i가 0, 즉 뽑히지 않았거나, population에 중복된 수가 있거나, i-1이 사용된 경우
            if i == 0 or population[i] != population[i-1] or consumed[i-1]:
                selected_idx.append(i)
                consumed[i] = 1
                find(selected_idx, count_left - 1)
                selected.pop()
                consumed[i] = 0

    find(selected_idx, n)
    return combinations


if __name__ == "__main__":
    population = [int(i) for i in input().split()]
    n = int(input())
    print(get_all_combinations(population, n))
