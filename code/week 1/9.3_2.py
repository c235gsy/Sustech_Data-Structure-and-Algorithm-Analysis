point1 = input("Please give me the first point of the line as x,y    ")
point2 = input("Please give me another point of the line as x,y    ")
point1 = list(map(float, point1.strip().split(",")))
point2 = list(map(float, point2.strip().split(",")))
x1 = point1[0]
y1 = point1[1]
x4 = point2[0]
y4 = point2[1]
x3 = x1/3 + 2*x4/3
y3 = y1/3 + 2*y4/3
x2 = x4/3 + 2*x1/3
y2 = y4/3 + 2*y1/3
print("\nNow I can split the line into three parts:   \n")
print("Part1:   between the point ("+str(x1)+","+str(y1)+") and ("+str(x2)+","+str(y2)+")")
print("Part2:   between the point ("+str(x2)+","+str(y2)+") and ("+str(x3)+","+str(y3)+")")
print("Part3:   between the point ("+str(x3)+","+str(y3)+") and ("+str(x4)+","+str(y4)+")")