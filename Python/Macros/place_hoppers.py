# I made this to place a lot of hoppers in Minecraft (over 816)

from pyKey import press
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Listener
from threading import Thread
import time

time.sleep(3)
mouse = Controller()


def space_thread():
    press("SPACEBAR", 24)


def l_shift_thread():
    press("LSHIFT", 24)


def on_press(key):
    if key == Key.alt_r:
        space_t = Thread(target=space_thread).start()
        l_shift_t = Thread(target=l_shift_thread).start()
        mouse.press(Button.right)
        time.sleep(24)

        mouse.release(Button.right)


with Listener(on_press=on_press) as listener:
    listener.join()
