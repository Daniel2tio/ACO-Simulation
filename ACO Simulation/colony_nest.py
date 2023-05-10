import pygame
import random
from parameters import *
from logic import *
from pheromones import *
from food import *
from ant import Ant

pygame.font.init()
text_color = (WHITE)
text_font = pygame.font.SysFont("Arial", 35)

class Nest:
    def __init__(self, position, n_ants=20):
        self.position = position
        self.n_ants = n_ants
        self.stock = 0
        self.ants = self.InitializeAnts()
        self.radius = 70
        self.color = BLACK

    def InitializeAnts(self):
        return [Ant(self.position, self) for _ in range(self.n_ants)]

    def Update(self, foods, pheromones, dt):
        for ant in self.ants:
            ant.Update(foods, pheromones, dt)
            if ant.position.x < 0:
                ant.position.x = WIDTH
            elif ant.position.x > WIDTH:
                ant.position.x = 0
            if ant.position.y < 0:
                ant.position.y = HEIGHT
            elif ant.position.y > HEIGHT:
                ant.position.y = 0
    def Show(self, screen, show_stock=True):
        pygame.draw.circle(screen, self.color, self.position.xy(), self.radius)

        if show_stock:
            text_surface = text_font.render(str(self.stock), True, text_color)
            text_rectangle = text_surface.get_rect(center=self.position.xy())
            screen.blit(text_surface, text_rectangle)
        for ant in self.ants:
            ant.Show(screen)

class Colony:
    def __init__(self):
        self.nest = Nest(Vector(WIDTH//2, HEIGHT//2), ANT_TOTAL)
        self.food = FoodMap(FOOD_SOURCE_TOTAL)
        self.pheromone = PheromoneMap()

    def Update(self, screen, showFoodTrail, showHomeTrail, delta_time):
        
        self.nest.Update(self.food, self.pheromone, delta_time)
        self.food.Update()
        self.pheromone.Update(screen, showFoodTrail, showHomeTrail)

    def Show(self, screen):
        self.nest.Show(screen)
        self.food.Show(screen)