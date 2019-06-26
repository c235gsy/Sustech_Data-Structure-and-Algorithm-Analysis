# 国内外升学硕士和博士意愿比较
import pandas as pd
import matplotlib.pyplot as plt


def get_name_and_data():
    filename = "./Project.xls"
    data = pd.ExcelFile(filename).parse(0)
    return data


student = get_name_and_data()[0:113]
print(student)
choice = student[["毕业去向", "深造学位"]].dropna(how='any')
quxiang = list(choice["毕业去向"])
xuewei = list(choice["深造学位"])

out_m=0
out_p=0
in_m=0
in_p=0

print(quxiang)
print(xuewei)
for i in range(len(quxiang)):
    if quxiang[i] == "国内读研":
        if xuewei[i] == "硕士":
            in_m += 1
        else:
            in_p += 1
    else:
        if xuewei[i] == "硕士":
            out_m += 1
        else:
            out_p += 1

print(out_p,out_m,in_m,in_p)
# ('top', 'bottom', 'center', 'baseline', 'center_baseline')
width = 0.2
ind = [0, 1]
master = [in_m, out_m]
phd = [in_p, out_p]
p1 = plt.bar(ind, master, width)
p2 = plt.bar(ind, phd, width, bottom=master)
plt.ylabel('Students Number')
plt.title('Progression of Students ')
plt.xticks(ind, ("Domestic", "Oversea"))
plt.legend((p1[0], p2[0]), ('Master', 'Phd'))

plt.text(0, in_m/2, in_m, ha='center', va='center', fontsize=10.5)
plt.text(1, out_m/2, out_m, ha='center', va='center', fontsize=10.5)
plt.text(0, in_m+in_p/2, in_p, ha='center', va='center', fontsize=10.5)
plt.text(1, out_m+out_p/2, out_p, ha='center', va='center', fontsize=10.5)
plt.text(0, in_p+in_m, in_p+in_m, ha='center', va='bottom', fontsize=10.5)
plt.text(1, out_m+out_p, out_m+out_p, ha='center', va='bottom', fontsize=10.5)

plt.show()