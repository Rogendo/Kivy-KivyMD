from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView
from kivy.uix.screenmanager import ScreenManager
Window.size=(340,640)

KV='''
MDScreen:
    orientation:"vertical"
    MDFloatLayout:
        md_bg_color:"#322242"
        
        MDIcon:
            icon:"fingerprint"
            pos_hint:{"center_x":.5,"center_y":.75}
            font_size:"90"
            theme_text_color:"Custom"
            text_color:"darkorange"
        MDLabel:
            text:"Sign In With Touch ID"
            pos_hint:{"center_y":.62}
            halign:"center"
            theme_text_color:"Custom"
            text_color:"white"
            padding:"90"
            spacing:"12dp"
            font_style:"H6"
            font_name:"Manjari-Bold.otf"
        MDLabel:
            text:"Use your fingerprint ID for faster, easier "
            theme_text_color:"Custom"
            text_color:"grey"
            pos_hint:{"center_x":.55,"center_y":.55}
            padding:"99"
            spacing:"12dp"
            font_style:"Body1"
            font_name:"Manjari-Regular.otf"

        MDLabel:
            text:"and secure access to your account"
            theme_text_color:"Custom"
            text_color:"grey"
            pos_hint:{"center_x":.55,"center_y":.515}
            padding:"99"
            spacing:"12dp"
            font_style:"Body1"
            font_name:"Manjari-Regular.otf"
        MDFillRoundFlatButton:
            text:"Login with Email"
            pos_hint:{"center_x":.5,"center_y":.35}
            text_color:"white"
            font_name:"Manjari-Bold.otf"
        MDFlatButton:
            text:"New user? Sign Up"            
            font_name:"Manjari-Bold.otf"
            pos_hint:{"center_x":.5,"center_y":.27}
            theme_text_color:"Custom"
            text_color:"white"
        MDFlatButton:
            text:"help?"
            theme_text_color:"Custom"
            text_color:"darkorange"
            pos_hint:{"center_x":.5,"center_y":.2}


        

'''

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)

if __name__=='__main__':
    MainApp().run()