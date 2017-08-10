import math
import random
import pygame
import player as player_module
import client as client_module

class Hack():
    def __init__(self,client, player,screen,map,network):
        self.client = client
        self.player = player
        self.screen = screen
        self.network = network
        self.map = map

        self.noclip= False
        self.count = 0
        self.spinCount = 0

        self.preKeys = pygame.key.get_pressed()


    def update(self,player):
        #Get keys
        keys = pygame.key.get_pressed()

        #NoClip
        if(keys[pygame.K_LCTRL]):
            self.noclip = True
        else:
            self.noclip = False

        #Shift Controls
        if(keys[pygame.K_LSHIFT] and self.count%4 == 0):
            #Speed Modifier
            if keys[pygame.K_PERIOD] and not self.preKeys[pygame.K_q]:
                player.step += 1
                print("Speed set to:",player.step)
            if keys[pygame.K_COMMA] and not self.preKeys[pygame.K_e]:
                player.step -= 1
                print("Speed set to:",player.step)
            #Nuker
            if(keys[pygame.K_SEMICOLON] and not self.preKeys[pygame.K_SEMICOLON]):
                 position = (self.map.get_map_pos(-1337,-1337))
                 self.client.cast = player.attack(player_module.Action(player.current_spell),(0,0),client_module.projectile_paths[player.current_spell])
                 player.cast_spells[-1].set_properties((position[0],position[1],0,0,player.current_spell))
                 print("Nuker Activated")
            
            self.preKeys = keys

            #Ring of death
            if(keys[pygame.K_SPACE]):
                 velocity = (math.sin(self.spinCount),math.cos(self.spinCount))
                 self.client.cast = player.attack(player_module.Action(self.player.current_spell),velocity,client_module.projectile_paths[0])
                 self.spinCount += 0.6
                 player.addMana(10)

                 

        self.count += 1
