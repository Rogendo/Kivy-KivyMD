from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView
from kivy.uix.screenmanager import ScreenManager
Window.size=(340,640)

KV='''

MDScreen:
    name:"main"
    
    MDFloatLayout:
        md_bg_color:"#322242"
        BoxLayout:
            orientation:"vertical"
    
                
    
        MDLabel:
            text:"There's a lot happening around you!"
            font_name:"Manjari-Bold.otf"

            allow_selection:True
            allow_copy:True
            theme_text_color:"Custom"
            text_color:"white"
            font_style:"H5"
            padding:"99"
            spacing:"18dp"
            pos_hint:{"center_x":.5,"center_y":.4}

        MDLabel:
            font_style:"Body1"
            text:"Our mission is to provide whats happening near you, browse and search, for the type of events you like to attend."
            theme_text_color:"Custom"
            text_color:"grey"
            font_name:"Manjari-Regular.otf"

            pos_hint:{"center_x":.5,"center_y":.3}
            padding:"99"
            spacing:"20"
        MDFloatingActionButton:
            icon:"arrow-right-circle"
            pos_hint:{"center_x":.86,"center_y":.1}
    MDRoundFlatButton:
        text:""
        pos_hint:{"center_x":.15,"center_y":.1}
        height:"10"

    MDRoundFlatButton:
        text:""
        height:"10"
        fill:True
        pos_hint:{"center_x":.37,"center_y":.1}
    MDRoundFlatButton:
        text:""
        height:"10"
        pos_hint:{"center_x":.59,"center_y":.1}
    MDCard:
        orientation:"vertical"
        size_hint:None,None
        size:"500dp","330dp"
        pos_hint:{"center_x":.5,"center_y":.7}
        md_bg_color:"#322242"
        
        Image:
            source:"assets/2.png"
            elevation:4.5
            shadow_offset:0,6
'''

class MainUI(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.theme_style = "Light"

        return Builder.load_string(KV)

if __name__=="__main__":
    MainUI().run()