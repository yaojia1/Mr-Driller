import pygame
import random
import sys
from pygame.font import *
pygame.init()
my_font = pygame.font.SysFont("arial", 40)
if not pygame.font: print('Warning, fonts disabled')
allblock=0
meltgroup=[]
BRICKG = [[] for i in range(40)]

def foo(var):
    # red, blue, green or yellow普通

    # brown,white, crystal
    return {
        'red':"red.png",
        'blue': "blue.png",
        'green': "green.png",
        'yellow':"yellow.png",
        'brown':"brown.png",
        'white':"white.png",
        'crystal':"crystal.jpg",
        'air':"air.png",
        'drill':"driller.png"
    }.get(var,'error')

class Brick(pygame.sprite.Sprite):
    _width = 15
    _height = 15
    sta=0#可以fall
    stoptime=0
    fuck=0#到底了为1
    fallingsingle=1
    def ttime(self,tics):
        if tics>=1:
            self.stoptime-=1
    def __init__(self,putimage):
        super().__init__()#调用父类的初始化方法
        self.mel=0
        global allblock
        allblock+=1
        #随机判断放哪一个图，标记序数得到iimage
        self.color=putimage#一个数，一会修改
        self.image = pygame.image.load(foo(putimage))#写一个函数判断放哪一个图片
        self.rect = self.image.get_rect()
        if putimage=="brown":
            self.life=5
        else:self.life=2
    def fall(self,tics):
        if self.color == "crystal" :
            if self.stoptime > 0:
                self.ttime(tics)
                return 0  # 两秒后stoptime=-0.1
            if self.stoptime < 0:
                print("透明色消除")
                drillbrick(self)
                return 0
        if self.rect.top>=2200-dril1.level:#到底了
            #self.sta=1
            self.fuck=1
            if self.mel!=1 and self.mel!=0:
                for lala in self.mel.mapn:
                    #lala.sta=1
                    lala.fuck=1
            return 0
        if self.fuck==1:return 0 #到底了
        if self.mel:
            if self.mel == 1:
                if self.fuck:
                    for grrr in meltgroup:
                        if pygame.sprite.Group.has(grrr.mapn, self):
                            for bbb in grrr.mapn:bbb.fuck=1
                            return 0
                return 0
            else:
                gg = self.mel  # 找到尊在的那个组
            if gg.fallable==0:#正在下落不能打扰
                kll=0
                gg.statu+=1
                for sss in gg.mapn:
                    '''压死driller'''
                    if sss.rect.top + 5 <= dril1.rect.top <= sss.rect.top + 50:
                        if sss.rect.left <= dril1.rect.left + 16 <= sss.rect.left + 50:
                            dril1.life -= 1
                            dril1.air = 100
                            dril1.rect.top, dril1.rect.left = 200, 250
                            for br in map1.brickGroup:
                                br.rect.top += dril1.level
                            dril1.level = 0
                    sss.sta+=1
                    sss.rect.top += 2
                if (sss.rect.top+dril1.level) % 50 == 0:
                    kll = 1         # 下落到50倍数了
                if kll:
                    '''失败尝试
                    for sss in gg.mapn:
                        x=sss.rect.left//50
                        y=sss.rect.top//50
                        if y==0:continue
                        if BRICKG[y-1][x]==sss:
                            BRICKG[y - 1][x] = 0
                        BRICKG[y][x] = sss'''
                    gg.fallable=1#可判断是否下咯
                return 0
            else:
                fall123=1#融合在fall
                for spr in gg.mapn:  # 组里的每一个石块
                    '''原方案：'''
                    if spr.rect.top+25 < self.rect.top and spr.rect.left==self.rect.left: continue
                    test_list = pygame.sprite.spritecollide(spr, map1.brickGroup, False)  # spr相交的石块
                    for ll in test_list:  # 查看有没有托
                        if pygame.sprite.Group.has(gg.mapn, ll):
                            continue
                        if ll.rect.top >= spr.rect.top+50 and ll.rect.left == spr.rect.left:  # 掉不下去
                            return 0

                    '''失败尝试
                    x=spr.rect.left//50
                    y = spr.rect.top//50
                    if y >= 39:continue
                    if BRICKG[y+1][x]:
                        if BRICKG[y+1][x].color == spr.color:continue
                        else:return 0#掉不下去'''
                for sss in gg.mapn:
                    sss.rect.top += 2
                gg.fallable = 0#没找到托，正在下落
                gg.statu+=1
                return 0
        #if融合
        '''原单个、压住了:'''
        collide_list = pygame.sprite.spritecollide(self, map1.brickGroup, False)
        for sp in collide_list:
            if  self.rect.left==sp.rect.left:
                if sp.rect.top == self.rect.top + 50:#压住了
                    self.melt()
                    self.fallingsingle=1
                    return 0
        '''失败尝试。单个是否压住
        x = self.rect.left // 50
        y = self.rect.top // 50
        if self.rect.top%50==0 and self.fallingsingle==0:
            
            if y >= 39: return 0
            if BRICKG[y + 1][x]:
                BRICKG[y][x]=self
                if y==0:pass
                else:
                    if BRICKG[y-1][x]==self:
                        BRICKG[y - 1][x] =0
                self.melt()
                self.fallingsingle = 1
                return 0'''
        if self.stoptime==0:
            if self.rect.top + 5 <= dril1.rect.top <= self.rect.top + 50:
                if self.rect.left <= dril1.rect.left + 16 <= self.rect.left + 50:
                    dril1.life -= 1
                    dril1.air=100
                    dril1.rect.top, dril1.rect.left = 200, 250
                    for br in map1.brickGroup:
                        br.rect.top += dril1.level
                    dril1.level = 0
            self.rect.top += 2
            self.fallingsingle=0
            self.sta +=1
    def melt(self):
        if self.color=='white':
            return 0
        if self.mel:return 0
        collide_list = pygame.sprite.spritecollide(self,map1.brickGroup, False)
        for sp in collide_list:
            if sp.color == self.color:
                if sp.fallingsingle==0:continue
                rel=0
                if sp.rect.left + 50 == self.rect.left or sp.rect.left - 50 == self.rect.left :
                    if sp.rect.top==self.rect.top:rel=1
                if sp.rect.top==self.rect.top+50 or sp.rect.top==self.rect.top-50:
                    if sp.rect.left  == self.rect.left:rel=1
                if rel and sp.mel==0:
                        if self.mel:
                            self.mel.aadd(sp)
                            sp.mel = 1
                        else:
                            self.mel = Mapnn(self)  # 一个对象
                            sp.mel = 1
                            self.mel.aadd(sp)
                            meltgroup.append(self.mel)

    def update(self,tics):
        self.fall(tics)

