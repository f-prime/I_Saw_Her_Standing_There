import variables
import math

class Zombie:

    def check(self):
        for num, zombie in enumerate(variables.zombies):
            try:
                distance = math.sqrt((zombie[0].x - variables.player.x) + (zombie[0].y - variables.player.y))
            except:
                try:
                    distance = math.sqrt((variables.player.x - zombie[0].x) + (variables.player.y - zombie[0].y))
                except:
                    distance = 1000

            if distance <= 15:
                if variables.player.x > zombie[0].x:
                    self.move(num, 1,0)
                    zombie[1] = False
                    zombie[2] = True
                else:
                    self.move(num, -1, 0)
                    zombie[1] = True
                    zombie[2] = False

            else:
                zombie[1] = zombie[2] = False

            self.move(num, 0, 5)

    def move(self, zombie, x, y):
        
        variables.zombies[zombie][0].x += x
        variables.zombies[zombie][0].y += y

        for wall in variables.walls:
            if variables.zombies[zombie][0].colliderect(wall):
                if x > 0:
                    variables.zombies[zombie][0].x -= x

                if x < 0:
                    variables.zombies[zombie][0].x += x

                if y > 0:
                    variables.zombies[zombie][0].y -= y

                if y < 0:
                    variables.zombies[zombie][0].y += y

