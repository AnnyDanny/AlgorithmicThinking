def count_number(numbbin):
    counter = 0
    strbin = str(numbbin)

    for i in strbin:
        if i == "1":
            counter += 1
    return counter

def count_bits(n):
    numbbin = bin(n).replace("0b", "")
    counter = count_number(numbbin)
    return counter

if __name__ == "__main__":
    n = int(input().strip())
    print(count_bits(n))