"""Problem: FizzBuzz — print 1-100, Fizz for multiples of 3, Buzz for 5, FizzBuzz for both."""


def fizzbuzz(n: int = 100) -> None:
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == "__main__":
    fizzbuzz()
