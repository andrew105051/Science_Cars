from pycat.core import Window, Sprite, Scheduler, RotationMode, Label, Color, KeyCode
import random

#width=1365

window = Window(width=700, height=335, enforce_window_limits=False)#(background_image='bg.jpg', width=600, height=335)
#window.background_sprite.scale = 1.5



class BG(Sprite):
    def on_create(self):
        self.scale = 1.5
        self.x = 680
        self.y = 167.5
        self.layer = -15
        self.image = 'bg.jpg'
    def on_update(self, dt):
        if window.is_key_pressed(KeyCode.D):
            self.x += -1

        if window.is_key_pressed(KeyCode.D):
            self.x += -1        


bg = window.create_sprite(BG)
bg = window.create_sprite(BG, x = 2040)
bg = window.create_sprite(BG, x = 3400)
#player = window.create_sprite(Player)
#bullet = window.create_sprite(Bullet)
#enemy=window.create_sprite(Enemy)
#enemy_bullet = window.create_sprite(Enemy_bullet)

#Scheduler.update(lambda: window.create_sprite(Enemy),3)


window.run()