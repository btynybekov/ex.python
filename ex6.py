def compute():
    N = 100
    x = sum(i for i in range(1, N + 1))
    y = sum(i**2 for i in range(1, N + 1))
    return str(x**2 - y)

if __name__ == "__main__":
    print(compute())
