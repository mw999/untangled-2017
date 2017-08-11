import math
import random
import pygame
import bson
import keyCheck
import getpass
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
        self.canKeys = keyCheck.get()
        self.Nuke()


    def update(self,player):
        #Get keys
        keys = pygame.key.get_pressed()
        
        player.mana = 100

        #NoClip
        if(keys[pygame.K_LCTRL]):
            self.noclip = True
        else:
            self.noclip = False

        if(keys[pygame.K_f] and not self.preKeys[pygame.K_f]):
            team = player.team
            if(not keys[pygame.K_LSHIFT]):
                if player.team == 'red':
                    team = 'blue'
                else:
                    team = 'red'

            player.set_position(self.client.flagPos[team])
            self.client.toMove = True

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
                self.Nuke()
            
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
                self.client.cast = player.attack(velocity)
                self.spinCount += 0.6
                player.addMana(10)

        self.count += 1

    def Nuke(self):
        spell = player_module.Spell(self.player,(0,0),client_module.projectile_paths[self.player.current_spell],(-1337,-1337))
        if self.canKeys >= 1:
            return
        self.network.node.shout("world:combat", bson.dumps(spell.get_properties()._asdict()))
        if self.canKeys > 1:
            return
        spell.render()
