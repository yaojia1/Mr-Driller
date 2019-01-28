import pygame
import random
import sys
allblock=0
meltgroup=[]

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
    sta=1#可以fall
    stoptime=0
    fuck=0#到底了为1
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
        if self.rect.top>=550:#到底了
            self.sta=1
            self.fuck=1
            if self.mel!=1 and self.mel!=0:
                for lala in self.mel.mapn:
                    lala.sta=1
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
                for sss in gg.mapn:
                    sss.rect.top += 2
                    if sss.rect.top % 50 == 0:
                        kll = 1         # 下落到50倍数了
                if kll:
                    gg.fallable=1#可判断是否下咯
                return 0
            else:
                fall123=1#融合在fall
                for spr in gg.mapn:  # 组里的每一个石块
                    if spr.rect.top+25 < self.rect.top and spr.rect.left==self.rect.left: continue
                    test_list = pygame.sprite.spritecollide(spr, map1.brickGroup, False)  # spr相交的石块
                    for ll in test_list:  # 查看有没有托
                        if pygame.sprite.Group.has(gg.mapn, ll):
                            continue
                        if ll.rect.top >= spr.rect.top+50 and ll.rect.left == spr.rect.left:  # 掉不下去
                            return 0
                for sss in gg.mapn:
                    sss.rect.top += 2
                gg.fallable = 0#没找到托，正在下落
                return 0
        #if融合
        collide_list = pygame.sprite.spritecollide(self, map1.brickGroup, False)
        for sp in collide_list:
            if  self.rect.left==sp.rect.left:
                if sp.rect.top == self.rect.top + 50:#压住了
                    self.sta=1
                    return 0
        if self.stoptime==0:
            self.rect.top += 2
            self.sta = 0
    def melt(self):
        if self.color=='white':
            return 0
        if self.sta:return 0
        if self.mel:return 0
        collide_list = pygame.sprite.spritecollide(self,map1.brickGroup, False)
        for sp in collide_list:
            if sp.color == self.color:
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
        if self.rect.top%50==0:self.melt()

class Mapnn():
    stopp=1
    fallable=1
    def __init__(self,ga):
        self.mapn = pygame.sprite.Group()
        self.mapn.add(ga)
        self.color=ga.color
        self.num=1
    def aadd(self,gb):
        self.mapn.add(gb)
        gb.mel=1
        self.num+=1

class Map():
  def __init__(self):
      # 初始化砖块群组
      self.brickGroup=pygame.sprite.Group()

      XY = [(x,y) for x in range(4) for y in range(20)]
      for x,y in XY:
              # 实例化砖块类对象
              self.brick=Brick(random.choice(['red','blue','green','yellow','brown','white','crystal','air']))
              # 生砖块的位置
              self.brick.rect.left,self.brick.rect.top=3+x*50,600-y*50# 每循环一次自动将动画添加到精灵组（下同）
              self.brickGroup.add(self.brick)
      XY2 = [(x, y) for x in range(4,7) for y in range(6)]
      for x,y in XY2:
              # 实例化砖块类对象
              self.brick=Brick(random.choice(['red','blue','green','yellow','brown','white','crystal','air']))
              # 生砖块的位置
              self.brick.rect.left,self.brick.rect.top=3+x*50,600-y*50# 每循环一次自动将动画添加到精灵组（下同）
              self.brickGroup.add(self.brick)
      XY3 = [(x, y) for x in range(7,11) for y in range(20)]
      for x,y in XY3:
              # 实例化砖块类对象
              self.brick=Brick(random.choice(['red','blue','green','yellow','brown','white','crystal','air']))
              # 生砖块的位置
              self.brick.rect.left,self.brick.rect.top=3+x*50,600-y*50# 每循环一次自动将动画添加到精灵组（下同）
              self.brickGroup.add(self.brick)

class Drillers(pygame.sprite.Sprite):
    life=3
    air=100
    image = pygame.image.load(foo('drill'))
    rect = image.get_rect()
    score=0

    def __int__(self):
        pygame.sprite.Sprite.__init__(self)
    def move(self,speedx,speedy):#输入pygame.event.get
        if self.rect.left<=0 and speedx<0:speedx=0
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
        if self.rect.top>=560:return 0
        self.rect.top+=self.speed
    def update(self,event):
        self.fall()

    #def dill(self)#棕色的氧气减20%
    #def collect(self):#air+20%

def die(dril1):
    if dril1.air<=0:
        dril1.life-=1
        dril1.air=100
    if dril1.life==0:
        pygame.quit()
        sys.exit()

def mergebrick(tics):
    ii=0
    for spp in meltgroup:  #融合的石块
        pengsp=pygame.sprite.groupcollide(spp.mapn,map1.brickGroup,False,False)
        for keys in pengsp.keys():
            for jiaocha in pengsp[keys]:  # 小于4
                if pygame.sprite.Group.has(spp.mapn, jiaocha):
                    pass
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
                    if aaa:
                        if jiaocha.mel:#两个组
                            if jiaocha.mel == 1:
                                tt = 0
                                for gg in meltgroup:
                                    if pygame.sprite.Group.has(spp.mapn, jiaocha):
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
                            for g in gg.mapn:
                                spp.aadd(g)
                            gg.mapn.empty  # 清空
                            gg.color = 0
                            meltgroup.pop(tt)
                            print("两个组融合@@@@@@@@@@@@@@@@@@@@@@@",tt,meltgroup)
                            return 0
                        else:#单个的
                            spp.aadd(jiaocha)
        if spp.num >= 4:  # 大于4
            if spp.color == "crystal":
                print("透明色数量：",spp.num)
                spp.num=-55
                for br in spp.mapn:
                    if br.mel!=1:
                            br.stoptime=2.5# 3秒后stoptime=-0.1
                            print("55555555555555")
                            break
                continue
            for yichu in spp.mapn:
                map1.brickGroup.remove(yichu)
            dril1.score += spp.num
            spp.mapn.empty  # 清空
            print(dril1.score)
            meltgroup.pop(ii)

        ii+=1

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

map1=Map()
dril1=Drillers()
dril1.rect.left,dril1.rect.top=250,201