class Mapnn():
    stopp=1
    fallable=1
    def __init__(self,ga):
        self.mapn = pygame.sprite.Group()
        self.mapn.add(ga)
        self.color=ga.color
        self.statu=ga.sta#264
        self.num=1
    def aadd(self,gb):
        self.mapn.add(gb)
        gb.mel=1
        self.num+=1
        self.statu+=gb.sta

class Map():
  def __init__(self):
      # 初始化砖块群组
      self.brickGroup=pygame.sprite.Group()

      XY = [(x,y) for x in range(11) for y in range(40)]#53，206
      for x,y in XY:
              # 实例化砖块类对象
              self.brick=Brick(random.choice(['red','blue','green','yellow','brown','white','crystal','air']))
              # 生砖块的位置
              self.brick.rect.left,self.brick.rect.top=3+x*50,250+y*50# 每循环一次自动将动画添加到精灵组（下同）
              self.brickGroup.add(self.brick)
              print(y)
              BRICKG[y].append(self.brick)
class Drillers(pygame.sprite.Sprite):
    life=3
    level=0
    air=100
    image = pygame.image.load(foo('drill'))
    rect = image.get_rect()
    score=0

    def __int__(self):
        pygame.sprite.Sprite.__init__(self)
    def move(self,speedx,speedy):#输入pygame.event.get
        if self.rect.left<=0 and speedx<0:speedx=0
        if self.rect.left>=518 and speedx>0:speedx=0
        self.rect.left+=speedx
        self.rect.top+=speedy
    def fall(self):#修改
        collide_list = pygame.sprite.spritecollide(self, map1.brickGroup, False)
        self.speed=2
        for sp in collide_list:
            if self.rect.top+38<=sp.rect.top<=self.rect.top+41 :#下接触了
                if sp.rect.left - 32 < self.rect.left < sp.rect.left + 50:
                    self.rect.top=sp.rect.top-39
                    self.speed=0
                    return 0
            #else:
             #   if sp.rect.left + 50 > self.rect.left > sp.rect.left + 25: self.rect.left = sp.rect.left  # 排左
              #  if sp.rect.left < self.rect.left + 32 < sp.rect.left + 25: self.rect.left = sp.rect.left - 32  # 排右
                #self.rect.top=sp.rect.top-39
        if self.rect.top + self.level >= 2210:return 0
        self.rect.top+=self.speed
    def update(self):
        self.fall()
        if self.rect.top+self.level>=2210:print("WIN")

    #def dill(self)#棕色的氧气减20%
    #def collect(self):#air+20%



