import pygame
import math
import random
import os
location = os.path.dirname(os.path.abspath(__file__))

class bullet:
    def __init__(self, x_pos, y_pos, power, radian):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_power = power * math.cos(radian)
        self.y_power = power * math.sin(radian)
        self.sprite = pygame.image.load(f"{location}/images/bullet_1.png")
        self.rect = self.sprite.get_rect()


pygame.init()

screen_width = 1000
screen_height = 550
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("유사 포트리스")

clock = pygame.time.Clock()


background = pygame.image.load(f"{location}/images/background.png")

cannon = pygame.image.load(f"{location}/images/cannon.png")
cannon_size = cannon.get_rect().size
cannon_width = cannon_size[0]
cannon_height = cannon_size[1]
cannon_x_pos,cannon_y_pos = 40, 430

E_cannon = pygame.image.load(f"{location}/images/cannon_enemy.png")
E_cannon_size = E_cannon.get_rect().size
E_cannon_width = E_cannon_size[0]
E_cannon_height = E_cannon_size[1]
E_cannon_x_pos,E_cannon_y_pos = 875, 430

canWheel = pygame.image.load(f"{location}/images/cannon_wheel.png")
canWheel_size = canWheel.get_rect().size
canWheel_width = canWheel_size[0]
canWheel_height = canWheel_size[1]

E_canWheel = pygame.image.load(f"{location}/images/cannon_wheel.png")
E_canWheel_size = E_canWheel.get_rect().size
E_canWheel_width = E_canWheel_size[0]
E_canWheel_height = E_canWheel_size[1]

power_bar = pygame.image.load(f"{location}/images/power_bar.png")
fuel_bar = pygame.image.load(f"{location}/images/fuel_bar.png")
power_pointer = pygame.image.load(f"{location}/images/pointer.png")
frame = pygame.image.load(f"{location}/images/fuel_frame.png")

score_font = pygame.font.Font(None, 40)


# variables
shoot = False
hit = False
count = 0
my_health = 100
ene_health = 100
rotate_angle = 0
E_rotate_angle = 0
rotate_mod = 0 
move_mod = 0
power = 0
charging = False
k=1
bullets = []
turn = 1
fuel = 100
whl_angle = 0
E_whl_angle = 0
exploding = [pygame.image.load(f"{location}/images/explod_1.png"), pygame.image.load(f"{location}/images/explod_2.png"), pygame.image.load(f"{location}/images/explod_3.png")]


