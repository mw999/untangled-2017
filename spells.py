import client
import time

def ability_arrow():
    if client.g.me.can_fire_ability:
        client.g.cast = client.g.me.attack(client.g.Action.SPELL, client.g.last_direction, client.g.arrow_image_path)
    
def ability_step():
    client.g.me.step = 2
    client.g.me.steptime = time.time()
    client.g.me.can_step_ability = False
