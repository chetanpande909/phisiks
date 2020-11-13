import pymunk, pygame

class Ball:
    def __init__(self, x, y, vx, vy, r, space):
        ## Body
        self.body = pymunk.Body()                   ## name suggests everything -_-
        self.body.position = x, y                   ## name suggests everything -_-
        self.body.velocity = vx, vy                 ## name suggests everything -_-
        ## Shape
        self.shape = pymunk.Circle(self.body, r)    ## this is the collision shape
        self.shape.density = 1                      ## if set to 0, body will behave wierdly
        self.shape.elasticity = 1                   ## name suggests everything -_-
        ## Adding to the space
        space.add(self.body, self.shape)
        self.shape.collision_type = 1               ## idk wht this does

    def draw(self, surf, color):
        ## Pygame comes into action ;)
        x, y = self.body.position
        pygame.draw.circle(surf, color, (int(x), int(y)), int(self.shape.radius))
