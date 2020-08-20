import time


def calculate(n):
    return sum(range(n))


start = time.time()
print("Result: ", calculate(100000000))
end = time.time()
print("Pure Python Time: ", end-start)