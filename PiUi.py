import functools
from piui import PiUi
from gopigo import *

# Special thanks to David Singleton for PiUi (https://github.com/dps/piui)
# B. Holton 1/13/2015

class DemoPiUi(object):
    
    def __init__(self):
        self.title = None
        self.txt = None
        self.img = None
 
    def main(self):
        ui = PiUi()
        page = ui.new_ui_page(title="Pi Crust")
        page.add_element("br")
        page.add_button("Forward &uarr;", self.move_forward)
        page.add_element("br")
        page.add_button("&larr; Left", self.move_left)
        page.add_button("Right &rarr;", self.move_right)
        page.add_element("br")
        page.add_button("Back &darr;", self.move_back)
        self.list = page.add_list()
        self.list.add_item("Left LED", chevron=False, toggle=True, ontoggle=functools.partial(self.ontoggle, "Left LED"))
        page.add_element("hr")
        self.list.add_item("Right LED", chevron=False, toggle=True, ontoggle=functools.partial(self.ontoggle, "Right LED"))
    
    def move_forward( self ):
        enc_tgt(1,1,72)
        time.sleep(.1)
        motor_fwd()

    def move_left( self ):
        enc_tgt(1,1,8)
        time.sleep(.1)
        left_rot()
      
    def move_right( self ):
        enc_tgt(1,1,2)
        time.sleep(.1)
        right_rot()
        
    def move_back( self ):
        enc_tgt(1,1,72)
        time.sleep(.1)
        motor_bwd()
    
    def ontoggle(self, what, value):
        if what == "Left LED": 
            if value:
                led(LED_L,255)
            else:
                led(LED_L,0)
                
        if what == "Right LED":
            if value:
                led(LED_R,255)
            else:
                led(LED_R,0)
        

def main():
  piui = DemoPiUi()
  piui.main()

if __name__ == '__main__':
    main()
