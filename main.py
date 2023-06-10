import pygame
import random
import time

class Bucket:
    def __init__(self, x, y, w, h, filename, speed):
        self.rect = pygame.Rect(x, y, w, h)
        self.image = pygame.image.load(filename)
        self.speed = speed

    def draw(self, window):
        pygame.draw.rect(window,(0, 0, 0), self.rect)
        window.blit(self.image, [self.rect.x, self.rect.y])

class Apple:
    def __init__(self, x, y, w, h, filename, speed):
        self.rect = pygame.Rect(x, y, w, h)
        self.image = pygame.image.load(filename)
        self.speed = speed

    def draw(self, window):
        pygame.draw.rect(window,(0, 0, 0), self.rect)
        window.blit(self.image, [self.rect.x, self.rect.y])



pygame.init()
screen = pygame.display.set_mode((500, 500))
fps = pygame.time.Clock()

background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (800, 2000))

bucketpng = (Bucket(180, 250, 80, 85, "pixil-frame-0 (13).png", 5))
apples = []
apples.append(Apple(200, 50, 40, 40, "imageedit_5_8933911748.png", 5))
apples.append(Apple(120, 50, 40, 40, "imageedit_5_8933911748.png", 5))
n = random.randint(0, 450)
startTime = time.time()
timer = int(time.time()-startTime)
points = 0
loseText = pygame.font.Font(None, 56).render("Ти програв! ", True, (0, 0, 0))
winText = pygame.font.Font(None, 56).render("Ти виграв! ", True, (0, 0, 0))
while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                bucketpng.speed = -5

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                bucketpng.speed = 5

    timer = int(time.time()-startTime) 
    timeText = pygame.font.Font(None, 56).render("Час: "+ str(timer), True, (0, 0, 0))
    pointText = pygame.font.Font(None, 56).render("Рахунок: "+ str(points), True, (0, 0, 0))
    
    if bucketpng.rect.x > 430:
        bucketpng.rect.x = 430
    if bucketpng.rect.x < 0:
        bucketpng.rect.x = 0
        

    bucketpng.rect.x += bucketpng.speed
    for i in range(len(apples)):
        apples[i].rect.y += apples[i].speed
    
    for i in range(len(apples)):
        if bucketpng.rect.colliderect(apples[i].rect):
            n = random.randint(0, 450)
            apples[i].rect.x = n
            apples[i].rect.y = -50
            points += 1


    for i in range(len(apples)):
        if apples[i].rect.y == 400:
            n = random.randint(0, 450)
            apples[i].rect.x = n
            apples[i].rect.y = -50
            points -= 1

    if timer > 10:
        screen.fill((250, 0, 0))
        screen.blit(loseText, [100, 100])
        pygame.display.flip()
        break

    if points == 5:
        screen.fill((0, 250, 0))
        screen.blit(winText, [100, 100])
        pygame.display.flip()
        break

    screen.fill((0, 170, 170))
    screen.blit(background, [0,0])
    screen.blit(timeText, [0, 0])
    screen.blit(pointText, [300, 0])
    for i in range(len(apples)):
        apples[i].draw(screen)
    bucketpng.draw(screen)
    pygame.display.flip()

    fps.tick(60)
