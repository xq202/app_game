import random
import pygame, sys
import button
from pygame.locals import *
pygame.init()
dis_width = 600
dis_height = 400
white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)
red = (255,0,0)
brown = (128,0,0)
file = open('snake_high_score.in','a+')
screen = pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption('test game')
clock = pygame.time.Clock()
exit_img = pygame.image.load('start_btn.png').convert_alpha()
exit_button = button.Button(50,330,exit_img,0.4)
#hiển thị một thông báo
def mess(screen,s,color,t,size):
    font = pygame.font.Font(None,size)
    text = font.render(s,color,SRCALPHA)
    screen.blit(text,t)
#in thức ăn
def print_food(foodx,foody,block):
    pygame.draw.rect(screen,blue,[int(foodx),int(foody),block,block])
#in một block
def print_block(x,y,z,t):
    pygame.draw.rect(screen,black,[x,y,z,t])
def menu():
    run = False
    menu = pygame.Surface((200,400),SRCALPHA)
    pygame.draw.polygon(menu,white,((0,0),(200,0),(200,400),(0,400),(0,0)))
    pygame.draw.polygon(menu,red,((0,0),(200,0),(200,400),(0,400),(0,0)),20)
    mess1 = '*su dung cac phim :'
    mess2 =  ' left , right, up, down  '
    mess3 = ' de dieu khien con ran.'
    mess4 = '*neu ran an vao than'
    mess5 = ' ran se bi ngan di,'
    mess6 = ' ban bi tru diem'
    mess7 = '*neu ran dam vao tuong'
    mess8 = ' game over'
    mess9 = '*an Esc de vao Help menu'
    mess(menu,mess1,(0,0,0),(20,20),20)
    mess(menu,mess2,(0,0,0),(20,40),20)
    mess(menu,mess3,(0,0,0),(20,60),20)
    mess(menu,mess4,(0,0,0),(20,80),20)
    mess(menu,mess5,(0,0,0),(20,100),20)
    mess(menu,mess6,(0,0,0),(20,120),20)
    mess(menu,mess7,(0,0,0),(20,140),20)
    mess(menu,mess8,(0,0,0),(20,160),20)
    mess(menu,mess9,(0,0,0),(20,180),20)
    screen.blit(menu,(0,0))
def again():
    block = 10
    snake_speed = 10
    x = 100
    y = 100
    x_snake = 0
    y_snake = 0
    snake_length = 3
    clock = pygame.time.Clock()
    foodx = 100
    foody = 200
    foodx = round(random.randrange(10,dis_width - block-15) / block) * block
    foody = round(random.randrange(10,dis_height - block-15) / block) * block
    game_running  = True
    arr_block = [[x-20,y],[x-10,y],[x,y]]
    check = False
    run = True
    onmenu = False
    timer = 0
    save_score = False
    high_score=0
    score_old = 0
    file.seek(0)
    test_file = file.readline()
    print(test_file)
    if test_file != '':
        high_score = int(test_file)
    while game_running:
        screen.fill(white)
        #viền quanh map
        pygame.draw.polygon(screen,brown,[(0,0),(dis_width,0),(dis_width,dis_height),(0,dis_height)],15)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_LEFT and x_snake!=10:
                    x_snake = -10
                    y_snake = 0
                    check = True
                elif event.key == pygame.K_RIGHT and x_snake!=-10:
                    x_snake = 10
                    y_snake = 0
                    check = True
                elif event.key == pygame.K_UP and y_snake!=10:
                    x_snake = 0
                    y_snake = -10
                    check = True
                elif event.key == pygame.K_DOWN and y_snake!=-10:
                    x_snake = 0
                    y_snake = 10
                    check = True
                elif event.key == pygame.K_ESCAPE:
                    onmenu = not onmenu
                if not run:
                    if event.key == pygame.K_q:
                        game_running = False
                    elif event.key == pygame.K_a:
                        run = True
                        save_score = False
                        again()
        if run:
            #in con rắn
            for i in range(len(arr_block)):
                if i==len(arr_block)-1 :
                    print_block(arr_block[i][0]+block/4,arr_block[i][1]+block/4,block/2,block/2)
                else:
                    print_block(arr_block[i][0],arr_block[i][1],block-1,block-1)
            if check:
                x+=x_snake
                y+=y_snake
                arr_block.append([x,y])
            while len(arr_block)>snake_length:
                arr_block.pop(0)
            #in thức ăn
            timer+=1
            if timer == 2:
                timer = 0
                print_food(foodx+block/4,foody+block/4,block/2)
            else :
                print_food(foodx,foody,block-1)
            #in score
            mess(screen,'score :' + str(snake_length) + '  high score: ' + str(high_score),red,(10,10),30)
            #con rắn ngắn đi khi ăn vào thân nó
            for i in range(len(arr_block)-2,-1,-1):
                if arr_block[i]==[x,y]:
                    for j in range(i):
                        snake_length-=1
            #rắn ăn mồi
            if x==foodx and y==foody:
                foodx = round(random.randrange(block,dis_width - block-15) / block) * block
                foody = round(random.randrange(block,dis_height - block-15) / block) * block
                snake_length+=1
        #con rắn đâm vào tường
            if x>=dis_width or x<0 or y>=dis_height or y<0:
                run = False
        if run == False:
            if snake_length>high_score and save_score==False:
                file.seek(0)
                file.truncate()
                score_old = high_score
                file.write(str(snake_length))
                high_score = snake_length
                save_score=True
            if snake_length>high_score:
                mess(screen,'  YOU WIN',red,(dis_width/3+30,dis_height/3+10),30)
                mess(screen,'  high score: '+str(high_score),red,(dis_width/3+30,dis_height/3+50),25)
            else:    
                mess(screen,' YOU LOSE',red,(dis_width/3+30,dis_height/3+10),30)
                mess(screen,'  your score: '+ str(snake_length),red,(dis_width/3+30,dis_height/3+30),25)
                mess(screen,'  high score: '+str(high_score),red,(dis_width/3+30,dis_height/3+50),25)
            mess(screen,'Q-quit  A-play again',red,(dis_width/3,dis_height/3+80),30)
        #mở menu
        if onmenu:
            check = False
            menu()
            if exit_button.draw(screen):
                onmenu = False
        pygame.display.update()
        clock.tick(snake_speed)
    pygame.quit()
    sys.exit()
again()
