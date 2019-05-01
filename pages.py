#for祝宝宝
import pygame
import random
import sys
import json
import string
from elements import *
from pygame.font import *
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800,600),0,32)
pygame.display.set_caption("Mr Driller")
framerate = pygame.time.Clock()
tic =0
my_font = pygame.font.SysFont("arial", 40)

text_start = my_font.render("Start", 3, (255, 255, 255))
text_h = my_font.render("Help", 3, (255, 255, 255))
text_back=my_font.render("Back",3,(0,0,0))
text_help1 = my_font.render("How to play", 5, (0, 0, 0))
text_end = my_font.render("Congratulations!",5,(255,255,255))
text_ask= my_font.render("Please input your name:",5,(255,255,255))
text_putin=my_font.render("Put in",3,(255,255,255))
text_score=my_font.render("Your score is:",3,(255,255,255))
text_list=my_font.render("RANK LIST",5,(255,255,255))
text_name=my_font.render("NAME",5,(255,255,255))
text_score1=my_font.render("SCORE",5,(255,255,255))
text_up=my_font.render("JUMP",5,(0,0,0))
text_down=my_font.render("Drill Down",5,(0,0,0))
text_left=my_font.render("Drill Left",5,(0,0,0))
text_right=my_font.render("Drill Right",5,(0,0,0))
startback = pygame.image.load("startback.jpg")
helpback = pygame.image.load("helpback.jpg")
turn_right=pygame.image.load("right1.jpg")
turn_left=pygame.image.load("left.jpg")
turn_up=pygame.image.load("up.jpg")
turn_down=pygame.image.load("down.jpg")
start = pygame.Surface(screen.get_size())
start= start.convert()
help_page = pygame.Surface(screen.get_size())
help_page = help_page.convert()
help_page.fill(color=(0,0,0))
end = pygame.Surface(screen.get_size())
end = end.convert()



def save(name,score):
    f=open('saveFile.txt', "r+")
    dic=f.read()
    dict=json.loads(dic)
    f.close()
    print(dict)
    dict[name]=score
    dic= json.dumps(dict)
    print(dict)
    f = open('saveFile.txt', "w+")
    f.write(dic)
    f.close()



'''bilt，画2个按钮在screen上一个开始游戏，一个是help游戏讲解'''
'''x,y是鼠标坐标，event是鼠标事件'''
'''if 点击help:
        就新画一个界面
        写上操作方法和一个返回按钮返回上个界面
elif点击开始游戏:
             return 0 开始游戏'''
def startpage(screen,x,y,event,f):
    start.blit(startback,(-50,0))
    pygame.draw.rect(start, (100, 100, 100), (180, 450, 100, 60), 0)
    pygame.draw.rect(start, (100, 100, 100), (560, 450, 100, 60), 0)
    start.blit(text_start,(190,455))
    start.blit(text_h,(570,455))
    screen.blit(start,(0,0))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y=event.pos
                if x>=560 and x<=660 and y>=450 and y<=510 and f==0:#help page,f judge we are in which page
                    help_page.blit(helpback,(0,0))                  #0:start    1:help
                    help_page.blit(text_help1,(300,60))
                    help_page.blit(turn_up, (100, 150))
                    help_page.blit(text_up, (200, 150))
                    help_page.blit(turn_down, (100, 210))
                    help_page.blit(text_down, (200, 210))
                    help_page.blit(turn_left, (100, 270))
                    help_page.blit(text_left, (200, 270))
                    help_page.blit(turn_right, (100, 330))
                    help_page.blit(text_right, (200, 330))
                    help_page.blit(text_back,(380,455))
                    screen.blit(help_page, (0, 0))
                    pygame.display.update()
                    f=1
                elif x>=370 and x<=470 and y>=450 and y<=510 and f==1:#back to start page
                    return startpage(screen, x, y, event, 0)
                elif x>=180 and x<=280 and y>=450 and y<=510 and f==0:#start game
                    return 0

    '''你可以设置几个参数加到参数栏来判断点击状态，因为这是个游戏循环会不停的调用这个函数'''
def endpage(screen,x,y,event,m,n,i,p,uscore1):
    dict={}
    l=[]
    names=""
    uscore2 = my_font.render(str(uscore1), 2, (255, 255, 255))
    end.fill((0,0,0))
    end.blit(text_end,(300,60))
    end.blit(text_ask, (100, 350))
    end.blit(text_score,(200,200))
    end.blit(uscore2, (400, 200))
    pygame.draw.rect(end, (100, 100, 100), (370, 450, 100, 60), 0)
    pygame.draw.rect(end,(255,255,255),(450,350,300,50),0)
    end.blit(text_putin, (380, 455))
    screen.blit(end, (0, 0))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:#input name
                inkey = chr(event.key)
                name = my_font.render(inkey, 2, (0, 0, 0))
                end.blit(name,(455+20*n,355))
                n += 1
                names+=str(inkey)
                screen.blit(end, (0, 0))
                pygame.display.update()
                if event.key == K_BACKSPACE:
                    pass#can not delete
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x>=370 and x<=470 and y>=450 and y<=510:
                    save(names, uscore1)
                    end.__init__(screen.get_size())
                    end.fill((0,0,0))
                    end.blit(text_list,(300,60))
                    end.blit(text_name, (400, 150 + i * 50))
                    end.blit(text_score1, (550, 150 + i * 50))
                    f = open('saveFile.txt', "r+")
                    dict = eval(f.read())
                    f.close()
                    pygame.display.update()
                    key = list(dict.keys())
                    for i in range(len(dict)):
                        k=0
                        for j in range(len(key)):
                            if dict[key[k]]<dict[key[j]]:
                                k=j
                            j+=1
                        l.append(key[k])
                        if i<=4:
                            if dict[key[k]]>=0:
                                num= my_font.render("No."+repr(m+1), 2, (255, 255, 255))
                                nam = my_font.render(key[k] , 2,(255, 255, 255))
                                sco = my_font.render(repr(dict[key[k]]), 2,(255, 255, 255))
                                m+=1
                                end.blit(num, (250, 150 + (i+1) * 50))
                                end.blit(nam, (400, 150 + (i+1) * 50))
                                end.blit(sco, (550, 150 + (i+1) * 50))
                        key.remove(key[k])
                        i+=1
                    print(l)
                    for p in range(len(dict)):
                        if l[p]==str(names):
                            you=my_font.render("YOURS :", 2, (255, 255, 255))
                            unum= my_font.render("No." + repr(p+1), 2, (255, 255, 255))
                            uname=my_font.render(l[p], 2, (255, 255, 255))
                            uscore=my_font.render(repr(dict[l[p]]), 2, (255, 255, 255))
                            end.blit(you, (100, 450))
                            end.blit(unum, (250, 450))
                            end.blit(uname, (400, 450))
                            end.blit(uscore, (550, 450))
                            screen.blit(end, (0, 0))
                            pygame.display.update()


    '''输入姓名'''
    '''一个提交姓名的按钮'''
    '''点击提交后姓名分数写入排名文件，页面上显示通关排名'''

