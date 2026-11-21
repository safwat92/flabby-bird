import pygame
import bird
import pipe
import random

class Game:
    def __init__(self):
        self.screen_w = 550
        self.screen_h = 700

        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_w, self.screen_h))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Flappy Bird")

        # global variables
        self.running = True
        self.game_state = "running"
        self.ground_height = 168
        self.flappy = bird.Bird(self.screen, self.screen_h, self.ground_height)
        self.pipe_group = pygame.sprite.Group()
        self.bird_group = pygame.sprite.Group()
        self.ground_scroll = 0
        self.last_mouse_state = False
        self.mid_screen = self.screen_h // 2
        self.pipe_freq = 2500
        self.last_pipe_shown = pygame.time.get_ticks() - self.pipe_freq
        self.score = 0
        self.highest_score = 0
        self.bird_passed_pipe = False
        self.restart_btn = pygame.image.load("img/restart.png")
        self.score_font = pygame.font.Font(None, 48)

    def load_background_images(self):
        self.bg_height = self.screen_h - self.ground_height

        bg_raw = pygame.image.load('img/bg.png')
        self.bg = pygame.transform.scale(bg_raw, (self.screen_w, self.bg_height))

        ground_raw = pygame.image.load('img/ground.png')
        self.ground_img = pygame.transform.scale(ground_raw, (self.screen_w + 35, self.ground_height))

    def ground_scroll_animation(self):
        self.ground_scroll -= 5

        if abs(self.ground_scroll) >= 35:
            self.ground_scroll = 0

    def spawn_pipes(self):
        now = pygame.time.get_ticks()
        if now - self.last_pipe_shown >= self.pipe_freq:
            rand_pos = random.randint(-180, 50)
            self.pipe_group.add(pipe.Pipe(self.screen_w, self.mid_screen + rand_pos, 1))
            self.pipe_group.add(pipe.Pipe(self.screen_w, self.mid_screen + rand_pos, -1))
            self.last_pipe_shown = now

    def draw(self):
        self.screen.blit(self.bg, (0, 0))
        self.pipe_group.draw(self.screen)
        self.screen.blit(self.ground_img, (self.ground_scroll, self.bg_height))
        self.bird_group.draw(self.screen)
        font = pygame.font.Font(None, 36)
        
        text_surface = font.render(str(self.score), True, (255, 255, 255))

        text_rect = text_surface.get_rect(center=(self.screen_w // 2, 100))
        self.screen.blit(text_surface, text_rect)

    def restart(self):
        self.score = 0
        self.pipe_group.empty()
        self.flappy.restart()
        self.last_pipe_shown = pygame.time.get_ticks() - self.pipe_freq
        self.bird_passed_pipe = False
        self.game_state = "running"

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_state == "running":
                    self.flappy.jump()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.game_state == "running":
                        self.flappy.jump()

    def update_score(self):
        if len(self.pipe_group) > 0:
            if self.bird_group.sprites()[0].rect.x > self.pipe_group.sprites()[0].rect.x and\
                self.bird_passed_pipe == False:
                self.score += 1
                self.bird_passed_pipe = True
            self.bird_passed_pipe = self.bird_group.sprites()[0].rect.x > self.pipe_group.sprites()[0].rect.x

    def check_collision(self):
        if pygame.sprite.groupcollide(self.bird_group, self.pipe_group, False, False):
            self.game_state = "game_over"
            
    def update(self):
        if self.game_state == "running":
            self.ground_scroll_animation()
            self.pipe_group.update()
            self.update_score()
            self.check_collision()
            self.spawn_pipes()
        self.bird_group.update() 

        if self.flappy.alive == False:
            self.game_state = "game_over"

    def run(self):
        self.load_background_images()
        self.bird_group.add(self.flappy)
        
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
         
            if self.game_state == "game_over":
                btn_rect = self.restart_btn.get_rect(center=(self.screen_w // 2, self.screen_h // 2))
                self.screen.blit(self.restart_btn, btn_rect)

                mouse_pos = pygame.mouse.get_pos()
                is_pressed = pygame.mouse.get_pressed()[0]
                if is_pressed and btn_rect.collidepoint(mouse_pos):
                    self.restart()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()


if __name__ == "__main__":
    g = Game().run()