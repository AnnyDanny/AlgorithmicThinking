def sort_array(source_array):
    dictEven = {}

    for i, v in enumerate(source_array):
        if v % 2 == 0:
            dictEven[i] = v

    return dictEven
    # sort_odds(dictOdd)


"""def sort_odds(dictOdd):
    for v in dictOdd.values():
        for k in dictOdd:
            if v """



if __name__ == "__main__":
    lst = [5, 8, 6, 3, 4]
    print(sort_array(lst))