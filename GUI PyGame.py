import pygame


def block_moment(screen, block, x, y):  # screen: object of window, block: image object, x & y: coordinates
    screen.fill((78, 56, 78))
    screen.blit(block, (x, y))
    pygame.display.flip()


def game():
    pygame.init()
    size = (500, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('PyGame')

    # adding background
    screen.fill((78, 56, 78))

    # load resources
    block = pygame.image.load('block.png').convert()
    x = 0
    y = 0
    screen.blit(block, (x, y))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y -= 10
                    block_moment(screen, block, x, y)
                elif event.key == pygame.K_DOWN:
                    y += 10
                    block_moment(screen, block, x, y)
                elif event.key == pygame.K_RIGHT:
                    x -= 10
                    block_moment(screen, block, x, y)
                elif event.key == pygame.K_LEFT:
                    x += 10
                    block_moment(screen, block, x, y)
            elif event.type == pygame.QUIT:
                running = False

        # update the screen
        pygame.display.flip()


if __name__ == '__main__':
    game()
