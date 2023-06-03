import pygame
import random

pygame.init()

# variables
work_speed = 100
word_length = 2
screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("Random Word")


background = pygame.image.load("C:/Users/효서/Documents/Programming/python/project_rand_word/background.png")

Main_Font = pygame.font.Font(None, 100)

before_word = ""
not_word = []
alphabet = "abcdefghijklmnopqrstuvwxyz"
word_to_find = "hi"


def random_word():
    word = ""
    for i in range(word_length):
        word += alphabet[random.randrange(26)]
    return word

word1 = "start?"
word2 = ""
word3 = ""

running = True
while running:

    if word1 in not_word:
        word1 = random_word()
        pass
    elif word2 in not_word:
        word2 = random_word()
        pass
    elif word3 in not_word:
        word3 = random_word()
        pass
    elif word1 == word_to_find or word2 == word_to_find or word3 == word_to_find:
        running = False
    else:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print(len(not_word))
            
        not_word.append(word1)
        word1 = random_word()
        not_word.append(word2)
        word2 = random_word()
        not_word.append(word3)
        word3 = random_word()
        pygame.time.delay(work_speed)
                    

    text1 = Main_Font.render(word1,True,(255,255,255))
    text2 = Main_Font.render(word2,True,(255,255,255))
    text3 = Main_Font.render(word3,True,(255,255,255))

    screen.blit(background, (0, 0))
    screen.blit(text1,(screen_width/2 - (text1.get_rect().size[0]/2) , screen_height/2 - (text1.get_rect().size[1]/2)))
    screen.blit(text2,(screen_width/2 - (text2.get_rect().size[0]/2) , screen_height/2 - (text2.get_rect().size[1]/2) - 300))
    screen.blit(text3,(screen_width/2 - (text3.get_rect().size[0]/2) , screen_height/2 - (text3.get_rect().size[1]/2) + 300))


    pygame.display.update() 

pygame.time.delay(1000)


not_word.sort()
not_word.remove("start?")
not_word.remove("")
not_word.remove("")

print(len(not_word))
print(not_word)
pygame.quit()