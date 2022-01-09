"""find the quickest way to sum two numbers in an array to get the target sum"""

def bestSum(targetSum, numbers):
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    shortestCombination = None
    for num in numbers:
        remainder = targetSum - num
        remainderResult = bestSum(remainder, numbers)
        if remainderResult != None:
            result = [*remainderResult, num]
            if shortestCombination == None or len(result) < len(shortestCombination):
                shortestCombination = result

    return shortestCombination

def bestSum_memo(targetSum, numbers, memo):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    shortestCombination = None
    for num in numbers:
        remainder = targetSum - num
        remainderResult = bestSum_memo(remainder, numbers, memo)
        if remainderResult != None:
            result = [*remainderResult, num]
            if shortestCombination == None or len(result) < len(shortestCombination):
                shortestCombination = result

    memo[targetSum] = shortestCombination
    return memo[targetSum]

print(bestSum_memo(127, [12,13,14], {}))