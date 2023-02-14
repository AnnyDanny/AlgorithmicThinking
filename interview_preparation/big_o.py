import timeit


def sum1(n):
    final_sum = 0
    for x in range(0, n + 1):
        final_sum += x

    return final_sum

def sum2(n):
    return int((n * (n + 1) / 2))

if __name__ == "__main__":
    print(sum1(10))
    
    print(sum2(10))