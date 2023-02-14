def applesFriends(friends, apples):
    v1 = 0
    v2 = 0
    v3 = 0.0
    if friends > apples:
        if friends % apples == 0:
            v1 = friends // apples
            v2 = 0
        else:
            v1 = 0
            v2 = apples
            v3 = apples / friends
    elif friends == apples:
        v1 = 1
        v2 = 0
        v3 = 1
    else:
        if apples % friends == 0:
            v1 = apples // friends
            v2 = 0
            v3 =

    print(v1)
    print(v2)
    print(v3)

if __name__ == "__main__":
    friends = int(input().strip())
    apples = int(input().strip())
    applesFriends(friends, apples)




