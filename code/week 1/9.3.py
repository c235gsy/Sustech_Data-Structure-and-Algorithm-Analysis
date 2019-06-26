a = "1525"*40
b = "2515"*40
a = a.lstrip("0")
b = b.lstrip("0")
length = max([len(a), len(b)])
a = "0"*(1+length-len(a))+a
b = "0"*(1+length-len(b))+b
a = list(map(int, list(a)))
b = list(map(int, list(b)))
c = list(map(int, list("0"*(len(a)))))
ab = list(map(int, list("0"*(len(a)))))
for i in range(1, len(a)):
    x = a[-i]
    y = b[-i]
    z = c[-i]
    if x+y+z < 10:
        ab[-i] = x+y+z
    if x+y+z >= 10:
        ab[-i] = x+y+z-10
        c[-i-1] += 1
print("".join(list(map(str, ab))).lstrip("0"))


