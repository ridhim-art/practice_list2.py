import pyautogui as pg
sw, sh = pg.size()

def activate_right_software():
    pg.moveTo(x=sw//2+300,y=sh//2)
    pg.click()

def activate_left_software():
    pg.moveTo(x=sw//3,y=sh//2,duration=2)
    pg.click()

def play_or_pause():
    activate_right_software()
    pg.press('space')

def volume_up():
    activate_right_software()
    pg.press('up')

def volume_down():
    activate_right_software()
    pg.press('down')


def forward():
    activate_right_software()
    pg.press('right')

def backward():
    activate_right_software()
    pg.press('left')



