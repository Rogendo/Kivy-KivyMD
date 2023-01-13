from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDScreen:
    orientation:"vertical"
    MDSmartTile:
        radius: 150
        box_radius: [0, 0, 24, 24]
        box_color: 1, 1, 1, .2
        source: "assets/jane.jpg"
        pos_hint: {"center_x": .5, "center_y": .7}
        size_hint: None, None
        size: "360dp", "360dp"

    MDIconButton:
        icon: "heart-outline"
        theme_icon_color: "Custom"
        icon_color: 1, 0, 0, 1
        pos_hint: {"center_y": .5}
        on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"

    MDLabel:
        text: "Julia and Julie"
        bold: True
        color: 1, 1, 1, 1
'''


class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


MyApp().run()