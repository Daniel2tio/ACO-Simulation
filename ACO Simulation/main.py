import pygame
from parameters import *
from logic import Vector
from colony_nest import Colony

# Initialising PyGame

pygame.display.init()

screen = pygame.display.set_mode(RESOLUTION)

clock = pygame.time.Clock()

fps = 60

colony = Colony()

# Toggling display of pheromones on/off
show_pheromone_food = True
show_pheromone_home = True

pause = False

run = True
while run:
    if not pause:
        screen.fill(WHITE)
    delta_time = clock.tick(fps)
    # update caption
    frame_rate = int(clock.get_fps())
    pygame.display.set_caption("COMP3004 - ANT COLONY SIMULATION: ( {} )".format(frame_rate))
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_f:
                show_pheromone_food = not show_pheromone_food
            if event.key == pygame.K_h:
                show_pheromone_home = not show_pheromone_home
            if event.key == pygame.K_SPACE:
                pause = not pause

    if not pause:
        colony.Update(screen, showFoodTrail=show_pheromone_food, showHomeTrail=show_pheromone_home, delta_time=delta_time)
        colony.Show(screen)

        pygame.display.flip()

pygame.quit()
