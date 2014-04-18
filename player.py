import variables


class Player:
    def move(self, x, y):
        variables.player.x += x
        variables.player.y += y
        
        for walls in variables.walls:
            if walls.colliderect(variables.player):
                if x > 0:
                    variables.player.x -= x

                if x < 0:
                    variables.player.x += x

                if y > 0:
                    variables.onground = True
                    variables.player.y -= y

                if y < 0:
                    variables.player.y += 10


        if variables.player.x <= 0:
            variables.player.x += abs(x)

        if variables.player.x >= variables.resolution[0] - 50:
            variables.player.x -= abs(x)

        if variables.player.y >= variables.resolution[1] - 50:
            variables.i_died = True


        if variables.player.colliderect(variables.her) and not variables.captured:
            variables.i_died = True


        for zombie in variables.zombies:
            if zombie[0].colliderect(variables.player) and not variables.captured:
                variables.i_died = True
