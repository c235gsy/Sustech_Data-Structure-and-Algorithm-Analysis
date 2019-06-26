# 工作类型统计
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager
zhfont1 = matplotlib.font_manager.FontProperties(fname='/Library/Fonts/Songti.ttc')




def get_name_and_data():
    filename = "./Project.xls"
    data = pd.ExcelFile(filename).parse(0)
    return data


student = get_name_and_data()[0:113]
work = list(student["工作单位"].dropna())
work_sta = dict(pd.value_counts(work))
print(work)
print(work_sta)


fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
data = [float(i) for i in work_sta.values()]
ingredients = [n for n in work_sta.keys()]


def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%\n({:d})".format(pct, absolute)


wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),textprops=dict(color="w"))
ax.legend(wedges, ingredients,title="Ingredients",loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1),prop=zhfont1)
print(help(ax.legend))
plt.setp(autotexts, size=8, weight="bold")
ax.set_title("Working Type Statistics")
plt.show()