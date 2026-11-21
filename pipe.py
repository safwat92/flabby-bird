import pygame

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        super().__init__()
        self.image = pygame.image.load("img/pipe.png")
        self.rect = self.image.get_rect()
        self.pipe_gap = 180
        # if position = 1, we are rendering top pipe, 0 is bottom pipe
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - self.pipe_gap // 2]
        elif position == -1:
            self.rect.topleft = [x, y + self.pipe_gap // 2]

    def update(self):
        self.rect.x -= 2
        if self.rect.x < -50:
            self.kill()