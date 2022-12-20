import math
import os
import random
import re
import sys

def odd_even_weird(n):
    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and n >= 2 and n <= 5:
        print("Not Weird")
    elif n % 2 == 0 and n >= 6 and n <= 20:
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")

if __name__ == '__main__':
    n = int(input().strip())
    odd_even_weird(n)
