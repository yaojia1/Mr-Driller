import pygame
import sys
from pages import *
from elements import *
from pygame.locals import *
screen = pygame.display.set_mode((800,600), 0, 32)
pygame.display.set_caption("Mr Driller")
framerate = pygame.time.Clock()
spdy = 0
tic=0
kkk1,kkk2=0,0
moveable=1
backimage = pygame.image.load("th.jpg")
rect = backimage.get_rect()
rect2 = pygame.Rect(0,0,rect.width ,rect.height)
rightimage=pygame.image.load("right.jpg")
text_fmt = my_font.render("AIR:" + str(dril1.air), 1, (255, 255, 255))
text_fmt2 = my_font.render("LIFE:" + str(dril1.life), 1, (255, 255, 255))
text_fmt3 = my_font.render("LEVEL:" + str(dril1.levelwin), 1, (255, 255, 255))
text_fmt4 = my_font.render("SCORE:" + str(dril1.score), 1, (255, 255, 255))
text_fmtwin = my_font.render("YOU WIN", 5, (255, 255, 255))
text_fmtlose = my_font.render("YOU LOSE", 5, (255, 255, 255))
text_fmtpause = my_font.render("PAUSE", 2, (255, 255, 255))
lifen=str(dril1.life)
pause=0

startpage(screen,0,0,0,0)
while True:
    '''TIME'''
    timepassed = framerate.tick(35)
    tic += timepassed / 1000
    screen.fill((0, 0, 0))
    '''开始界面'''

    '''background'''
    rect2.y =dril1.level+40
    if rect2.y>900:rect2.y=dril1.level+40-900
    screen.blit(backimage,(0,0),rect2)#背景图的移动
    screen.blit(rightimage, (555, 0))
    '''DIE'''
    if dril1.air<=0:
        dril1.life-=1
        dril1.air=100
        text_fmt = my_font.render("AIR:" + str(dril1.air), 1, (255, 255, 255))
        text_fmt2 = my_font.render("LIFE:" + str(dril1.life), 1, (255, 255, 255))
    '''输赢，暂未成功'''
    if dril1.life==0:
        endpage(screen, 0, 0, 0, 0, 0, 0, 0, dril1.score)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(kkk1, "@@@", kkk2)
                pygame.quit()
                sys.exit()
        screen.fill((0, 0, 0))
        '''画砖块，人'''
        map1.brickGroup.draw(screen)
        screen.blit(dril1.image, dril1.rect)
        '''右边信息栏'''
        screen.blit(text_fmt, (600, 100))
        screen.blit(text_fmt2, (600, 200))
        screen.blit(text_fmt3, (600, 300))
        screen.blit(text_fmt4, (600, 400))
        screen.blit(text_fmtlose, (250, 250))
        pygame.display.update()
        continue
    '''win界面需要高分榜'''
    if dril1.levelwin>=10:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(kkk1, "@@@", kkk2)
                pygame.quit()
                sys.exit()
        screen.fill((0, 0, 0))
        '''画砖块，人'''
        map1.brickGroup.draw(screen)
        screen.blit(dril1.image, dril1.rect)
        '''右边信息栏'''
        screen.blit(text_fmt, (600, 100))
        screen.blit(text_fmt2, (600, 200))
        screen.blit(text_fmt3, (600, 300))
        screen.blit(text_fmt4, (600, 400))

        screen.blit(text_fmtwin, (250, 250))
        pygame.display.update()
        continue

    '''pause'''
    if pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(kkk1, "@@@", kkk2)
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if 560<x<668 and 500<y<540:
                    pause=0
        screen.fill((0, 0, 0))
        '''画砖块，人'''
        map1.brickGroup.draw(screen)
        screen.blit(dril1.image, dril1.rect)
        '''右边信息栏'''
        screen.blit(text_fmt, (600, 100))
        screen.blit(text_fmt2, (600, 200))
        screen.blit(text_fmt3, (600, 300))
        screen.blit(text_fmt4, (600, 400))
        screen.blit(text_fmtpause, (600, 500))
        pygame.display.update()
        continue

    '''driller移动+打砖块'''
    key_pressed = pygame.key.get_pressed()
    spdx = 0  # 不动的时候x速度为0
    '''移动'''
    x = (dril1.rect.left + 13) // 50  # 中间
    collide_listm = pygame.sprite.spritecollide(dril1, map1.line[x], False)
    if x<10:
        rrr= x+1
        collide_listr = pygame.sprite.spritecollide(dril1, map1.line[rrr], False)
    else:
        rrr=x
        collide_listr=collide_listm
    if x>=1:
        lll=x-1
        collide_listl = pygame.sprite.spritecollide(dril1, map1.line[lll], False)
    else:
        lll = x
        collide_listl=collide_listm
    if key_pressed and moveable:
        if key_pressed[pygame.K_RIGHT]:
            spdx = 2
            if x!=rrr:
                for sp in collide_listr:
                    if dril1.rect.left + 16 < sp.rect.left <= dril1.rect.left + 33:  # 右边挡住了
                        if sp.rect.top < dril1.rect.top + 30: spdx = 0  # 腰上边的
            kkk1 += spdx
        if key_pressed[pygame.K_LEFT]:
            spdx = -2
            if x!=lll:
                for sp in collide_listl:
                    if dril1.rect.left + 16 > sp.rect.left + 51 >= dril1.rect.left:
                        if sp.rect.top < dril1.rect.top + 30: spdx = 0  # 腰上边的
            kkk2 += spdx
    '''打砖块'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(kkk1, "@@@", kkk2)
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if 560 < x < 668 and 500 < y < 540:
                pause = 1
        if event.type == pygame.KEYDOWN:  # 加了分数air显示
            # 键盘有按下？
            if event.key == pygame.K_UP:
                if dril1.rect.top > 550:
                    spdy = -6
                else:
                    for sp in collide_listm:
                        if sp.rect.top > dril1.rect.top + 35 and dril1.rect.top < sp.rect.top: spdy = -6
                    xx=dril1.rect.left
                    if xx<x*50+3:#左边超出
                        for sp in collide_listl:
                            if sp.rect.top > dril1.rect.top + 35 and dril1.rect.top < sp.rect.top: spdy = -6
                    elif xx+32>x*50+53:#右边超出
                        for sp in collide_listr:
                            if sp.rect.top > dril1.rect.top + 35 and dril1.rect.top < sp.rect.top: spdy = -6

            if event.key == pygame.K_DOWN:
                for sp in collide_listm:
                    if sp.rect.top <= dril1.rect.top + 40 <= sp.rect.top + 10:
                        if sp.color == "crystal":
                            if (sp.rect.top + dril1.level) % 50 == 0 and sp.stoptime == 0:
                                sp.stoptime = 2.5  # 3秒后stoptime=-0.1
                                break
                            else:
                                break
                        drillbrick(sp)
                        text_fmt4 = my_font.render("SCORE:" + str(dril1.score), 1, (255, 255, 255))

                        text_fmt = my_font.render("AIR:" + str(dril1.air), 1, (255, 255, 255))

                        spdy = 0
                        break
            if event.key == pygame.K_LEFT:
                moveable = 1
                if x!=0:
                    for sp in collide_listl:
                        if sp.rect.top < dril1.rect.top + 10 < sp.rect.top + 50 and dril1.rect.left + 16 > sp.rect.left + 51 >= dril1.rect.left:
                            moveable = 0
                            spdx = 0
                            if sp.life > 0:
                                sp.life -= 1
                            else:
                                if sp.color == "crystal":
                                    if (sp.rect.top + dril1.level) % 50 == 0 and sp.stoptime == 0:
                                        sp.stoptime = 2.5  # 3秒后stoptime=-0.1
                                        break
                                    else:
                                        break
                                drillbrick(sp)
                                text_fmt4 = my_font.render("SCORE:" + str(dril1.score), 1, (255, 255, 255))
                                text_fmt = my_font.render("AIR:" + str(dril1.air), 1, (255, 255, 255))
                        break
            if event.key == pygame.K_RIGHT:
                moveable = 1
                if x!=10:
                    for sp in collide_listr:
                        if sp.rect.top < dril1.rect.top + 10 < sp.rect.top + 50 and dril1.rect.left + 16 < sp.rect.left <= dril1.rect.left + 33:
                            moveable = 0
                            spdx = 0
                            if sp.life > 0:
                                sp.life -= 1
                            else:
                                if sp.color == "crystal":
                                    if (sp.rect.top + dril1.level) % 50 == 0 and sp.stoptime == 0:
                                        sp.stoptime = 2.5  # 3秒后stoptime=-0.1
                                        break
                                    else:
                                        break
                                drillbrick(sp)
                                text_fmt4 = my_font.render("SCORE:" + str(dril1.score), 1, (255, 255, 255))
                                text_fmt = my_font.render("AIR:" + str(dril1.air), 1, (255, 255, 255))
                            break

    '''移动+跳跃减速'''
    dril1.move(spdx, spdy)
    if spdy < 0:
        spdy += 0.2  # 跳跃减速
        for sp in collide_listm:
            if sp.rect.top + 51 >= dril1.rect.top >= sp.rect.top + 25:
                spdy = 0
                break
        if xx < x * 50 + 3:  # 左边超出
            for sp in collide_listr:
                if sp.rect.top + 51 >= dril1.rect.top >= sp.rect.top + 25:
                    spdy = 0
                    break
        elif xx + 32 > x * 50 + 53:  # 右边超出
            for sp in collide_listr:
                if sp.rect.top + 51 >= dril1.rect.top >= sp.rect.top + 25:
                    spdy = 0
                    break

    '''砖块融合消除'''
    mergebrick(tic)
    map1.brickGroup.update(tic)
    '''画砖块，人'''
    map1.brickGroup.draw(screen)
    screen.blit(dril1.image, dril1.rect)
    '''右边信息栏'''
    screen.blit(text_fmt, (600, 100))
    screen.blit(text_fmt2, (600, 200))
    screen.blit(text_fmt3, (600, 300))
    screen.blit(text_fmt4, (600, 400))
    screen.blit(text_fmtpause, (600, 500))
    '''level'''
    if dril1.rect.top<560: dril1.update()
    '''深度'''
    levelup()
    '''刷新'''
    pygame.display.update()
    '''AIR'''
    if tic >= 0.2:
        text_fmt3 = my_font.render("LEVEL:" + str(dril1.levelwin), 1, (255, 255, 255))
        text_fmt4 = my_font.render("SCORE:" + str(dril1.score), 1, (255, 255, 255))
        if str(dril1.life) != lifen:
            text_fmt2 = my_font.render("LIFE:" + str(dril1.life), 1, (255, 255, 255))
            lifen = str(dril1.life)
    if tic>=1:
        tic=0
        dril1.air-=1
        text_fmt = my_font.render("AIR:" + str(dril1.air), 1, (255, 255, 255))
        print(dril1.air)