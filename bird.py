import pygame

class Bird(pygame.sprite.Sprite):
    def __init__(self, screen, screen_h,ground_height):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.screen_h = screen_h
        self.ground_height = ground_height
        self.bird_pos = screen_h // 2 - 100 # 300
        self.bird_state = "break"
        self.velocity = -5

        self.images = [
            pygame.image.load("img/bird1.png"),
            pygame.image.load("img/bird2.png"),
            pygame.image.load("img/bird3.png"),
        ]

        self.counter = 0
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=(80, self.bird_pos))
        self.alive = True

    def update(self):        
        self.velocity += 0.25
        if self.velocity > 8:
            self.velocity = 8

        if self.rect.y < self.screen_h - self.ground_height:
            self.rect.y += self.velocity
            if self.velocity >= 0:
                self.bird_state = "falling"
        else:
            self.rect.y = self.screen_h - self.ground_height
            self.bird_state = "break"
            self.alive = False

        self.counter += 1

        if self.counter > 10:
            self.counter = 0
            self.index = (self.index + 1) % len(self.images)
        self.image = self.images[self.index]

        if self.bird_state == "falling":
            self.image = pygame.transform.rotate(self.images[self.index], -30)
        elif self.bird_state == "break":
            self.image = pygame.transform.rotate(self.images[self.index], 0)
        else:
            self.image = pygame.transform.rotate(self.images[self.index], 30)

    def jump(self):
        self.velocity = -6
        self.bird_state = "rising"

    def restart(self):
        self.alive = True
        self.velocity = -5
        self.rect = self.image.get_rect(center=(80, self.bird_pos))