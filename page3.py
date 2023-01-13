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
    md_bg_color:"#1a1b54"

    MDFloatLayout:
        MDSmartTile:
            radius: 150
            box_radius: [24, 24, 24, 24]
            source: "assets/jane.jpg"
            pos_hint: {"center_x": .1, "center_y": .95}
            size_hint: None, None
            size: "50dp", "50dp"
        MDLabel:
            text:"Hi, Jane!"
            pos_hint: {"center_x": .72, "center_y": .95}
            theme_text_color:"Custom"
            text_color:"white"
            font_name:"Manjari-Bold.otf"
        MDIconButton:
            icon:"bell-badge-outline"
            theme_text_color:"Custom"
            text_color:"white"
            pos_hint: {"center_x": .9, "center_y": .95}
            

        MDCard:
            text:"card"
            orientation:"vertical"
            size_hint:None,None
            size:"150dp","110dp"
            pos_hint:{"center_x":.25,"center_y":.8}
            md_bg_color:"#282878"
            radius:"25dp"
            # MDIconButton:
            #     icon:"dots-vertical"
            #     pos_hint:{"top":1,"right":1}
            MDLabel:
                theme_text_color:"Custom"
                text_color:"white"
                text:"Total balance"
                halign:"center"
                font_style:"Body2"
                height:self.texture_size[1]
            # MDSeparator:
            #     height:"1dp"

            MDLabel:
                text:"15,269"
                theme_text_color:"Custom"
                text_color:"white"
                halign:"center"
                font_style:"H5"
        MDCard:
            orientation:"vertical"
            size_hint:None,None
            size:"150dp","110dp"
            pos_hint:{"center_x":.75,"center_y":.8}
            md_bg_color:"#282878"
            radius:"25dp"
            # MDIconButton:
            #     icon:"dots-vertical"
            #     pos_hint:{"top":1,"right":1}
            MDLabel:
                theme_text_color:"Custom"
                text_color:"white"
                halign:"center"
                text:"Monthly spending"
                font_style:"Body2"
                height:self.texture_size[1]
            # MDSeparator:
            #     height:"1dp"

            MDLabel:
                text:"7,175"
                theme_text_color:"Custom"
                text_color:"white"
                halign:"center"
                font_style:"H5"
        MDFlatButton:
            text:"My Cards"
            theme_text_color:"Custom"
            text_color:"white"
            font_name:"Manjari-Bold.otf"
            pos_hint:{"center_x":.19,"center_y":.65}
            font_style:"H6"
        MDFlatButton:
            text:"Deposits"
            theme_text_color:"Custom"
            text_color:"grey"
            font_name:"Manjari-Bold.otf"
            pos_hint:{"center_x":.5,"center_y":.65}
            font_style:"Body2"
        MDFlatButton:
            text:"Transactions"
            theme_text_color:"Custom"
            text_color:"grey"
            font_name:"Manjari-Bold.otf"
            pos_hint:{"center_x":.8,"center_y":.65}
            font_style:"Body2"
        MDCard:
            size_hint:None,None
            radius:25
            md_bg_color:"orange"
            pos_hint:{"center_x":.5,"center_y":.53}
            size:"300dp","100dp"
            MDLabel:
                text:"Salary Card"
                theme_text_color:"Custom"
                text_color:"white"
                pos_hint:{"center_y":.7}
                font_name:"Manjari-Bold.otf"
                padding:"99"
                
        MDCard:

            size_hint:None,None
            size:"300dp","100dp"
            radius:25
            md_bg_color:"purple"
            pos_hint:{"center_x":.5,"center_y":.45}
            MDLabel:
                text:"Private Card"
                theme_text_color:"Custom"
                text_color:"white"
                pos_hint:{"center_y":.7}
                font_name:"Manjari-Bold.otf"
                padding:"99"
        MDCard:

            size_hint:None,None
            size:"300dp","150dp"
            radius:25
            md_bg_color:"pink"
            pos_hint:{"center_x":.5,"center_y":.33}
            MDLabel:
                text:"Family Card"
                theme_text_color:"Custom"
                text_color:"white"
                pos_hint:{"center_y":.77}
                font_name:"Manjari-Bold.otf"
                padding:"99"
            
            MDLabel:
                text:"VISA"
                theme_text_color:"Custom"
                text_color:"white"
                size_hint:None,None
                pos_hint:{"center_x":.8,"center_y":.2}
                font_style:"H4"
                bold:True
        MDCard:
            radius:10
            size_hint:None,None
            size:"300dp","60dp"
            md_bg_color:"#282878"
            pos_hint:{"center_x":.5,"center_y":.12}
            MDFlatButton:
                text:"Add card                                                   +"
                font_name:"Manjari-Bold.otf"
                font_style:"Body1"
                theme_text_color:"Custom"
                text_color:"white"
                pos_hint:{"center_x":.5,"center_y":.5}

                
                
                
                
                   
'''
class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)
if __name__=='__main__':
    MainApp().run()