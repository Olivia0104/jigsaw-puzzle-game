# jigsaw-puzzle-game
基于pygame实现的拼图游戏，运行环境：Spyder

实现了通过键盘按键选择不同难度的拼图游戏，通过鼠标点击移动拼图位置。

## 功能实现

#### 一、选择难度和图片

通过绑定点击事件，按‘A’键是四宫格，按‘B’键是三宫格，按‘C’键是二宫格，每次用于拼图的图片从images文件中通过random.choice()随机选出，界面大小就是图片的大小。

#### 二、打乱拼图并渲染到页面上

通过board列表记录每块拼图，去掉右下角的拼图，设置为空拼图（列表值为-1），通过200次随机的移动拼图，将拼图打乱，并确保可以恢复为原图，通过screen.blit()渲染到界面上。

#### 三、移动拼图

移动拼图时，记录鼠标点击的位置，计算出点击的是那个位置上的拼图，看这个位置上下左右有没有空拼图，若有，则将其列表值交换，记录现在空拼图的位置，将移动后的拼图情况渲染到界面上，若没有则无动作。

#### 四、拼图完成结束页面

每次移动拼图后会检查是否所有拼图返回了原位，一旦所有拼图都处于自己原来的位置，则显示结束页面，游戏结束。
