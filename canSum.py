"""Takes an array of numbers as input and checks if a certain target sum can be created and returns a Bool"""

def canSum(targetSum, numbers):
    if targetSum == 0: # base case: getting 0 by substracting 2 or more numbers from each other proves that there is a valid combo
        return True
    if targetSum < 0: # base case
        return False
    for num in numbers: # checks which base case is reached for each path in the recursion tree
        remainder = targetSum - num # remainder variable replaces the targetSum variable for the next nodes in the recursion tree
        if canSum(remainder, numbers) == True:
            return True

    return False

def canSum_memo(targetSum, numbers, memo):

    if targetSum in memo: # adds another base case that caches duplicate nodes and returns the Bool they represent
        return memo[targetSum]

    if targetSum == 0:
        return True
    if targetSum < 0:
        return False

    for num in numbers:
        remainder = targetSum - num

        if canSum_memo(remainder, numbers, memo) == True:
            memo[targetSum] = True # stores the Bool in the memo variable
            return True
    memo[targetSum] = False # stores the Bool in the memo variable
    return False