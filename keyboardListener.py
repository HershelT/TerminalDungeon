from pynput import keyboard

# Define a key listener
class MyKeyListener:
    def __init__(self, key_actions={}):
        self.keys_pressed = set()
        self.key_actions = key_actions
        self.user_input= None
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
    def is_r_pressed(self):
        return "'r'" in self.keys_pressed
    def is_g_pressed(self):
        return "'g'" in self.keys_pressed
    def is_b_pressed(self):
        return "'b'" in self.keys_pressed
    def is_y_pressed(self):
        return "'y'" in self.keys_pressed
    def is_m_pressed(self):
        return "'m'" in self.keys_pressed
    def is_c_pressed(self):
        return "'c'" in self.keys_pressed
    def is_w_pressed(self):
        return "'w'" in self.keys_pressed
    def is_0_pressed(self):
        return "'0'" in self.keys_pressed
    def is_1_pressed(self):
        return "'1'" in self.keys_pressed
    
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
    def is_tab_pressed(self):
        return "Key.tab" in self.keys_pressed
    def is_space_pressed(self):
        return "Key.space" in self.keys_pressed
    
    
    
    def check_keys(self):
        for key in list(self.keys_pressed):  # Create a copy of self.keys_pressed
            if key in self.key_actions:
                self.key_actions[key]()
        

#when getting keyboard input type in:
    # key_listener = MyKeyListener()
    #         listener = keyboard.Listener(
    #             on_press=key_listener.on_press,
    #             on_release=key_listener.on_release)