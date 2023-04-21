from pygame import *
from random import *

speed_x = 7
speed_y = 7

razreshenie = 1000, 628
clock = time.Clock()
FPS = 60

window = display.set_mode((razreshenie))
game = True
display.set_caption('Пинг-понг')
background = transform.scale(image.load('galaxy.jpg'), (razreshenie))


class GameSprite(sprite.Sprite):
    def __init__(self, image_p, speed, rect_x, rect_y, width, height):
        super().__init__()
        self.image = transform.scale(image.load(image_p), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
        self.width = width
        self.height = height

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < razreshenie[1] - self.height - 5:
            self.rect.y += self.speed

    def update_r(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < razreshenie[1] - self.height - 5:
            self.rect.y += self.speed




font.init()
font1 = font.SysFont('Arial', 40)
font2 = font.SysFont('Arial', 20)
win1 = font1.render('player 1 win', True, (255, 0, 0))
win2 = font1.render('player 2 win', True, (0, 255, 0))

player1 = Player("rocket.png", 10, 100, 200, 40, 150)
player2 = Player("rocket.png", 10, 900, 200, 40, 150)

ball = GameSprite('hhh.png', 7, 300, 300, 50,50)



finish = False

while game:
    if finish != True:
        window.blit(background, (0, 0))
        player1.reset()
        player1.update_l()
        player2.reset()
        player2.update_r()
        ball.reset()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y < 0 or ball.rect.y > 628 - 50:
            speed_y *= -1

        if sprite.collide_rect(ball, player1):
            speed_x *= -1

        if sprite.collide_rect(ball, player2):
            speed_x *= -1

        if ball.rect.x < 0:
            window.blit(win2, (200, 200))

        if ball.rect.x > 1000:
            window.blit(win1, (200, 200))








    for e in event.get():
        if e.type == QUIT:
            game = False


    display.update()
    clock.tick(FPS)
