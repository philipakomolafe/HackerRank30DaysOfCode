#DAY3 OF HACKERRANK_30_DAYS_CHALLENGE

n = int(input().strip())
numbers = list(range(1, 101))
if (n in numbers) & ((n % 2) != 0):
    print(f"{n} is weird")
elif (n % 2 == 0) & (n in numbers[1:5]):
    print("Not Weird")
elif (n % 2 == 0) & (n in numbers[5:20]):
    print("Weird")
elif (n % 2 == 0) & (n in numbers[20:]):
    print("Not Weird")