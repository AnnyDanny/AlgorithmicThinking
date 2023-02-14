def minion_game(string):
    scoreConconants = 0
    scoreVowels = 0

    for substrLen in range(1, len(string) + 1):
        for startPos in range(len(string)):
            if substrLen + startPos > len(string):
                break
            element = string[startPos:substrLen + startPos]
            if element[0].lower() in "aeiou":
                scoreVowels += 1
            else:
                scoreConconants += 1

    if scoreVowels > scoreConconants:
        print("Kevin", scoreVowels)
    elif scoreVowels == scoreConconants:
        print("Draw")
    else:
        print("Stuart", scoreConconants)


if __name__ == '__main__':
    s = "BANANANAAAS"
    minion_game(s)
