
def devided(reverse, lenght):
    expandad_list = []
    zero_num = lenght - 1

    for i in range(lenght):
        n = reverse[i] * (10**zero_num)
        if n != 0:
            expandad_list.append(str(n))
        zero_num -= 1
    return expandad_list

def expanded_number(number):
    res = 0
    value = []
    lenght = len(str(number))
    str_expanded = ""

    for i in range(lenght):
        res = int(number % 10)
        value.append(res)
        number = number / 10

    reverse = reversed(value)
    expandad_list = devided(list(reverse), lenght)
    str_expanded = " + ".join(expandad_list)
    return str_expanded

if __name__ == "__main__":
    number = int(input())
    print(expanded_number(number))