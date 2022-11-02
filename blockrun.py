import pygame, sys
from pygame.locals import *
import random
import menu_block_run
import button_block_run

pygame.init()
timer = 0
fps = 200
min_fps = 200
width = 800
height = 600
size_Line = 10
size_block = 20
x_block = 200
y_block_down = height*2/3-size_block
y_block_up = height/3+size_Line-4
space_obstacle = random.randrange(15,100)
up_or_down = random.randint(0,1)
y_block = y_block_down
arr_obstacle = []
jump = False
y_next = 0
x_obstancle = width-100
height_obstancle = random.randrange(50,100)
width_obstancle = 20
do_kho = 2
global score
score = 0
x_button_gameover = width/3
y_botton_gameover = height/4
width_buton_go = 250
height_button_go = 300
file = open('high score.in', 'a+')
file.seek(0)
test_high_score = file.readline()
print(test_high_score)
if test_high_score == '':
    high_score = 0
else:
    high_score = int(test_high_score)
exit = button_block_run.Button('exit',20,"black",(100,255,200),50,30,x_button_gameover+50,y_botton_gameover+height_button_go-50)
restart = button_block_run.Button('restart',20,"black",(100,255,200),70,30,x_button_gameover+width_buton_go-100,y_botton_gameover+height_button_go-50)
continues = button_block_run.Button('continue',20,"black",(100,255,200),70,30,x_button_gameover+width_buton_go-100,y_botton_gameover+height_button_go-50)
game_over = menu_block_run.game_event('Game over',40,width_buton_go,height_button_go,x_button_gameover,y_botton_gameover)
game_menu = menu_block_run.game_event('menu',40,width_buton_go,height_button_go,x_button_gameover,y_botton_gameover)
start = button_block_run.Button('start game',20,pygame.color.Color('red'),pygame.color.Color('yellow'),100,30,350,300)
dis = pygame.display.set_mode((width,height))
def mess(textinp,x,y,color,size):
    font = pygame.font.Font(None,size)
    text = font.render(textinp,True,color)
    dis.blit(text,(x,y))
def obstacle(x,y,width,height,up_or_down):
    surface = pygame.Surface((width,height),SRCALPHA)
    pygame.draw.polygon(surface,"red",((0,height),(width/2,0),(width,height),(0,height)))
    if up_or_down==1:
        dis.blit(surface,(x,y))
    else:
        surface = pygame.transform.flip(surface,False,True)
        dis.blit(surface,(x,y))
def print_block(x,y,color,width,height):
    pygame.draw.rect(dis,color,(x,y,width,height))
def print_line(x,y,length,size):
    surface = pygame.Surface((length,10),SRCALPHA)
    pygame.draw.line(surface,(0,0,0),(length,0),(0,0),size)
    dis.blit(surface,(x,y))
game_running = True
running = False
on_menu = False
endgame = False
game_start = False
save_score = False
clock = pygame.time.Clock()
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump = not jump
                if jump:
                    y_next = -1
                else:
                    y_next = 1
            if event.key == pygame.K_ESCAPE and endgame == False:
                on_menu = not on_menu
                if on_menu==False:
                    running = True
                else:
                    running = False
    dis.fill(pygame.color.Color('white'))
    print_line(0,height/3,width*2,size_Line)
    print_line(0,height*2/3,width*2,size_Line)
    if game_start == False:
        if start.draw(dis):
            game_start = True
            running = True
    if running:
        y_block+=y_next
    if (y_block<=y_block_up or y_block>=y_block_down):
        y_next = 0
    #lam moi
    if len(arr_obstacle)==0 or arr_obstacle[-1][0]+width_obstancle+arr_obstacle[-1][3]<width:
        space_obstacle = random.randrange(15+do_kho,100+do_kho*2)
        up_or_down = random.randint(0,1)
        height_obstancle = random.randrange(20,90)
        arr_obstacle.append([width,height_obstancle,up_or_down,space_obstacle])
    #in chuong ngai vat
    for i in arr_obstacle:
        if i[2]==1:
            obstacle(i[0],y_block_down-(i[1]-width_obstancle),width_obstancle,i[1],1)
        else:
            obstacle(i[0],y_block_up,width_obstancle,i[1],0)
    #chuong ngai vat move
    if running:
        for i in arr_obstacle:
            i[0]-=1
    if arr_obstacle[0][0]<-width:
        arr_obstacle.pop(0)
    #in block
    print_block(x_block,y_block,"green",size_block,size_block)
    #check block va cham chuong ngai vat
    for i in arr_obstacle:
        if (x_block==i[0] or x_block+size_block==i[0]+width_obstancle) and y_block+size_block > y_block_down-i[1]+size_block and i[2]==1:
            running = False
            endgame = True
        if (x_block==i[0] or x_block+size_block==i[0]+width_obstancle) and y_block < y_block_up+i[1] and i[2]==0:
            running = False
            endgame = True
    mess('dung space de dieu khien',300,500,"black",20)
    mess('score: ' + str(score) + '   high score: '+ str(high_score),20,100,"black",20)
    #hien thi bang game over
    if endgame == True:
        if save_score == False:
            file.seek(0)
            s = file.readline()
            if s!='':
                if int(s)<score:
                    file.seek(0)
                    file.truncate()
                    file.write(str(score))
                    high_score = score
            else :
                file.write(str(score))
                high_score = score
            save_score = True
        game_over.draw(dis)
        if exit.draw(dis):
            game_running = False
        if restart.draw(dis):
            arr_obstacle.clear()
            score = 0
            y_next = 0
            y_block = y_block_down
            running = True
            jump = False
            fps = min_fps
            on_menu = False
            endgame = False
            save_score = False
        print_score = menu_block_run.game_event('your score: '+str(score),20,150,50,x_button_gameover+50,y_botton_gameover+100)
        print_score.draw(dis)
    #mở menu
    if on_menu:
        game_menu.draw(dis)
        if exit.draw(dis):
            game_running = False
        if continues.draw(dis):
            on_menu = False
            running = True
    timer+=1
    #tang diem
    if running:
        score +=1
    if timer>3000+fps:
        do_kho+=1
        timer = 0
        fps+=25
    pygame.display.update()
    clock.tick(fps)
