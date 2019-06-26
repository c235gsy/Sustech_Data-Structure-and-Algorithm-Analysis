# 8.预期月薪统计（以 k 为单位）
import pandas as pd
import matplotlib.pyplot as plt


def get_name_and_data():
    filename = "./Project.xls"
    data = pd.ExcelFile(filename).parse(0)
    return data


def check(value):
    if value > 100:
        return value/1000
    else:
        return value


student = get_name_and_data()[0:113]
print(student)
salary = student["月薪"].dropna()
salary = list(map(check, salary))
print(salary)


count = [0,0,0,0,0,0]
for s in salary:
    if s >= 50:
        count[5] += 1
    else:
        count[int(s//10)] += 1
        print (s,end=" : ")
        print (int(s//10))

print(count)


width = 0.2

x = [i for i in range(6)]
y = count

plt.rcdefaults()
fig, ax = plt.subplots()
ax.barh(x, y, align='center',color='green', ecolor='black')
ax.set_yticks(x)
ax.set_yticklabels(["0<=s<10", "10<=s<20", "20<=s<30", "30<=s<40", "40<=s<50", "s>=50"])
ax.invert_yaxis()
ax.set_xlabel('Number of Student')
ax.set_ylabel('Range of Salary\nunit: K')
ax.set_title('Excepted Salary Distribution')

plt.show()

