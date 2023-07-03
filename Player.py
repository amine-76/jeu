import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self,x,y):
            super().__init__()
            self.sprite_sheet = pygame.image.load('Dresseur.png')
            self.image = self.get_image(0,0)
            self.image.set_colorkey([0,0,0])
            self.rect=self.image.get_rect()
            self.position=[x,y]
            self.images = {
                'down': self.get_image(0,0),
                'left': self.get_image(0,75),
                'right': self.get_image(0,150),
                'up': self.get_image(0,175)
            }
            self.speed = 3

    def change_animation(self,name):
        self.image = self.images[name]
        self.image.set_colorkey((0,0,0))


    def update(selt):
        selt.rect.topleft = selt.position

    def move_right(self):
        self.position[0] += self.speed

    def move_left(self):
        self.position[0] -= self.speed

    def move_up(self):
        self.position[1] -= self.speed

    def move_down(self):
        self.position[1] += self.speed

    def get_image(self,x,y):
        image = pygame.Surface([75,75])
        image.blit(self.sprite_sheet,(0,0),(x,y,70,70))
        return image