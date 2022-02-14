import pygame
import random
pygame.init()

win = pygame.display.set_mode((600, 600))

pygame.display.set_caption("lol")

x = random.randint(1, 575)
y = random.randint(1, 575)
enemyx = random.randint(1, 575)
enemyy = random.randint(1, 575)
width = 25
height = 25
obstaclex = enemyx - 5
obstacley = enemyy - 5
vel = 2
bg = pygame.image.load('bg.png')

run = True
while run:
    pygame.time.delay(4)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    key = pygame.key.get_pressed()

    if key[pygame.K_a]:
        x -= vel

    if key[pygame.K_d]:
        x += vel

    if key[pygame.K_s]:
        y += vel

    if key[pygame.K_w]:
        y -= vel

    win.blit(bg, (0,0))
    player = pygame.draw.rect(win, (255,0,0), (x,y,width,height))
    enemy = pygame.draw.rect(win, (0,0,255), (enemyx,enemyy,width,height))
    #obstacle = pygame.draw.rect(win, (0,255,0), (obstaclex,obstacley,width,height))


    money = player.colliderect(enemy)

    if money:
        enemyy = random.randint(1, 575)
        enemyx = random.randint(1, 575)
        #obstaclex = random.randint(1, 575)
        #obstacley = random.randint(1, 575)

    #if player.colliderect(obstacle):
        #break

    

    

    pygame.display.update()
pygame.quit()        
