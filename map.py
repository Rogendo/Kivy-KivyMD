# from kivymd.app import MDApp
# from kivy.lang import Builder
#
#
# class Mapview(MDApp):
#     def build(self):
#         self.theme_cls.theme_style="Dark"
#         self.theme_cls.primary_palette="Pink"
#         return Builder.load_file('map.kv')
#
#
# if __name__=="__main__":
#     Mapview().run()
from kivymd.app import MDApp
from kivy_garden.mapview import MapView

class Mapview(MDApp):
    def build(self):
        mapview=Mapview(zoom=10,lat=36,lon=-115)
        return mapview

if __name__=="__main__":
    Mapview().run()