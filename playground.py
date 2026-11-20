# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True

background = pygame.image.load("img/bg.png")
scaled_bg = pygame.transform.scale(background, (500,500))
# pipe = pygame.image.load("img/pipe.png")

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/bird1.png")
        self.selected_image = 0
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

bird_group = pygame.sprite.Group()
flabby = Bird(250, 250)
bird_group.add(flabby)
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.blit(scaled_bg, (0,0))
    bird_group.draw(screen)
    screen.blit(pygame.image.load("img/bird1.png"), (250, 250))
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()