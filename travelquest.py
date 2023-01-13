from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.widget import  Widget
from kivy.core.window import Window

Window.size=(340,640)
KV='''

MDScreen:
    orientation:"vertical"
    # md_bg_color:"lightblue"
    
    MDLabel:
        text:"Travel Quest"
        font_style:"H6"
        font_name:"font2.pfb"
        padding_x:"5dp"
        # pos_hint:{"center_x":.5,"center_y":.5}
    MDSmartTile:
        radius:50
        box_radius:[0,0,24,24]
        box_color:"lightblue"
        source:"assets/jane.jpg"
        pos_hint:{"center_x":.5,"center_y":.6}
        size_hint: None, None
        size: "320dp", "320dp"
    MDRaisedButton:
        text: "Sign In"
        md_bg_color: "lightgreen"
        pos_hint:{"center_x":.5,"center_y":.3}
    MDRaisedButton:
        text: "Sign Up"
        md_bg_color: "lightblue"
        pos_hint:{"center_x":.5,"center_y":.2}

        

            
'''


class TravelQuest(MDApp):
    def build(self):
        return Builder.load_string(KV)


if __name__=='__main__':
    TravelQuest().run()