import math
import random
import pygame
import player as player_module

class Hack():
    def __init__(self,player,screen,map,network):
        self.player = player
        self.screen = screen
        self.network = network
        self.map = map

        self.noclip= False
        self.inputCool = 0


    def update(self,player):
        #Get keys
        keys = pygame.key.get_pressed()

        #NoClip
        if(keys[pygame.K_LCTRL]):
            self.noclip = True
        else:
            self.noclip = False

        #Shift Controls
        if(keys[pygame.K_LSHIFT]):
            #Speed Modifier
            if(self.inputCool == 0):
                if keys[pygame.K_w]:
                    player.step += 1
                    self.inputCool = 4
                    print("Speed set to:",player.step)
                if keys[pygame.K_s]:
                    player.step -= 1
                    self.inputCool = 4
                    print("Speed set to:",player.step)
            else:
                self.inputCool -= 1

            #Ring of death
            if(keys[pygame.K_SPACE]):
                for i in range(0,30):
                     player.attack(player_module.Action.SPELL,(math.sin(i),math.cos(i)),(player.x,player.y))
