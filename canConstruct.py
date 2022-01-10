"""Checks through a Bool if a target string can be created from an array of strings"""

def canConstruct(target, wordBank):
    if target == '':
        return True

    for word in wordBank:
        if target.startswith(word) == True:
            suffix = target[len(word)::]
            if canConstruct(suffix, wordBank) == True:
                return True

    return False

print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))


def canConstruct_memo(target, wordBank, memo):
    if target in memo:
        return memo[target]
    if target == '':
        return True

    for word in wordBank:
        if target.startswith(word) == True:
            suffix = target[len(word)::]
            if canConstruct_memo(suffix, wordBank, memo) == True:
                memo[target] = True
                return True

    memo[target] = False
    return False

print(canConstruct_memo("easfweugibrugbufodwefbisufrbgiufa", ["ee", "as", "e", "weffiubjfdn"], {}))