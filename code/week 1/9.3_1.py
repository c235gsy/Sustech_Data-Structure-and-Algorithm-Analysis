line = input("We usally use y=kx+b to define a line, please give me the k. if k does not exist, please input \"non\":   ")
point = input("I want to a point,please give me like x,y    ")

if "non" in line:
    point = (point.strip ().split (","))
    print ("The vertical line perpendicular to that line at that point: y=" + str (point[1]))

else:
    k = float (line.strip ())
    point = (point.strip ().split (","))
    x0 = float (point[0])
    y0 = float (point[1])
    if k != 0:
        new_k = -1 / k
        new_b = x0 / k + y0
        print ("The vertical line perpendicular to that line at that point: y=" + str (new_k) + "x+" + str (new_b))
    if k == 0:
        print ("The vertical line perpendicular to that line at that point: x=" + str (x0))