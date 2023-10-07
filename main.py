import pygame

pygame.init()

ScreenWidth = 640
ScreenHeight = 480
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))

pygame.display.set_caption("Kopeng Game")

clock = pygame.time.Clock()
 
running = True 

while running:

    DeltaTime = clock.tick(30)

    for event in pygame.event.get(): 
        
        if event.type == pygame.QUIT: 
            running = False

    screen.fill((255, 0, 0))
    pygame.display.update()


pygame.quit()