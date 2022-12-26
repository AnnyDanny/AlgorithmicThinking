def break_camel_case(s):
    strBreak = ""

    for letter in s:
        if letter.isupper():
            strBreak += " "
        strBreak += letter
    return strBreak



if __name__ == "__main__":
    s = input().strip()
    print(break_camel_case(s))