import pygame
import sys

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
            
        self.all_sprites = pygame.sprite.Group() # собираем все спрайты в одну кучу
        self.all_sprites.add(self.player_1)
        self.all_sprites.add(self.player_2)
        self.main_loop()

    def main_loop(self):
        game = True
        while game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                    self.all_srites.update()
                    self.screen.fill(BLACK)
                    self.all_sprites.draw(self.screen)
                    pygame.display.flip()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                game = False
                
            self.screen.fill(BLACK)
            self.all_sprites.update()
            self.all_sprites.draw(self.screen)
            pygame.display.flip()


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
        print("Да, я запускаюсь")
        if not self.is_automatik:
            keys = pygame.key.get_pressed()
            if keys[self.keys[0]]:
                self.rect.y += self.speed
            if keys[self.keys[1]]:
                self.rect.y -= self.speed



game = Game()

sys.exit()