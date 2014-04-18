import variables
import math

class Her:
    
    def check(self):
        try:
            distance = math.sqrt((abs(variables.her.x) - abs(variables.player.x)) + (abs(variables.her.y) - abs(variables.player.y)))
        except:
            try:
                distance = math.sqrt((abs(variables.player.x) - abs(variables.her.x)) + (abs(variables.player.x) - abs(variables.her.x)))
            except:
                distance = 100
        
        if distance <= 15:
            variables.infected = True
        
            if variables.her.x - variables.player.x > 0:
                self.move(-2, 0)

            else:
                self.move(2, 0)
        self.move(0, 5)

    def move(self, x, y):
        
        if x > 0:
            variables.her_moving_right = True
        if x < 0:
            variables.her_moving_left = True
        variables.her.x += x
        variables.her.y += y

        for walls in variables.walls:
            if walls.colliderect(variables.her):
                if x > 0:
                    variables.her.x -= x

                if x < 0:
                    variables.her.x += x

                if y < 0:
                    variables.her.y += y

                if y > 0:
                    variables.her.y -= y

        if variables.her.colliderect(variables.cage):
            variables.captured = True
            
        if variables.her.x >= variables.resolution[0] - 50:
            variables.her.x -= x

        if variables.her.x <= 0:
            variables.her.x += x

        if variables.her.y >= variables.resolution[1] - 50:
            variables.she_died = True
