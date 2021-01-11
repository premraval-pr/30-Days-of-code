# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
people = {}
for i in range(0, int(n)):
    name, number = input().split(" ")
    people[name] = number

while True:
    try:
        name = input()
    except EOFError:
        break
    if name in people.keys():
        print(name+"="+people[name])
    else:
        print("Not found")
