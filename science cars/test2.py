from pycat.core import Window, Sprite, Scheduler, RotationMode, Label, Color, KeyCode
import random

#width=1365

window = Window(width=700, height=335, enforce_window_limits=False)#(background_image='bg.jpg', width=600, height=335)
#window.background_sprite.scale = 1.5

class Player(Sprite):
    def on_create(self):
        self.scale = 50
        self.x = 50
        self.y = 70
        self.layer = 10
        self.image = 'car.png'
    def on_update(self, dt):
        #if window.is_key_pressed(KeyCode.A):
            #self.x += -4
        #if window.is_key_pressed(KeyCode.D):
            #self.x += 4
        if window.is_key_pressed(KeyCode.W):
            self.y += 2
        if window.is_key_pressed(KeyCode.S):
            self.y += -2
        if self.is_touching_any_sprite_with_tag('enemy'):
            self.delete()
            window.close()


player = window.create_sprite(Player)
#bullet = window.create_sprite(Bullet)
#enemy=window.create_sprite(Enemy)
#enemy_bullet = window.create_sprite(Enemy_bullet)

#Scheduler.update(lambda: window.create_sprite(Enemy),3)


window.run()