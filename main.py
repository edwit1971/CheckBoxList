#############################################################
# File Name : main.py
#
# KivyMD - List with CheckBoxes
#
# Created :   July 2020 
#############################################################


from kivy.properties import StringProperty

from kivy.uix.boxlayout  import BoxLayout
from kivy.uix.scrollview import ScrollView

from kivymd.app              import MDApp
from kivymd.icon_definitions import md_icons

from kivymd.uix.list             import MDList
from kivymd.uix.list             import IRightBodyTouch
from kivymd.uix.list             import IconLeftWidget
from kivymd.uix.list             import OneLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox


class ListItemWithCheckbox(OneLineAvatarIconListItem):
    '''Custom list item.'''
    icon = StringProperty("android")
    
    def __init__(self, pText, pIcon, **kwargs):
        super(ListItemWithCheckbox, self).__init__(**kwargs)
        ###
        self.RCheck = RightCheckbox()
        ###
        ListItemWithCheckbox.icon = IconLeftWidget(icon = pIcon)
        self.text = pText
        ###
        if(self.RCheck.parent == None):
            self.add_widget(self.RCheck)
        if(ListItemWithCheckbox.icon.parent == None):
            self.add_widget(ListItemWithCheckbox.icon)
        return


class RightCheckbox(IRightBodyTouch, MDCheckbox):
    '''Custom right container.'''
    pass

class MainApp(MDApp):
    
    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)
        self.Screen  = BoxLayout()
        self.Scroll  = MDList()
        self.ScrView = ScrollView()
        return
    
    def build(self):
        if(self.Scroll.parent == None):
            self.ScrView.add_widget(self.Scroll)
        if(self.ScrView.parent == None):
            self.Screen.add_widget(self.ScrView)
        return self.Screen

    def on_start(self):
        icons = list(md_icons.keys())
        for i in range(30):
            self.Scroll.add_widget(ListItemWithCheckbox(pText=f"Item {i}", pIcon=icons[i]))


MainApp().run()

