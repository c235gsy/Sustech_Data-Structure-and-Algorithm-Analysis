n = 200
start = n
Hail = []

while n != 1:
    if n % 2 == 0:
        Hail.append(int(n))
        n = n/2
    else:
        Hail.append(int(n))
        n = 3*n + 1
if n == 1:
    Hail.append(1)

print("\nthe Hailstone("+str(start)+"):")
print(Hail)
print("\nthe length of Hailstone("+str(start)+"):")
print(len(Hail))