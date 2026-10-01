from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

side_nav_instance = SideNav()
menu_item_instance = MenuItem(label="")
sub_menu_item_instance = SubMenuItem()
side_nav_instance.set(SideNav_logo, "Company Logo")
side_nav_instance.set(SideNav_toggle, "Toggle Button")
menu_item_instance.set(MenuItem_icon, "home-icon")
menu_item_instance.set(MenuItem_label, "Home")
sub_menu_item_instance.set(SubMenuItem_label, "Sub Home")
logo = side_nav_instance.get(SideNav_logo)
toggle = side_nav_instance.get(SideNav_toggle)
icon = menu_item_instance.get(MenuItem_icon)
label = menu_item_instance.get(MenuItem_label)
sub_label = sub_menu_item_instance.get(SubMenuItem_label)
print(f"SideNav Logo: {logo}")
print(f"SideNav Toggle: {toggle}")
print(f"MenuItem Icon: {icon}")
print(f"MenuItem Label: {label}")
print(f"SubMenuItem Label: {sub_label}")
side_nav_styling = Styling(size=Size(width="216px", height="500px", unit_size=UnitSize.PIXELS), color=Color(background_color="rgba(255,255,255,0.1)", text_color="#fff", border_color=""), position=Position(type=PositionType.RELATIVE))
menu_item_styling = Styling(size=Size(font_size="0.76em", unit_size=UnitSize.EM), color=Color(text_color="#fff", border_color="", background_color=""), position=Position(type=PositionType.RELATIVE))
sub_menu_item_styling = Styling(size=Size(font_size="0.76em", unit_size=UnitSize.EM), color=Color(text_color="#fff", border_color="", background_color=""), position=Position(type=PositionType.RELATIVE))
side_nav_instance.styling = side_nav_styling
menu_item_instance.styling = menu_item_styling
sub_menu_item_instance.styling = sub_menu_item_styling
side_nav_styling.size.padding = "10px"
side_nav_styling.size.margin = "0"
side_nav_styling.position.z_index = 1
menu_item_styling.color.hover_text_color = "#3ed8b5"
sub_menu_item_styling.color.hover_text_color = "#3ed8b5"
side_nav_styling.animation = "animate-width 1.2s ease-in-out"
sub_menu_item_styling.animation = "animate-height 1.2s ease-in-out"
