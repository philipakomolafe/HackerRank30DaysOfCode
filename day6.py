#DAY-6 OF HACKERRANK 30 DAYS CHALLENGE..

def print_even_odd_chars(s):
    """
    s = describe the input character.
    decription == here's a function that accepts any string character,
    returns the even-indexed chars, and returns the odd-indexed chars as well..
    """
    even_chars = ""
    odd_chars = ""

    for i in range(len(s)):
        if i % 2 == 0:
            even_chars += s[i]
        else:
            odd_chars += s[i]

    print(even_chars + " " + odd_chars)

#determine the number of test cases:
test_cases = int(input("Enter test-case range:. "))
for i in range(test_cases):
    s = input()
    print_even_odd_chars(s)