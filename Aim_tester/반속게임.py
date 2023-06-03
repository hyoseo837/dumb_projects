import pygame
import random
import time
import sys

pygame.init()

screen_width = 1400
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("반속게임")

font = pygame.font.Font(None, 40)
end_font = pygame.font.Font(None, 100)

clock = pygame.time.Clock()

# load background image
# background1 = pygame.image.load("C:/Users/ace20/Desktop/프로그래밍/gamedata/코리안발디/문1.png")

# load sprite
R = pygame.image.load("에임 테스터/알.png")
R_size = R.get_rect().size
R_width = R_size[0]
R_height = R_size[1]
R_x_pos = random.randrange(100,1300)
R_y_pos = random.randrange(100,700)

R2 = pygame.image.load("에임 테스터/알.png")
R2_size = R2.get_rect().size
R2_width = R2_size[0]
R2_height = R2_size[1]
R2_x_pos = random.randrange(100,1300)
R2_y_pos = random.randrange(100,700)

R3 = pygame.image.load("에임 테스터/알.png")
R3_size = R3.get_rect().size
R3_width = R3_size[0]
R3_height = R3_size[1]
R3_x_pos = random.randrange(100,1300)
R3_y_pos = random.randrange(100,700)

# Movement Variable
# to_x = 0
# to_y = 0
# character_speed = 0.5

# Text Variable
# [Font Name] = pygame.font.Font([Font Name], [Font Size])

# Time Variable
# [Moment Name] = pygame.time.get_ticks() # Save the moment

# event loop
running = True
point = 0
time_point = False
starting_time = 0

show_point = font.render(str(point), True, (0,0,0))
show_end_point = end_font.render(str(point), True, (0,0,0))
p30 = font.render("/ 30s", True, (128,128,128))

while running:

    # FPS setting
    dt = clock.tick(300)

    # Check event
    for event in pygame.event.get():
        screen.fill((255,255,255))

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                f_pos = pos[0]
                f_pos2 = pos[1]
                # print(f_pos)
        
                if f_pos>=R_x_pos-15 and f_pos<= R_x_pos+15 and f_pos2>= R_y_pos-15 and f_pos2<= R_y_pos+15:
                    R_x_pos = random.randrange(100,1300)
                    R_y_pos = random.randrange(100,700)
                    point += 1

                if f_pos>=R2_x_pos-15 and f_pos<= R2_x_pos+15 and f_pos2>= R2_y_pos-15 and f_pos2<= R2_y_pos+15:
                    R2_x_pos = random.randrange(100,1300)
                    R2_y_pos = random.randrange(100,700)
                    point += 1

                if f_pos>=R3_x_pos-15 and f_pos<= R3_x_pos+15 and f_pos2>= R3_y_pos-15 and f_pos2<= R3_y_pos+15:
                    R3_x_pos = random.randrange(100,1300)
                    R3_y_pos = random.randrange(100,700)
                    point += 1

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         starting_time = pygame.time.get_ticks()

        # if time_point == True:
        #     starting_time = pygame.time.get_ticks()
        # else:
        #     starting_time = 0
    
    current_time = pygame.time.get_ticks()

    if current_time - starting_time > 30000:
        time_point = True


            
    show_point = font.render(str(point), True, (0,0,0))
    show_end_point = end_font.render(str(point), True, (0,0,0))
    time_going = font.render(str(round(current_time*0.001)), True, (128,128,128))
    cps_point = font.render(str(round(point/30, 3)), True, (128,128,128))
    cps_ann = font.render(str('click/s'), True, (128,128,128))

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_q:
        #         s1_tf = True
        #     if event.key == pygame.K_LEFT:
        #         to_x -= character_speed
        #     if event.key == pygame.K_RIGHT:
        #         to_x += character_speed

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_w:
        #         s2_tf = True    
    
        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_LEFT:
        #         to_x = 0
        #     if event.key == pygame.K_RIGHT:
        #         to_x = 0
    
    # Collision Variable
    # Collision Check
    # if [Object 1]_rect.colliderect([Object 2]_rect):
    #     [Action]
    
    # Draw in Screen
    # Draw background
    # screen.blit(background1, (0, 0))

    # Draw Sprite
    if time_point == False:
        screen.blit(R, (R_x_pos,R_y_pos))
        screen.blit(R2, (R2_x_pos,R2_y_pos))
        screen.blit(R3, (R3_x_pos,R3_y_pos))
        screen.blit(show_point, (10,10))
        screen.blit(time_going, (1290,10))
        screen.blit(p30, (1330,10))

    elif time_point == True:
        screen.blit(show_end_point, (screen_width/2-20,screen_height/2-20))
        screen.blit(cps_point, (screen_width/2-70,screen_height/2+80))
        screen.blit(cps_ann, (screen_width/2+10,screen_height/2+80))
    # screen.blit(printed_time, (50,50))


    # # Draw Text
    # screen.blit([Text Name],([Text Coordinate]))

    # Update Screen
    pygame.display.update() 

# pause
pygame.time.delay(50)

# end game 
pygame.quit()