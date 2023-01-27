import pyglet
from pyglet.window import key
from pyglet import image

window = pyglet.window.Window()

player_left_img = pyglet.image.load('mac_left.png')
player_right_img = pyglet.image.load('mac_right.png')
player2 = pyglet.sprite.Sprite(player_left_img, x=100, y=100)


keys = key.KeyStateHandler()
window.push_handlers(keys)

def update(dt):
    if keys[key.W]:
        player2.y += dt * 120
    if keys[key.S]:
        player2.y += dt * -120
    if keys[key.A]:
        player2.x += dt * -120
    if keys[key.D]:
        player2.x += dt * 120
pyglet.clock.schedule_interval(update, 1/120.0)

@window.event
def on_draw():
    window.clear()
    player2.draw()

pyglet.app.run()