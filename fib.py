import time


def fib40(n):
    if n <= 1:
        return n
    else:
        return fib40(n-1) + fib40(n-2)


def fib_memo(n, memo):
    # Reducing the 2**n complexity via memoization
    if n in memo:
        return memo[n]
    elif n <= 1:
        return n
    else:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
        return memo[n]
start = time.time()
print(fib_memo(40, {}))
end = time.time()

exact_time = end - start
print(exact_time)
