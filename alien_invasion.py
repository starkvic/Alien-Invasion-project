from msilib.schema import Class
import sys
import pygame

class AlienInvasion:
    """Overall class to manage game assests and behaviour"""

    def __init__(self):
        #initialize the game, and create game resources.
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        #start the main loop for the game.
        while True:
            #Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #make most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    #make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()