import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

is_blue = True


done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(60, 60, 120, 120))
    
    pygame.display.flip()

