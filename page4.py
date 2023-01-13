from kivy.lang import Builder
from kivymd.app import MDApp

KV="""
MDScreen:
    orientation:"vertical"
    MDLabel:
        text:"Log in Form"
        pos_hint:{"center_y":.9}
        halign:"center"
        font_style:"H5"
        font_name:"Manjari-Bold.otf"
    MDSeparator:
        height:"1dp"
        
    MDCard:
        size_hint:None,None
        size:"600dp","300dp"
        pos_hint:{"center_x":.5,"center_y":.5}
        md_bg_color:"orange"

"""
class Main(MDApp):
    def build(self):
        self.theme_cls.theme_style="Light"
        self.theme_cls.primary_palette="Pink"
        return Builder.load_string(KV)

if __name__=="__main__":
    Main().run()
