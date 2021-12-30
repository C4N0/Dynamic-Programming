"""Number of possibilities to travel through a mxn matrix with just
    the "up" and "right" arrow keys"""
import time
import pandas as pd


def gridTravel(m, n):
    if m == 1 and n == 1:  # Base case for recursion
        return 1
    elif m == 0 or n == 0:  # another base case
        return 0
    else:
        return gridTravel(m - 1, n) + gridTravel(m, n - 1)


def gridTravel_memo(m, n, memo):
    key = str(m) + "," + str(n)  # delineates a cacheable variable for the memo
    if key in memo:
        return memo[key]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    else:
        memo[key] = gridTravel_memo(m - 1, n, memo) + gridTravel_memo(m, n - 1, memo)
        return memo[key]


start = time.time()
a = gridTravel_memo(10, 10, {})
b = gridTravel_memo(20, 20, {})
c = gridTravel_memo(30, 30, {})
d = gridTravel_memo(40, 40, {})




frame = pd.DataFrame({"10x10 Matrix": a, "20x20 Matrix": b, "30x30 Matrix": c, "40x40 Matrix": d},{"Possibilities"})
print(frame)
end = time.time()
exact_time = end - start  # time in seconds needed to run the code
print(exact_time)
