words = ["adsdf","sfd"]

def isTrue(row, word):
    matchCount = 0
    for letter in word:
        for char in row:
            if (char == letter):
                matchCount += 1
    return matchCount


def findWords(words):
    output = []
    row1 = "qwertyuiop"
    row2 = "asdfghjkl"
    row3 = "zxcvbnm"



    for x in range(len(words)):
        matchCount = isTrue(row1, words[x].lower())
        if (matchCount == len(words[x])):
            output.append(words[x])

        matchCount = isTrue(row2, words[x].lower())
        print(matchCount, words[x])
        if (matchCount == len(words[x])):
                output.append(words[x])

        matchCount = isTrue(row3, words[x].lower())
        if (matchCount == len(words[x])):
            output.append(words[x])

    print(output)


findWords(words)