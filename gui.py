from tkinter import *
import random

import pandas as pd
import numpy as np
import turtle
import time
from PIL import Image, ImageTk


def back():
    turtle.tracer(False)
    turtle.penup()
    turtle.home()
    turtle.goto(-100, 0)
    turtle.left(90)
    turtle.pendown()

data = pd.read_csv('sites.csv', usecols=['x', 'y'])
data = np.array(data)
x = [row[0] for row in data]
y = [row[1] for row in data]

turtle.screensize(800, 600)
turtle.speed(10)
turtle.hideturtle()
turtle.tracer(False)
turtle.penup()
turtle.goto(-100,150)
turtle.pendown()
turtle.forward(300)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(300)
turtle.penup()
turtle.goto(-150, -50)
turtle.pendown()
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.penup()
turtle.goto(150, 150)
turtle.pendown()
turtle.left(90)
turtle.forward(300)
back()
for i in range(len(x)):
    turtle.goto(x[i]+50,y[i])
    back()
time.sleep(0.01)

ts = turtle.getscreen()
ts.getcanvas().postscript(file="finall.eps")
# im = Image.open("finall.eps")
# im.save("finall.jpg", "JPEG")


'''import matplotlib.pyplot as plt
from PIL import ImageTk,Image


data = pd.read_csv('sites.csv', usecols=['x', 'y'])
data = np.array(data)
x = [row[0] for row in data]
y = [row[1] for row in data]

plt.figure()
#plt.xticks(np.linspace(-5,30,7))
#plt.yticks(np.linspace(-15,15,6))
ax = plt.gca()  # 获取当前坐标的位置
# 指定坐标的位置
ax.xaxis.set_ticks_position('both')  # 设置bottom为x轴
ax.yaxis.set_ticks_position('left')  # 设置left为y轴
ax.spines['bottom'].set_position(('data', 0))  # 这个位置的括号要注意
ax.spines['left'].set_position(('data', 0))
plt.axis('off')  # 去掉坐标轴
plt.plot([x,y])
#plt.show()
plt.savefig("line.jpg")

'''
'''def traverse_imgs(writer, images):
    # 遍历所有图片，并且让writer抓取视频帧
    for img in images:
        plt.imshow(img)
        writer.grab_frame()
        plt.pause(0.01)
        plt.clf()


if __name__ == '__main__':
    # 创建video writer, 设置好相应参数，fps
    metadata = dict(title='01', artist='Matplotlib', comment='depth prediiton')
    writer = FFMpegWriter(fps=10, metadata=metadata)

    # 读出自己的所有图片
    images = ....

    figure = plt.figure(figsize=(10.8, 7.2))
    plt.ion()  # 为了可以动态显示
    plt.tight_layout()  # 尽量减少窗口的留白
    with writer.saving(figure, 'out.mp4', 100):
        traverse_imgs(writer, images)
'''


root = Tk() # 创建窗口对象
root.geometry("1980x1020+0+0", )
root.title("声源定位跟踪系统")   # 设置窗口标题

sites = ['AB距离：                         {}'.format(0.1),
         '角度：                             {}'.format(0.1),
         'X:                                  {:.5}'.format(x[0]),
         'Y:                                  {:.5}'.format(y[0])]
labels = range(4)
for i in range(4):
   ct = [random.randrange(256) for x in range(3)]
   brightness = int(round(0.299*ct[0] + 0.587*ct[1] + 0.114*ct[2]))
   ct_hex = "%02x%02x%02x" % tuple(ct)
   bg_colour = '#' + "".join(ct_hex)
   l = Label(root,
                text=sites[i],
                ) # fg='White' if brightness < 120 else 'Black', bg=bg_colour
   l.place(x = 100, y = 30 + i*80, width=360, height=50)

bottons = ["声源定位", "声源指示", "动态追踪"]
labels = range(3)
for i in range(3):
   ct = [random.randrange(256) for x in range(3)]
   brightness = int(round(0.299*ct[0] + 0.587*ct[1] + 0.114*ct[2]))
   ct_hex = "%02x%02x%02x" % tuple(ct)
   bg_colour = '#' + "".join(ct_hex)
   l = Button(root,
                text=bottons[i],
                ) # fg='White' if brightness < 120 else 'Black', bg=bg_colour
   l.place(x = 100, y = 400 + i*100, width=360, height=100)


# 显示自选的图片
img= Image.open("finall.eps")
img = img.resize((840, 840), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img, master=root)
imgLabel = Label(root, image=img)
imgLabel.place(x = 600, y = 0 , width=840, height=860)

'''img2 = Image.open("kuang.jpg")
img2 = img.resize((500,520), Image.ANTIALIAS)
img2 = ImageTk.PhotoImage(img, master=root)
imgLabel2 = Label(root,img2,alpha=0.7)
imgLabel2.place(x = 600, y = 20 , width=480, height=550)
'''

root.mainloop()

