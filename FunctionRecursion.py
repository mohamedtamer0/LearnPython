# FunctionRecursion

def cleanWord(word):
    if len(word) == 1:
        return word

    if word[0] == word[1]:
        return cleanWord(word[1:])

    return word


print(cleanWord("WWWoooorrrldd"))
