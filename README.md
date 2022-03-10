# Mr. Driller
rewrite the famous PlayStation game "Mr Driller". <br>
改编著名电子游戏《钻地先生》
## 1. Project Overview
"Early Days" is an entertainment company specialized in in all times video games classic revivals. It
wants now to rewrite the famous PlayStation game "Mr Driller". This game was originally developed
and published by Namco company.`<br>
Your team is in competition with several subcontractors to do the development, the best project will
win the contract.<br>
You are free to use whichever language/library you want, such as Python/Pygame or C/SDL, and your
game **must run on the three major platforms**: Linux, Windows and Mac OS X.
## 2. Functional Expression需求分析
### 2.1 游戏描述
Mr Driller is a 2D puzzle game. The player controls a driller and has several levels to achieve. The main 
goal of each level is to dig untill its depth without lacking air or being crashed by a falling block.
### 2.2 游戏规则
##### 2.2.1 移动和动作
**移动** ：左右键移动；上键跳跃：脚下为空时匀速下落<br>
**动作** : 移动方向上有障碍物时，根据砖块坚硬程度点击相应次数方向键
##### 2.2.2 砖块
**regular blocks:**<br>
有红色、蓝色、绿色或黄色的规则方块。<br>
1. 当玩家消灭其中一个方块时，他同时消灭相同颜色的相邻方块。它们上面的所有块都因重力而下落。<br>
2. 当正常的方块在钻完一些洞后掉下来时，它们会与相邻的相同颜色的方块合并并停止掉下来。如果至少有四个区块合并，它们就会消失<br>

**special blocks：**<br>
1. 棕色的需要5次钻击才能消失，必须一个一个钻。然而，它们在下降后合并，具有与常规块相同的消失性质。<br>
2. 白色的不会与其他相同颜色的块合并。<br>
3. 晶体在消失之前有很短的寿命。<br>
##### 2.2.3 空气
玩家拥有每秒减少1%的空气供给。开采一个棕色区块空气减少20%。<br>
玩家可以收集空气胶囊，增加20%的空气供给。
##### 2.2.4 分数
合并后消除或消除的每个砖块都会带来分数。
玩家还可以通过收集空气胶囊来提高分数。<br>
他最终在完成一个关卡后获得奖励。
##### 2.2.5 生命，输/赢
如果供气降至零，或者司钻被掉落的石块砸到，玩家将失去生命，并在完全供气的情况下在相同的深度重新启动。<br>
当玩家失去三条命时，游戏就结束了。如果他完成了所有的关卡，他就赢了。
### 2.3 需要实现的功能
##### 2.3.1 等级
游戏必须拥有至少10个不同的关卡。前面部分中描述的所有元素都必须存在。<br>
每一层的深度将逐渐增加，同时空气胶囊的数量将减少。<br>
不同类型的块会随机生成。
##### 2.3.2 score
计算与实时显示玩家积分，并拥有查看积分榜单的功能。
##### 2.3.3 暂停
玩家可以在游戏中随时暂停。
## 3. 技术实现
### 开发环境 The Development Environment
**1. PyCharm python IDE**<br>
_First_, PyCharm has the features of a general IDE, such as debugging, syntax highlighting, Project management, code jumping, smart prompting, auto completion, unit testing, version control.<br>
_In addition_, PyCharm also provides some great features for Django development, while supporting Google App Engine, and even more cool, PyCharm supports IronPython.<br>
**2. Python 3.6**
### 图像引擎与使用的模块
**Image engine： Pygame**<br>
Contains images and sounds. Built on SDL, it allows real
time video game
development without being tied to low level languages such as machine language
and assembly language.
##### 1.1 pygame graphics interface 
Images can be read and saved using the
pygame.image module. Use pygame.image.load to read the image file.
Support
format JPEG 、 PNG 、 GIF 、 BMP 、 PCX 、 TGA 、 TIF 、
LBM,PBM 、 XPM
##### 1.2 pygame Drawing 
In addition to blit the pre drawn picture to the
Surface, you can also draw some simple graphics on the Surface, such as
points, lines, squares, circles, etc. This feature is mainly done by the
**pygame.draw**module. <br>
`surface = pygame.display.set_mode((640, 480))//Draw the canvas
pygame.draw.rect(surface, (0,0,255), (100, 200, 100, 100))//Draw a rectangle`
##### 1.3 pygame Write 
Need to import the pygame.fontNeed to import the **pygame.font** module and initialize module and initialize itit
<br>
`import pygame.fontpygame.font.init()`
##### 1.4 其他模块

1. sys：
2. pygame<br>
⚫ pygame.locals<br>
⚫ pygame.sprite<br>
⚫ pygame.display<br>
3. json <br>
◆ json.loads<br>
◆ json.dumps: Used to encode Python objects into JSON strings<br>
4. random
### 游戏工作流程
![image](https://github.com/yaojia1/teamwork/IMG/workfolw.png)
### 代码结构
![image](https://github.com/yaojia1/teamwork/IMG/structure.png)
### 主引擎工作流程
![image](https://github.com/yaojia1/teamwork/IMG/engine.png)
### 内容介绍
The following introduction to functions is to classify functions according to different
documents.
##### 1， elements. py
1. save (name, Save game data (including player name, grade) to a file
for storage
1. startpage (screen,x,y,event, Generate a start interface
1. endpage (screen,x,y,event,m,n,i,p, Receive the score data, apply for
the name, complete the grade, and generate the end screen.
##### 2， pages.py
1. foo(var) Return the image address according to the var value.<br>
2. Brick<br>
2.1 Brick.init: Implement brick initialization<br>
2.2 Brick.fall: Achieve fall<br>
2.3 Brick.melt: Grouping adjacent bricks of the same color<br>
3. Meltgroupadd<br>
3.1 Meltgroupadd .__init__: Create a new sprite group<br>
3.2 Meltgroupadd . Add a brick to the group<br>
4. Map<br>
4.1 Map.__init__: 初始化全部图形<br>
4.2 Map.changemap: 升级换地图<br>
5. Drillers (pygame.sprite.Sprite).<br>
5.1 M ove Achieve character movement<br>
5.2 F all Realize the gravity drop of the character<br>
5.3 U pdata : Update character status<br>
6. mergebrick ( Realize the elimination and fusion of brick groups
7. drillbrick ( Remove the bricks that have been dug
8. levelup High rise
