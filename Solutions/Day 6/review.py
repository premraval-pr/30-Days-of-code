# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    word = input()
    solution = ""
    for letter in word[::2]:
        solution += letter
    solution += " "
    for letter in word[1::2]:
        solution += letter
    print(solution)
