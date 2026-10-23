import pygame

class Bird:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.bird_pos = self.game.screen_h // 2 - 100 # 300
        self.bird_state = "break"
        self.velocity = -5

        self.images = [
            pygame.image.load("img/bird1.png"),
            pygame.image.load("img/bird2.png"),
            pygame.image.load("img/bird3.png"),
        ]
        self.counter = 0
        self.index = 0

    def render_bird(self):
        self.counter += 1

        if self.counter > 10:
            self.counter = 0
            self.index = (self.index + 1) % len(self.images)

        if self.bird_state == "falling":
            bird_image = pygame.transform.rotate(self.images[self.index], -30)
        elif self.bird_state == "break":
            bird_image = pygame.transform.rotate(self.images[self.index], 0)
        else:
            bird_image = pygame.transform.rotate(self.images[self.index], 30)

        self.screen.blit(bird_image, (80, self.bird_pos))

    def update(self):
        self.velocity += 0.25
        if self.velocity > 8:
            self.velocity = 8

        if self.bird_pos < self.game.screen_h - self.game.ground_height:
            print(f"pos: {self.bird_pos} velocity: {self.velocity}")
            self.bird_pos += self.velocity
            if self.velocity >= 0:
                self.bird_state = "falling"
        else:
            self.bird_pos = self.game.screen_h - self.game.ground_height
            self.bird_state = "break"


    def jump(self):
        self.velocity = -8
        self.bird_state = "rising"