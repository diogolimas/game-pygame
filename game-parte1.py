import pygame

pygame.init()

#locations variables
x = 400
y = 300

velocity = 10

window = pygame.display.set_mode((600,600))

pygame.display.set_caption("Py Game test application")

open_window = True

while(open_window):
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open_window = False
        commands = pygame.key.get_pressed()
    if(commands[pygame.K_UP]):
        y-= velocity
    if(commands[pygame.K_DOWN]):
        y+= velocity
    if(commands[pygame.K_RIGHT]):
        x+= velocity
    if(commands[pygame.K_LEFT]):
        x-= velocity

    window.fill((229, 244, 251))
    pygame.draw.circle(window, (148, 216, 45), (x,y), 50 )

    pygame.display.update()
pygame.quit()