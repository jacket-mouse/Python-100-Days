def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for index, val in enumerate(fib(20)):
        print(index, val)


if __name__ == '__main__':
    main()