import pygame
import random

pygame.init()

word_length = 3
screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Random Word")


background = pygame.image.load("C:/Users/효서/Documents/Programming/python/project_rand_word/background.png")

Main_Font = pygame.font.Font(None, 300)
Second_Font = pygame.font.Font(None, 50)

before_word = ""
not_word = []
alphabet = "abcdefghijklmnopqrstuvwxyz"


def random_word():
    word = ""
    for i in range(word_length):
        word += alphabet[random.randrange(26)]
    return word

word = "start?"

running = True
while running:

    if word in not_word:
        word = random_word()
        pass
    else:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    not_word.append(word)
                    before_word = word
                    word = random_word()
                if event.key == pygame.K_n:
                    running = False

    before_text = Second_Font.render(before_word, True, (255,255,255) )
    text = Main_Font.render(word,True,(255,255,255))
    screen.blit(background, (0, 0))
    screen.blit(text,(screen_width/2 - (text.get_rect().size[0]/2) , screen_height/2 - (text.get_rect().size[1]/2)))
    screen.blit(before_text, (30, screen_height/2 - (before_text.get_rect().size[1]/2)))

    pygame.display.update() 

not_word.sort()
print(not_word)
pygame.quit()