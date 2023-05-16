import pygame
import sys
from random import randint, choice
from math import radians, sin, cos

WHITE = (255,255,255)
BLACK = (00, 00, 00)

class Game:
    def __init__(self):
        pygame.init()
        WHITE = (255, 255, 255)
        screen_info = pygame.display.Info()
        self.W = screen_info.current_w
        self.H = screen_info.current_h
        self.screen = pygame.display.set_mode(
            (self.W, self.H),
            pygame.FULLSCREEN
        )
        self.screen_rect = self.screen.get_rect()
        self.player_1 = Paddle(
            self.screen_rect,
            (self.screen_rect.width * 0.1, self.screen_rect.centery),

            keys = (pygame.K_s,pygame.K_w),
            

        )
        self.player_2 = Paddle(
            self.screen_rect,
            (self.screen_rect.width * 0.9, self.screen_rect.centery),
            is_automatic = True,
            keys = (pygame.K_s, pygame.K_w))
        
        ball = Ball(self.screen_rect)
        ball.throw_in()
        self.paddles = pygame.sprite.Group()
        self.ball = pygame.sprite.Group()
        self.paddles.add(self.player_1)
        self.paddles.add(self.player_2)
        self.ball.add(ball)
        self.main_loop()

    def main_loop(self):
        game = True
        while game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                game = False

            self.screen.fill(BLACK)
            self.paddles.update()
            self.ball.update()
            self.paddles.draw(self.screen)
            self.ball.draw(self.screen)
            pygame.display.flip()
        pygame.quit    


class Paddle(pygame.sprite.Sprite): #отец ракетки
    def __init__(
                self,
                screen_rect =None,
                center = (10, 10),
                color = WHITE,
                size = (20, 150),
                keys = (pygame.K_UP, pygame.K_DOWN),
                speed = 10,
                is_automatic = False 
                
    ):
        super().__init__() 
        if not size:
            size = (screen_rect.width * 0.01, screen_rect.height * 0.05) 
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speed = speed
        self.keys = keys
        self.is_automatik = is_automatic

    def update(self):
        print("я запускаюсь")
        if not self.is_automatik:
            keys = pygame.key.get_pressed()
            if keys[self.keys[0]]:
                self.rect.y += self.speed
            if keys[self.keys[1]]:
                self.rect.y -= self.speed
    

class Ball(pygame.sprite.Sprite):
    """
    мяч
    отскок
    """
    def __init__(
        self,
        screen_rect=None,
        center=None,
        color=WHITE,
        size=(5, 5),
        speed=1,
        direction=90,
        vel_x=0,
        vel_y=0
        
    ):
        super().__init__()
        self.screen_rect = screen_rect
        if not size:
            size = (self.screen_rect.width * 0.01, self.screen_rect.weight * 0.01)
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        if not center:
            self.rect.center = screen_rect.center
        self.speed = speed
        self.direction = direction
        selfvel_x = vel_x
        selfvel_y = vel_y

    def update(self):
        self.vel_x = sin(radians(self.direction)) * self.speed
        self.vel_y = cos(radians(self.direction)) * self.speed * -1
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
    
    def throw_in(self):
        self.rect.center = self.screen_rect.center
        self.direction = choice((randint(45, 135), randint(225, 315)))


game = Game()

sys.exit()