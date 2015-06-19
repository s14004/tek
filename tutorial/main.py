'''
import pyglet
from tutorial import resources

window = pyglet.window.Window()


@window.event
def on_draw():
    window.clear()
    sprite_bach.draw()

@window.event
def on_key_press(symbol, modifiers):
    form pyglet.window import key
    if symbol == key.LEFT:
        owl_sprites[0].x -= 1
    elif symbol == key.RIGHT
        owl_sprites[0].x

def update(dt):
    pass

if __name__ == '__main__':
    sprite = pyglet.sprite.Sprite(resources.owl)
    pyglet.clock.schedule_interval(update, 0.5)
    pyglet.app.run()
    '''
