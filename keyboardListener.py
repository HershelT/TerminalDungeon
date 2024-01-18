from pynput import keyboard

# Define a key listener
class MyKeyListener:
    def __init__(self):
        self.keys_pressed = set()

    def on_press(self, key):
        self.keys_pressed.add(str(key))

    def on_release(self, key):
        self.keys_pressed.discard(str(key))

    def is_pressed(self, key):
        return str(key) in self.keys_pressed

    #define what keys can be pressed
    def is_s_pressed(self):
        return "'s'" in self.keys_pressed
    def is_x_pressed(self):
        return "'x'" in self.keys_pressed
    def is_f_pressed(self): 
        return "'f'" in self.keys_pressed
    
    #Non keyboard charcters like enter 
    def is_left_arrow_pressed(self):
        return "Key.left" in self.keys_pressed
    def is_right_arrow_pressed(self):
        return "Key.right" in self.keys_pressed
    def is_up_arrow_pressed(self):
        return "Key.up" in self.keys_pressed
    def is_down_arrow_pressed(self):
        return "Key.down" in self.keys_pressed
    def is_enter_pressed(self):
        return "Key.enter" in self.keys_pressed

#when getting keyboard input type in:
    # key_listener = MyKeyListener()
    #         listener = keyboard.Listener(
    #             on_press=key_listener.on_press,
    #             on_release=key_listener.on_release)