def mergebrick(tics):
    ii=0
    for spp in meltgroup:  #融合的石块
        pengsp=pygame.sprite.groupcollide(spp.mapn,map1.brickGroup,False,False)
        for keys in pengsp.keys():
            for jiaocha in pengsp[keys]:  # 小于4
                if pygame.sprite.Group.has(spp.mapn, jiaocha):continue
                else:
                    aaa=0
                    if spp.color == jiaocha.color:#是否可以融合
                        for bb in spp.mapn:
                            if bb.rect.top == jiaocha.rect.top:
                                if bb.rect.left + 50 == jiaocha.rect.left or bb.rect.left - 50 == jiaocha.rect.left:
                                    aaa=1
                            if bb.rect.left == jiaocha.rect.left:
                                if bb.rect.top == jiaocha.rect.top + 50 or bb.rect.top == jiaocha.rect.top - 50:
                                    aaa=1
                    if aaa:#可以融合
                        if jiaocha.mel:#两个组
                            tt=0
                            if jiaocha.mel == 1:
                                tt = 0
                                for gg in meltgroup:
                                    if pygame.sprite.Group.has(gg.mapn, jiaocha):
                                        break
                                    tt+=1
                                print("111111")
                            else:
                                print("222222222222")
                                gg=jiaocha.mel
                                tt = 0
                                for sss in meltgroup:
                                    if sss == gg: break
                                    tt += 1
                            spp.statu+=gg.statu
                            for g in gg.mapn:
                                spp.aadd(g)
                            gg.mapn.empty  # 清空
                            gg.color = 0
                            meltgroup.pop(tt)
                            print("两个组融合@@@@@@@@@@@@@@@@@@@@@@@",tt,gg.statu,meltgroup)
                            return 0
                        else:#单个的
                            if jiaocha.fallingsingle==0:continue
                            spp.aadd(jiaocha)
        if spp.num >= 4:  # 大于4
            # if spp.statu == 0: continue
            if spp.color == "crystal" :
                for bbb in spp.mapn:
                    if bbb.mel!=1:
                        if bbb.stoptime!=0:pass
                        else:
                            bbb.stoptime=2.5
                            print("透明色数量：", spp.num)
            for yichu in spp.mapn:
               map1.brickGroup.remove(yichu)
            dril1.score += spp.num
            spp.mapn.empty  # 清空
            print(dril1.score)
            meltgroup.pop(ii)
        ii+=1

'''
def mergedisappear(megroup,i):
       if spp.num >= 4:  # 大于4
           # if spp.statu == 0: continue
           if spp.color == "crystal" :
               for bbb in spp.mapn:
                   if bbb.mel!=1:
                       if bbb.stoptime!=0:pass
                       else:
                           bbb.stoptime=2.5
                           print("透明色数量：", spp.num)
           for yichu in spp.mapn:
               map1.brickGroup.remove(yichu)
           dril1.score += spp.num
           spp.mapn.empty  # 清空
           print(dril1.score)
           meltgroup.pop(i)

'''
def drillbrick(sp):
    if sp.life > 0:
        sp.life -= 1
    else:
        if sp.color == "brown":
            dril1.air -= 20
        if sp.mel!=0:
            ssss = 0
            for gro in meltgroup:
                if pygame.sprite.Group.has(gro.mapn, sp):
                    if sp.color == "air":
                        dril1.air += 20 * gro.num
                    for yichu in gro.mapn:
                        map1.brickGroup.remove(yichu)
                    dril1.score += gro.num
                    gro.mapn.empty  # 清空
                    print(dril1.score)
                    meltgroup.pop(ssss)
                    return 0
                ssss += 1
        if sp.color=="air":
            dril1.air+=20
        map1.brickGroup.remove(sp)

def levelup():
    if dril1.rect.top>=310:
        for gr in map1.brickGroup:
            gr.rect.top -= 2
        dril1.rect.top -= 2
        dril1.level += 2
    if dril1.rect.top<200:
        for gr in map1.brickGroup:
            gr.rect.top += 2
        dril1.rect.top += 2
        dril1.level -= 2

map1=Map()
dril1=Drillers()
dril1.rect.left,dril1.rect.top=250,200
