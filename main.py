import pygame
import sys
from elements import *
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((800,600), 0, 32)
pygame.display.set_caption("Mr Driller")
framerate = pygame.time.Clock()
spdy = 0
tic=0
kkk1,kkk2=0,0
moveable=1
my_font = pygame.font.SysFont("arial", 40)
if not pygame.font: print('Warning, fonts disabled')
while True:
    die(dril1)
    timepassed=framerate.tick(60)
    tic+=timepassed/1000
    screen.fill((0, 0, 0))
    collide_list2 = pygame.sprite.spritecollide(dril1, map1.brickGroup, False)
    key_pressed = pygame.key.get_pressed()
    spdx = 0  # 不动的时候x速度为0
    if key_pressed and moveable:
        if key_pressed[pygame.K_RIGHT]:
            spdx = 2
            for sp in collide_list2:
                if dril1.rect.left + 16 < sp.rect.left <= dril1.rect.left + 33:  # 右边挡住了
                    if sp.rect.top < dril1.rect.top + 30: spdx = 0  # 腰上边的
            kkk1 += spdx
        if key_pressed[pygame.K_LEFT]:
            spdx = -2
            for sp in collide_list2:
                if dril1.rect.left + 16 > sp.rect.left + 51 >= dril1.rect.left:
                    if sp.rect.top < dril1.rect.top + 30: spdx = 0  # 腰上边的
            kkk2 += spdx
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(kkk1,"@@@" ,kkk2)
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # 键盘有按下？
            if event.key == pygame.K_UP:
                if dril1.rect.top > 550: spdy = -5
                else:
                    for sp in collide_list2:
                        if sp.rect.top > dril1.rect.top + 35 and dril1.rect.top < sp.rect.top: spdy = -5
            if event.key == pygame.K_DOWN:
                for sp in collide_list2:
                    if sp.rect.left<dril1.rect.left+16<sp.rect.left+50:
                        if sp.color == "crystal":
                            if (sp.rect.top+dril1.level) % 50 == 0 and sp.stoptime == 0:
                                sp.stoptime = 2.5  # 3秒后stoptime=-0.1
                                break
                            else:
                                break
                        drillbrick(sp)
                        spdy=0
                        break
            if event.key == pygame.K_LEFT:
                moveable = 1
                for sp in collide_list2:
                    if sp.rect.top<dril1.rect.top+10<sp.rect.top+50 and dril1.rect.left + 16 > sp.rect.left + 51 >= dril1.rect.left:
                        moveable=0
                        spdx=0
                        if sp.life>0:
                            sp.life-=1
                        else:
                            if sp.color == "crystal":
                                if (sp.rect.top+dril1.level) % 50 == 0 and sp.stoptime == 0:
                                    sp.stoptime = 2.5  # 3秒后stoptime=-0.1
                                    break
                                else:
                                    break
                            drillbrick(sp)
                        break
            if event.key == pygame.K_RIGHT:
                moveable = 1
                for sp in collide_list2:
                    if sp.rect.top<dril1.rect.top+10<sp.rect.top+50 and dril1.rect.left + 16 < sp.rect.left <= dril1.rect.left + 33:
                        moveable=0
                        spdx=0
                        if sp.life>0:
                            sp.life-=1
                        else:
                            if sp.color == "crystal":
                                if (sp.rect.top+dril1.level) % 50 == 0 and sp.stoptime == 0:
                                    sp.stoptime = 2.5  # 3秒后stoptime=-0.1
                                    break
                                else:
                                    break
                            drillbrick(sp)
                        break
    dril1.move(spdx,spdy)
    if spdy<0:
        spdy += 0.1  # 跳跃减速
        for sp in collide_list2:
            if sp.rect.top+51>=dril1.rect.top>=sp.rect.top+44:
                spdy=0
                break
    mergebrick(tic)
    map1.brickGroup.update(tic)
    map1.brickGroup.draw(screen)
    screen.blit(dril1.image, dril1.rect)
    text_fmt = my_font.render("AIR:" + str(dril1.air), 1, (255, 255, 255))
    text_fmt2 = my_font.render("LIFE:" + str(dril1.life), 1, (255, 255, 255))
    text_fmt3 = my_font.render("LEVEL:" + str(dril1.level), 1, (255, 255, 255))
    screen.blit(text_fmt,(560,100))
    screen.blit(text_fmt2, (560, 200))
    screen.blit(text_fmt3, (560, 300))
    if dril1.rect.top<560: dril1.update()
    levelup()
    pygame.display.update()
    if tic>=1:
        tic=0
        dril1.air-=1
        print(dril1.air)


