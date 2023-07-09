from pynput.keyboard import Key, Controller, Listener

key = Controller()

total_inputs = 0


def on_press(key):
    global total_inputs

    if key != Key.esc:
        total_inputs += 1
    else:
        print(f"\n{total_inputs}")
        liste.stop()


with Listener(on_press=on_press) as liste:
    liste.join()
