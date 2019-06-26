
from tkinter import *
root = Tk()

#创建三个label 分别显示 red blue yellow
#注意三个Label 的大小, 他们均与文本的长度有关
Label(root,
      text='red',
      bg='red'
      ).pack()
Label(root,
      text='blue',
      bg='blue'
      ).pack()
Label(root,
      text='yellow',
      bg='yellow'
      ).pack()
#再创建三个Label与上次不同的是这三个Label 均使用width 和heigth属性
Label(root,
      text='red',
      bg='red',
      width=10,
      height=3
      ).pack()
Label(root,
      text='blue',
      bg='blue',
      width=10,
      height=3
      ).pack()
Label(root,
      text='yellow',
      bg='yellow',
      width = 10,
      height = 3
      ).pack()

root.mainloop()

