import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Bee movie")

screenWidth = 500

x = 50
y = 430
width = 40
height = 60
vel = 5

isJumping = False
jumpCount = 10

gameOn = True

while gameOn:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False
        
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < screenWidth - width - vel:
        x += vel
    if not(isJumping):
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < 500 - height - vel:
            y += vel
        if keys[pygame.K_SPACE]:
            isJumping = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJumping = False
            jumpCount = 10



    win.fill((0, 0, 0))
    pygame.draw.rect(win, (0, 200, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()