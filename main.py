from game import *
import pygame

if __name__ == '__main__':


        running = True
        clock = pygame.time.Clock()
        game = Game(pygame.display.set_mode((WIDTH, HEIGHT))
)

        while running:
            clock.tick(FPS)

            draw(pygame.display.set_mode((WIDTH, HEIGHT)), game.matrix, game.cells, game.score, game.over)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        game.left()
                    if event.key == pygame.K_RIGHT:
                        game.right()
                    if event.key == pygame.K_UP:
                        game.up()
                    if event.key == pygame.K_DOWN:
                        game.down()
                    if event.key == pygame.K_q and pygame.key.get_mods() & pygame.KMOD_CTRL and game.over:
                        game.reset()

        pygame.quit()
        quit()

