
def solution(limit):
    for number in range(1, n+1):
        if number % 15 == 0:
            print("FizzBuzz")
            return
        elif number % 3 == 0:
            print("Fizz")
            return
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
            return
