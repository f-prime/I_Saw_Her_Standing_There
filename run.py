import pygame
from pygame.locals import *
import variables
import map_
import sys
import player as player_
import zombie as zombie_
import her as her_

def main():
    if not variables.player:
        screen = pygame.display.set_mode(variables.resolution)
        variables.screen = screen
    else:
        screen = variables.screen
    print variables.level
    map_.generate(variables.levels[variables.level])
    clock = pygame.time.Clock()
    Player = player_.Player()
    Her = her_.Her()
    Zombie = zombie_.Zombie()
    tile = pygame.image.load("res/tile.jpg").convert()
    her = pygame.image.load("res/her.png").convert_alpha()
    player = pygame.image.load("res/player.png").convert_alpha()
    her_infected = pygame.image.load("res/her_infected.png").convert_alpha()
    zombie = pygame.image.load("res/zombie.png").convert_alpha()
    zombie_moving_left = pygame.image.load("res/zombie_moving_left.png").convert_alpha()
    zombie_moving_right = pygame.image.load("res/zombie_moving_right.png").convert_alpha()
    player_moving_left = pygame.image.load("res/player_moving_left.png").convert_alpha()
    player_moving_right = pygame.image.load("res/player_moving_right.png").convert_alpha()
    cage = pygame.image.load("res/cage.png").convert_alpha()
    cage_closed = pygame.image.load("res/cage_closed.png").convert_alpha()
    her_moving_left = pygame.image.load("res/her_moving_left.png").convert_alpha()
    her_moving_right = pygame.image.load("res/her_moving_right.png").convert_alpha()
    pygame.font.init()
    font = pygame.font.Font("res/font.tff", 75)
    while True:
        clock.tick(65)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == K_UP and variables.jump == 0 and variables.onground:
                    variables.onground = False
                    variables.jump = 15
                
                if variables.i_died or variables.she_died or event.key == K_r:
                    variables.i_died = variables.she_died = False
                    variables.walls = []
                    variables.zombies = []
                    variables.captured = False
                    variables.infected = False
                    main()
        screen.fill((255,255,255))
        for ground in variables.walls:
            screen.blit(tile, (ground.x, ground.y))
        if variables.next_:
            level = variables.level - 1
        else:
            level = variables.level

        if not variables.she_died and not variables.i_died:
            if not variables.infected:
                for x in variables.text[level][0]:
                    screen.blit(font.render(x[0], 1, (0,0,0)), x[1])

            elif not variables.captured:
                for x in variables.text[level][1]:
                    screen.blit(font.render(x[0], 1, (0,0,0)), x[1])

            else:
                for x in variables.text[level][2]:
                    screen.blit(font.render(x[0], 1, (0,0,0)), x[1])
        
        elif variables.she_died:
            for x in variables.text[level][4]:
                screen.blit(font.render(x[0], 1, (0,0,0)), x[1])

        else:
            for x in variables.text[level][3]:
                screen.blit(font.render(x[0], 1, (0,0,0)), x[1])

        variables.moving = False

        key = pygame.key.get_pressed()
        
        if key[K_LEFT]:
            variables.moving = True
            variables.direction = "left"
            Player.move(-5, 0)

        if key[K_RIGHT]:
            variables.moving = True
            variables.direction = "right"
            Player.move(5, 0)
        
        if variables.jump > 0:
            Player.move(0, -10)
            variables.jump -= 1
        
        else:
            Player.move(0, 5)
        
        
        for zombies in variables.zombies:
            if zombies[1]:
                screen.blit(zombie_moving_left, (zombies[0].x, zombies[0].y))

            elif zombies[2]:
                screen.blit(zombie_moving_right, (zombies[0].x, zombies[0].y))

            else:
                screen.blit(zombie, (zombies[0].x, zombies[0].y))
        
        Zombie.check()

        if not variables.infected:
            screen.blit(her, (variables.her.x, variables.her.y))
        
        else:
            if variables.her_moving_right:
                screen.blit(her_moving_right, (variables.her.x, variables.her.y))
            elif variables.her_moving_left:
                screen.blit(her_moving_left, (variables.her.x, variables.her.y))
            else:
                screen.blit(her_infected, (variables.her.x, variables.her.y))

        if not variables.moving:
            screen.blit(player, (variables.player.x, variables.player.y))
        else:
            if variables.direction == "left":
                screen.blit(player_moving_left, (variables.player.x, variables.player.y))
            else:
                screen.blit(player_moving_right, (variables.player.x, variables.player.y))
        
        if not variables.captured:
            screen.blit(cage, (variables.cage.x, variables.cage.y))
        else:
            if not variables.next_go:
                variables.level += 1
                variables.next_ = 200
            variables.next_go = True
            screen.blit(cage_closed, (variables.cage.x, variables.cage.y))
            if variables.next_ == 0:
                variables.captured = False
                variables.next_go = False
                variables.infected = False
                variables.walls = []
                variables.zombies = []
                main()
            else:
                variables.next_ -= 1    
        variables.her_moving_right = variables.her_moving_left = False
        if not variables.captured:
            Her.check()
         
        pygame.display.update()

main()
        

