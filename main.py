import pygame as pg
import sys, random, os

def message(msg, color, x, y):
    msg = str(msg)
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, (x, y))

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)

path1 = resource_path('sound1.wav')
path2= resource_path('sound2.wav')
path3 = resource_path('sound3.wav')


results = [0]
count = 0
last_count = 0
w, h = 1200, 800
rectw = 60
color = (255,0,125)
btn_color = (255,0,200)
btn_pressed = False
s = 10
tick = 0

pg.init()
window = pg.display.set_mode((w,h))
fps = pg.time.Clock()

rect1 = pg.Rect(random.randint(rectw, w-rectw), random.randint(rectw+90, h-rectw), rectw,rectw)
button = pg.Rect(w/2-500, 10, 200, 50)

sound1 = pg.mixer.Sound(path1)
sound2 = pg.mixer.Sound(path2)
sound3 = pg.mixer.Sound(path3)
sound2.set_volume(0.2)
sound3.set_volume(0.3)

font_style = pg.font.Font(None, 56)
while True:
    window.fill(color, rect = rect1)
    window.fill(btn_color, rect = button)
    pressed = pg.mouse.get_pressed()
    pos = pg.mouse.get_pos()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    if pg.mouse.get_focused():
        if pressed[0]:
            if rect1.x <= pos[0] <= rect1.x+rectw and rect1.y <= pos[1] <= rect1.y+rectw:
                window.fill((0,0,0),rect1)
                rect1.update(random.randint(rectw, w-rectw), random.randint(rectw+150, h-rectw), rectw,rectw)
                sound1.play()
                if btn_pressed:
                    count += 1
            if button.x <= pos[0] <= button.x + button.width and button.y <= pos[1] <= button.y + button.height:
                btn_pressed = True
                window.fill((0, 0, 0), (w / 2 - 250, 100, w / 2 + 250, 50))
    if btn_pressed:
        tick += 1
        if tick % 30 == 0:
            s-=1
            if s==0:
                btn_pressed = False
                sound2.play()
                if count > max(results) and s == 00:
                    message(f"НОВЫЙ РЕКОРД: {count}", (0,125,255), w / 2 -250, 100)
                    sound3.play()
                s = 10
                results.append(count)
                count = 0

    fps.tick(30)
    text_surface = font_style.render(f'Time: {s} sec', True, color)
    text_width, text_height = text_surface.get_size()[0]+30, text_surface.get_size()[1]
    text_x, text_y = w/2-250, 10
    # Заполняем область с текстом сплошным чёрным цветом
    window.fill((0, 0, 0), (w/2-150, 0, w/2+250, 90))
    window.blit(text_surface, (text_x, text_y))
    message("START", (0,100,255), button.center[0]-60, button.y+5)
    message(f"Кол-во очков: {count}", color, w/2-250, 55)
    message(f"Прошлый результат: {results[-1]}", color, w/2+100, 10)
    message(f"Рекорд: {max(results)}", color, w/2+100, 55)
    pg.display.update()