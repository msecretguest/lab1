import random

a = int(input("input (start) a: "))
b = int(input("input (end) b: "))
p = random.randint(a, b)
c = int(input("input c: "))
i = 0
while i < 100000:
    if c > p:
        print("Input lower number")
        c = int(input("input c: "))
    if c < p:
        print("Input higher number")
        c = int(input("input c: "))
    if c == p:
        i = 100000000
    i += 1
    break

print("U ARE WIN")
