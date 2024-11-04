def fizz_buzz(n):
    for x in range(1, n + 1):
        if x % 5 == 0 and x % 3 == 0:
            print("FizzBuzz")
        elif x % 5 == 0:
            print("Buzz")
        elif x % 3 == 0:
            print("Fizz")
        else:
            print(x)


fizz_buzz(20)
