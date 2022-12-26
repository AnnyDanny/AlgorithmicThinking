def descending_order(num):
    numToStr = str(num)
    numToList = list(numToStr)

    for i in range(len(numToList) - 1):
        for j in range(len(numToList) - 1):
            if numToList[j] < numToList[j + 1]:
                temp = numToList[j + 1]
                numToList[j + 1] = numToList[j]
                numToList[j] = temp
                if j == len(numToList) - 1:
                    break
    return numToList

if __name__ == "__main__":
    num = int(input().strip())
    print(descending_order(num))



