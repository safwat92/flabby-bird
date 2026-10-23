import pygame
import bird

class Game:
    def __init__(self):
        self.screen_w = 600
        self.screen_h = 600
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_w, self.screen_h))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Flappy Bird")

        self.ground_scroll = 0
        self.bird = bird.Bird(self)

    def render_background_images(self):
        self.ground_height = 168
        self.bg_height = self.screen_h - self.ground_height

        bg_raw = pygame.image.load('img/bg.png')
        self.bg = pygame.transform.scale(bg_raw, (self.screen_w, self.bg_height))

        ground_raw = pygame.image.load('img/ground.png')
        self.ground_img = pygame.transform.scale(ground_raw, (self.screen_w + 35, self.ground_height))

    def ground_image_scroll(self):
        ground_y = self.bg_height

        self.screen.blit(self.bg, (0, 0))

        self.screen.blit(self.ground_img, (self.ground_scroll, ground_y))

        self.ground_scroll -= 5

        if abs(self.ground_scroll) >= 35:
            self.ground_scroll = 0

    def run(self):
        self.render_background_images()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.bird.jump()

            self.ground_image_scroll()
            self.bird.render_bird()
            self.bird.update()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