running = True
while running:

    dt = clock.tick(60)

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                rotate_mod = 1
            elif event.key == pygame.K_DOWN:
                rotate_mod = -1
            if event.key == pygame.K_RIGHT:
                move_mod = 1
            elif event.key == pygame.K_LEFT:
                move_mod = -1
            elif event.key == pygame.K_SPACE:
                power = 0
                charging = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                rotate_mod = 0
            elif event.key == pygame.K_DOWN:
                rotate_mod = 0
            if event.key == pygame.K_RIGHT:
                move_mod = 0
            elif event.key == pygame.K_LEFT:
                move_mod = 0
            elif event.key == pygame.K_SPACE:
                charging = False
                if not shoot:
                    shoot = True
                    if turn == 1:
                        bullets.append(bullet(cannon_x_pos + 10 , cannon_y_pos + 20, power/9 + 5, angle_rad))
                    else:
                        bullets.append(bullet(E_cannon_x_pos-22 , E_cannon_y_pos+10, power/9 + 5, E_angle_rad+math.pi))
                fuel = 100

    
    if rotate_mod != 0:
        if turn == 1:
            if rotate_angle >= 0 and rotate_angle <= 90:
                rotate_angle += rotate_mod * 2
            elif rotate_angle > 90:
                rotate_angle = 90         
            elif rotate_angle < 0:
                rotate_angle = 0
        else:
            if E_rotate_angle >= -90 and E_rotate_angle <= 0:
                E_rotate_angle += rotate_mod * -2
            elif E_rotate_angle > 0:
                E_rotate_angle = 0         
            elif E_rotate_angle < -90:
                E_rotate_angle = -90


    if move_mod != 0:
        if turn == 1:
            if fuel > 0:
                cannon_x_pos += 1 * move_mod
                whl_angle += -3 * move_mod
                fuel -= 1
        else:
            if fuel > 0:
                E_cannon_x_pos += 1 * move_mod
                E_whl_angle += -3 * move_mod
                fuel -= 1


    angle_rad = rotate_angle * math.pi / 180
    E_angle_rad = E_rotate_angle * math.pi / 180

    if charging:
        if power > 100:
            k =-1
        elif power < 0:
            k = 1
        power += 2 * k
    
    
    rot_cannon = pygame.transform.rotate(cannon, rotate_angle)
    E_rot_cannon = pygame.transform.rotate(E_cannon, E_rotate_angle)
    rot_wheel = pygame.transform.rotate(canWheel, whl_angle)
    E_rot_wheel = pygame.transform.rotate(E_canWheel, E_whl_angle)

    cannon_rect = rot_cannon.get_rect()
    cannon_rect.left = cannon_x_pos - rot_wheel.get_rect().size[0] / 2
    cannon_rect.top = cannon_y_pos - rot_cannon.get_rect().size[1]/2 + 30
    
    E_cannon_rect = E_rot_cannon.get_rect()
    E_cannon_rect.left = E_cannon_x_pos - E_rot_cannon.get_rect().size[0]/2
    E_cannon_rect.top = E_cannon_y_pos - E_rot_cannon.get_rect().size[1]/2 + 30

    for i in bullets:
        i.rect = i.sprite.get_rect()
        i.rect.left = i.x_pos
        i.rect.top = i.y_pos
    
    for i in bullets:
        if hit:
            i.x_power, i.y_power = 0,0
            i.sprite = exploding[count//5]
            count += 1
            if count > 12:
                bullets.remove(i)
                hit = False
                count = 0
            turn = (turn + 1)%2
            shoot = False
            
        else:
            if turn == 1:
                if i.y_pos > 500 or i.rect.colliderect(E_cannon_rect):
                    hit = True
            else:
                if i.y_pos > 500 or i.rect.colliderect(cannon_rect):
                    hit = True
            i.y_power -= 0.3
            i.x_pos += i.x_power/1.5
            i.y_pos -= i.y_power

        

    
    health = score_font.render(f"{my_health}", True,(255,255,255))



    screen.blit(background, (0, 0))
    screen.blit(power_bar, (10, 100))
    screen.blit(pygame.transform.scale(fuel_bar, (15,fuel*3)), (screen_width - 25, 400 -fuel*3))
    screen.blit(power_pointer, (20,390 - power*3))
    screen.blit(frame, (screen_width - 25, 100))
    
    screen.blit(rot_cannon, (cannon_x_pos - rot_cannon.get_rect().size[0]/2,cannon_y_pos - rot_cannon.get_rect().size[1]/2 + 30))
    screen.blit(E_rot_cannon, (E_cannon_x_pos - E_rot_cannon.get_rect().size[0]/2,E_cannon_y_pos - E_rot_cannon.get_rect().size[1]/2 + 30))
    screen.blit(rot_wheel ,(cannon_x_pos - rot_wheel.get_rect().size[0] / 2, screen_height - 70 - rot_wheel.get_rect().size[1] / 2))
    screen.blit(E_rot_wheel ,(E_cannon_x_pos - E_rot_wheel.get_rect().size[0] / 2, screen_height - 70 - E_rot_wheel.get_rect().size[1] / 2))
    for i in bullets:
        screen.blit(i.sprite,(i.x_pos-i.sprite.get_rect().size[0]/2,i.y_pos-i.sprite.get_rect().size[1]/2))

    screen.blit(health,(30,30))

    
    # # Draw Text
    # screen.blit([Text Name],([Text Coordinate]))

    # Update Screen
    pygame.display.update() 

# pause
pygame.time.delay(200)

# end game 
pygame.quit()