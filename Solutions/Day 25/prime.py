# Enter your code here. Read input from STDIN. Print output to STDOUT
import math


def isPrime(number):
    if number == 1:
        return "Not prime"
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return "Not prime"
    return "Prime"


for i in range(int(input())):
    number = int(input())
    print(isPrime(number))
