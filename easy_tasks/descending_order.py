def descending_order(num):
    strnum = str(num)
    listnum = list(strnum)

    for i in range(len(listnum) - 1):
        if listnum[i + 1] < listnum[i]:
            temp = listnum[i]
            listnum[i] = listnum[i + 1]
            listnum[i + 1] = temp
    return listnum

if __name__ == "__main__":
    num = int(input().strip())
    print(descending_order(num))
