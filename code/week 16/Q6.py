# (6) 工作目标城市统计，是否回家乡？
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager
zhfont1 = matplotlib.font_manager.FontProperties(fname='/Library/Fonts/Songti.ttc')


def get_name_and_data():
    filename = "./Project.xls"
    data = pd.ExcelFile(filename).parse(0)
    return data


student = get_name_and_data()[0:113]
#print(student)
choice = student[["省", "市", "工作省份", "工作城市"]].dropna(how='any')
#print(choice)

provence = [p.strip().replace("省", "") for p in choice["省"]]
city = [p.strip().replace("市", "") for p in choice["市"]]
work_provence = [p.strip().replace("省", "") for p in choice["工作省份"]]
work_city = [p.strip().replace("市", "") for p in choice["工作城市"]]

N = len(provence)
infor = {}

for c in set(work_city):
    infor[c] = [0, 0, 0]
    # (非家乡，同省不同市，同市)

for i in range(N):
    if provence[i] != work_provence[i]:
        infor[work_city[i]][0] += 1
    else:
        if city[i] != work_city[i]:
            infor[work_city[i]][1] += 1
        else:
            infor[work_city[i]][2] += 1

city = list(set(work_city))
no_cp = [infor[c][0] for c in city]
p_no_c = [infor[c][1] for c in city]
cp = [infor[c][2] for c in city]
width = 0.2
ind = [i for i in range(len(city))]
print(city)
p1 = plt.bar(ind, no_cp, width)
p2 = plt.bar(ind, p_no_c, width, bottom=no_cp)
p3 = plt.bar(ind, cp, width, bottom=[no_cp[i]+p_no_c[i] for i in range(len(city))])
plt.ylabel('Students Number')
plt.yticks(range(0, 16, 2))
plt.title('Progression of Students ')
plt.xticks(ind, city, fontproperties=zhfont1)
#plt.xticks(ind, ('Guang Zhou', 'Shen Zhen', 'Chang Sha', 'Nan Jing', 'Fu Zhou'))
plt.legend((p1[0], p2[0], p3[0]), ('Did not Back', 'Home-provence', 'Home-city'))

plt.show()


