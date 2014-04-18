import variables
import pygame

def generate(map_):
    with open(map_, 'rb') as file:
        y_cord = 0
        for x in file.readlines():
            x_cord = 0
            for y in list(x):
                if y == "w":
                    variables.walls.append(pygame.Rect(x_cord, y_cord, 50, 50))
                if y == "c":
                    variables.cage = pygame.Rect(x_cord+50, y_cord, 25, 100)

                if y == "h":
                    variables.her = pygame.Rect(x_cord, y_cord, 25, 50)

                if y == "p":
                    variables.player = pygame.Rect(x_cord, y_cord, 25, 50)
                
                if y == "z":
                    variables.zombies.append([pygame.Rect(x_cord, y_cord, 25, 50), False, False])

                x_cord += 50

            y_cord += 50
