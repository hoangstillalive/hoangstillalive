import datetime
# print(time.hour, time.minute)
while True:
    time = datetime.datetime.now()
    if ((time.hour == 8) and (time.minute == 41)):
        import pyglet
        music = pyglet.resource.media('cello.wav')
        music.play()
        pyglet.app.run()