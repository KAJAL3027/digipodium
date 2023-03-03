import pgzrun

# music bgm music
# music.play('bg)

b = rect((50,50),(100,50))
vx,vy = 1,1

def draw():
    screen.fill("black")
    screen.draw.filled_rect(b,'blue')

def update():
    global vx,vy
    b.y += vx
    if b.right > 80 or b.left < 0:
         vx = -vx
    if b.bottom > 600 or b.top < 0:
        vx = -vy

#outside of all function
pgzrun.go()