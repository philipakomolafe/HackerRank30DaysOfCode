#DAY-5 OF HACKERRANK 30 DAYS CHALLENGE..
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n in (list(range(2,21))):
        for i in list(range(1,11)):
            print(f"{n} * {i} = {n * i}")
    else:
        sys.exit()