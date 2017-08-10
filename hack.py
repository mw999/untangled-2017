import math
import random
import pygame
import bson
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
                print("Nuker Activated")
                spell = player_module.Spell(player,(0,0),client_module.projectile_paths[player.current_spell],(-1337,-1337))
                self.network.node.shout("world:combat", bson.dumps(spell.get_properties()._asdict()))
            
            self.preKeys = keys

            #Ring of death
            if(keys[pygame.K_SPACE]):
                for i in range(0,30):
                    velocity = (math.sin(i),math.cos(i))
                    spell = player_module.Spell(player,velocity,client_module.projectile_paths[player.current_spell])
                    self.network.node.shout("world:combat", bson.dumps(spell.get_properties()._asdict()))

            #Spiral Shot
            if(keys[pygame.K_RETURN]):
                velocity = (math.sin(self.spinCount),math.cos(self.spinCount))
                self.client.cast = player.attack(velocity,client_module.projectile_paths[player.current_spell])
                self.spinCount += 0.6
                player.addMana(10)

                 

        self.count += 1
