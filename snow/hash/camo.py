def solution(clothes):
    cloth_dict = dict()
    total = 1

    for item, key in clothes:
        if key in cloth_dict.keys():
            cloth_dict[key].append(item)
        else:
            cloth_dict[key] = [item]

    for key in cloth_dict.keys():
        total *= (len(cloth_dict[key]) + 1)

    return total - 1


print(solution([["yellow_hat", "headgear"], [
      "blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]	))

print(solution([["crow_mask", "face"], [
      "blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
