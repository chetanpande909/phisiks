# Imports
import pymunk, pygame, math

GLOBAL_FRICTION = 0.5

# Dynamic means it will move 
class DynamicBall:
    def __init__(self, pos, vx, vy, img_of_32px, space):
        ## Image
        self.image = img_of_32px
        ## Body
        self.body = pymunk.Body(body_type=pymunk.Body.DYNAMIC)## name suggests everything -_-
        self.body.position = pos[0]                  ## name suggests everything -_-
        self.body.velocity = vx, vy                 ## name suggests everything -_-
        ## Shape
        self.shape = pymunk.Circle(self.body, 16)    ## this is the collision shape
        self.shape.density = 1                      ## if set to 0, body will behave wierdly
        self.shape.elasticity = 0.50                ## name suggests everything -_-
        self.shape.friction = GLOBAL_FRICTION
        ## Adding to the space
        space.add(self.body, self.shape)
        self.shape.collision_type = 1               ## idk wht this does, but if i comment it, the ball doesn't move
        ## This will b used for collsions for pygame
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect(
            self.body.position.x, 
            self.body.position.y, 
            self.shape.radius * 2, 
            self.shape.radius * 2
        )

    def draw(self, surf):
        ## Pygame comes into action ;)
        x, y = self.body.position
        self.rect.center = self.shape.body.position

        rotated_image = pygame.transform.rotate(self.image, -math.degrees(self.body.angle))
        new_rect = rotated_image.get_rect(center = self.image.get_rect(topleft = self.rect.topleft).center)

        surf.blit(rotated_image, new_rect.topleft)


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
        self.shape.friction = GLOBAL_FRICTION
        ## Adding to the space
        space.add(self.body, self.shape)
        self.shape.collision_type = 1               ## idk wht this does
        StaticLine.all_lines.append(self)

    def draw(self, surf, color):
        pygame.draw.line(surf, color, self.shape.a, self.shape.b, int(self.shape.radius) * 2)

# Victory Flag
class VictoryFlag:
    def __init__(self, pos):           # U have to put bottom point of the flag while making an instance
        self.image = pygame.image.load('imgs/victory_flag.png')
        self.rect = self.image.get_rect()
        self.rect.bottomleft = tuple(pos)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)