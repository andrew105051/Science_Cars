

from pycat.core import Window, Sprite, Scheduler, RotationMode, Label, Color, KeyCode, Player
import random


from random import randint
import random



soundlose = Player('Car Horn2.wav')

soundshoot = Player('Pew.wav')

soundstart = Player('Whistle.wav')

soundcoin = Player('Coin.wav')

gamemusic = Player('music.wav')

gamewin = Player('Win.wav')

gameover = Player('Lose.wav')


#h=335


#width=1365


window = Window(width=700, height=335, enforce_window_limits=False)


#(background_image='bg.jpg', width=600, height=335)


#window.background_sprite.scale = 1.5


score_label = window.create_label()

score_label.font_size = 25

score_label.text = '0'

score_label.x = 25

score_label.y = 300

score_label.layer = 100

score = 0




class BG(Sprite):
    def on_create(self):
        self.scale = 1.5
        self.x = 680
        self.y = 167.5
        self.layer = -15
        self.image = 'bg.jpg'
        soundstart.play()
        gamemusic.play()
    def on_update(self, dt):
            self.x += -2
            if 'endbg' in self.tags and self.x < 350 and self.x > 340:
                window.create_sprite(win)
                playcar.delete()
                gamemusic.pause()
                gamewin.play()
                enemy.delete()
                coin.delete()
                bullet.delete()
                self.delete()
                score_label.text = str(score)                     



class Playcar(Sprite):
    def on_create(self):
        self.scale = 0.35
        self.x = 65 
        self.y = 70
        self.layer = 10
        self.image = 'car2d.png'
        self.add_tag('car')
    def on_update(self, dt):
        #if window.is_key_pressed(KeyCode.A):
            #self.x += -4
        #if window.is_key_pressed(KeyCode.D):
            #self.x += 4
        if window.is_key_pressed(KeyCode.W)and self.y < 75:
            self.y += 1.5
        if window.is_key_pressed(KeyCode.S)and self.y > 5:
            self.y += -1.5
        if self.is_touching_any_sprite_with_tag('enemy'):
            soundlose.play()
            #self.delete()
            #Scheduler.wait(2, window.close)
        if score < 0:
            window.create_sprite(lose)
            gamemusic.pause()
            gameover.play()
            self.delete()    
        if window.is_key_down(KeyCode.SPACE):
            window.create_sprite(Bullet, position = self.position) 
            soundshoot.play()
        


class Bullet(Sprite):
    def on_create(self):
        self.scale = 0.08
        self.add_tag('bullet')
        self.image = 'laser.png'
        self.timer = 0
    def on_update(self, dt):
        self.move_forward(10)
        if self.is_touching_window_edge():
            self.delete()
        if self.is_touching_any_sprite_with_tag('enemy'):
            Scheduler.wait(0.5, self.delete)
            self.delete()
        if window.is_key_down(KeyCode.SPACE):
           global score
           score += -1
           score_label.text = str(score)



class Enemy(Sprite):
    def on_create(self):
        self.scale =0.25
        self.image = 'fly.png'
        self.y = random.randint(10, 120)
        self.x = 700
        self.add_tag('enemy')
        self.timer = 0
        self.layer = 10
    def on_update(self, dt):  
        if self.x < 0 :
            self.delete()
        self.x += -6 
        if self.is_touching_any_sprite_with_tag('bullet'):
            Scheduler.wait(0.01, self.delete)
            self.delete()
        if self.is_touching_any_sprite_with_tag('car'):
            soundlose.play()
            Scheduler.wait(0.2, self.delete)
            global score
            score += -5
            score_label.text = str(score)
            self.delete()   


        
class Coin(Sprite):
    def on_create(self):
        self.scale =0.05
        self.image = 'coin.png'
        self.y = random.randint(10, 80)
        self.x = 700
        self.add_tag('money')
    def on_update(self, dt): 
        if self.x < 0 :
            self.delete() 
        self.x += -2
        if self.is_touching_any_sprite_with_tag('car'):
            global score
            score += 1
            score_label.text = str(score)
            soundcoin.play()
            self.delete()           



class Lose(Sprite):
    def on_create(self):
        self.image = 'lose.png'
        self.x = 350
        self.y = 167.5
        self.scale = 1.85
        self.timer = 0
        self.layer = 50
    def on_update(self, dt):  
        self.timer += dt
        if self.timer > 2.5 :
            window.close()
        elif self.timer > 0 :
            pass



class Win(Sprite):
    def on_create(self):
        self.image = 'win.png'
        self.x = 350
        self.y = 167.5
        self.scale = 0.4
        self.timer = 0
        self.layer = 50
    def on_update(self, dt):  
        self.timer += dt
        if self.timer > 4.5 :
            window.close()
        elif self.timer > 2 :
            self.image = 'newyear.jpg'
            self.scale = 1.07
        elif self.timer > 0 :
            pass




bg = window.create_sprite(BG)

bg = window.create_sprite(BG, x = 2040)

bg = window.create_sprite(BG, x = 3400)

bg = window.create_sprite(BG, x = 4760, tag = 'endbg')#+1360

lose = Lose

win = Win

playcar = window.create_sprite(Playcar)

bullet = window.create_sprite(Bullet)

enemy=window.create_sprite(Enemy)

coin=window.create_sprite(Coin)


#enemy_bullet = window.create_sprite(Enemy_bullet)


Scheduler.update(lambda: window.create_sprite(Coin),1.2)

Scheduler.update(lambda: window.create_sprite(Enemy),1.2)


window.run()



#wasd

#space to shoot (min -1)

#car crash min -5

#point less then 0 game over

#after 4 laps win

# let's play !  

