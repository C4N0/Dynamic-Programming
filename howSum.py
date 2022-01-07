"""Shows me if there is a combination of numbers that add up to the target sum"""

def howSum(targetsum, numbers):
    if targetsum == 0:
        return []
    if targetsum < 0:
        return None

    for num in numbers:
        remainder = targetsum - num
        remainderResult = howSum(remainder, numbers)
        if remainderResult != None:
            return [*remainderResult, num]

    return None


def howSum_memo(targetsum, numbers, memo):
    if targetsum in memo:
        return memo[targetsum]
    if targetsum == 0:
        return []
    if targetsum < 0:
        return None

    for num in numbers:
        remainder = targetsum - num
        remainderResult = howSum_memo(remainder, numbers, memo)
        if remainderResult != None:
            memo[targetsum] = [*remainderResult, num]
            return memo[targetsum]

    memo[targetsum] = None
    return None


print(howSum_memo(3003, [7,14], {}))