# Imports
import pymunk, pygame

# Dynamic means it will move 
class DynamicBall:
    def __init__(self, x, y, vx, vy, r, space):
        ## Body
        self.body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)## name suggests everything -_-
        self.body.position = x, y                   ## name suggests everything -_-
        self.body.velocity = vx, vy                 ## name suggests everything -_-
        ## Shape
        self.shape = pymunk.Circle(self.body, r)    ## this is the collision shape
        self.shape.density = 1                      ## if set to 0, body will behave wierdly
        self.shape.elasticity = 1                   ## name suggests everything -_-
        ## Adding to the space
        space.add(self.body, self.shape)
        self.shape.collision_type = 1               ## idk wht this does, but if i comment it, the ball doesn't move

    def draw(self, surf, color):
        ## Pygame comes into action ;)
        x, y = self.body.position
        pygame.draw.circle(surf, color, (int(x), int(y)), int(self.shape.radius))
        '''
        x, y and radius are floats and thus need to b changed to integer,
        cuz pygame doesn't supports floats as position and radius to draw
        '''
# Converse of Dynamic -_-
class StaticBox:
    def __init__(self, x, y, w, h, r, space):
        ## Rect for pygame
        self.rect = pygame.Rect(x, y, w, h)
        ## Body
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)## name suggests everything -_-
        # self.body.position = x, y                   ## name suggests everything -_-
        ## Shape
        self.shape = pymunk.Poly(self.body, [(x, y), (x+w, y), (x+w, y+h), (x, y+h)], radius=r)     ## this is the collision shape
        self.shape.elasticity = 1                   ## name suggests everything -_-
        ## Adding to the space
        space.add(self.body, self.shape)
        self.shape.collision_type = 1               ## idk wht this does
        
    def draw(self, surf, color):
        # self.rect.center = self.body.position               ## match the rect's position with the body's position
        pygame.draw.rect(surf, color, self.rect)

# Box is slow so just draw a line with the width ;)
# looks the same tho
class StaticLine:
    all_lines = []
    def __init__(self, start_point, end_point, w, space):
        ## Body
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)## name suggests everything -_-
        # self.body.position = x, y                   ## name suggests everything -_-
        ## Shape
        self.shape = pymunk.Segment(self.body, start_point, end_point, w)     ## this is the collision shape
        self.shape.elasticity = 1                   ## name suggests everything -_-
        ## Adding to the space
        space.add(self.body, self.shape)
        self.shape.collision_type = 1               ## idk wht this does
        StaticLine.all_lines.append(self)

    def draw(self, surf, color):
        pygame.draw.line(surf, color, self.shape.a, self.shape.b, int(self.shape.radius) * 2)

# Victory Flag
class VictoryFlag:
    def __init__(self, x, y):           # U have to put bottom point of the flag while making an instance
        self.image = pygame.image.load('victory_flag.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = (x, y)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)