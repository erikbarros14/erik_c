import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus, Large_Cactus# importei o cacto maior
from dino_runner.components.obstacles.bird import Bird # importei arquivo do passaro
from dino_runner.utils.text_utils import draw_message_component
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD # importei variáveis globais



class ObstacleManager:
    def __init__ (self):
        self.obstacles = []

    def update (self, game):
        if len(self.obstacles) == 0: # se o tamanho da lista for 0 e é
            item = random.randint(0, 2)
            if item == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS)) # o small cactus
            elif item == 1:
                self.obstacles.append(Large_Cactus(LARGE_CACTUS))
            elif item == 2:
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles: # para cada obstaculo que aparecer 
            obstacle.update(game.game_speed, self.obstacles) # mostra o obstaculo
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                
                    game.score -= 1
                    game.game_speed = 20 
                    pygame.time.delay(500) 
                    game.playing = False 
                    game.death_count += 1 
                    break
                
                elif game.player.type == 'hammer':
                    self.obstacles.remove(obstacle)
                    #game.score += 100  
                    
                    #fonte = pygame.font.SysFont('arial', 40, True, False)
                    #texto = "+100 Score"
                    #formatext = fonte.render(texto, True, (0, 0, 0))
                    #game.screen.blit(formatext, (370, 130))

                elif game.player.type == 'shield':
                    self.obstacles.remove(obstacle)
                elif game.player.type == 'default':
                    pass

    def draw (self, screen): # desenhar na tela
        for obstacle in self.obstacles: # para cada obstaculo
            obstacle.draw(screen) # mostra na tela ele

    def reset_obstacles (self):
        self.obstacles = []