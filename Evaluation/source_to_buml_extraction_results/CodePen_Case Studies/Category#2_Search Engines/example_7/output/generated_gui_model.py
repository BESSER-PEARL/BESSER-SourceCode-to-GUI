from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *
from enum import Enum


class LayoutType(Enum):
    FLEX = "flex"
    GRID = "grid"


class PositionType(Enum):
    RELATIVE = "relative"
    ABSOLUTE = "absolute"


class ButtonType(Enum):
    RAISED = "raised"


class ButtonActionType(Enum):
    SEARCH = "search"


class JustificationType(Enum):
    CENTER = "center"


class UnitSize(Enum):
    PIXELS = "px"


class Layout:

    def __init__(self, type, orientation, gap, alignment):
        self.type = type
        self.orientation = orientation
        self.gap = gap
        self.alignment = alignment


class Size:

    def __init__(self, width=None, height=None, padding=None, margin=None, font_size=None, unit_size=UnitSize.PIXELS):
        self.width = width
        self.height = height
        self.padding = padding
        self.margin = margin
        self.font_size = font_size
        self.unit_size = unit_size


class Position:

    def __init__(self, type, z_index=0):
        self.type = type
        self.z_index = z_index


class Color:

    def __init__(self, background_color, text_color, border_color):
        self.background_color = background_color
        self.text_color = text_color
        self.border_color = border_color


class Styling:

    def __init__(self, size=None, position=None, color=None):
        self.size = size
        self.position = position
        self.color = color


class ViewElement:

    def __init__(self, name, description, styling=None):
        self.name = name
        self.description = description
        self.styling = styling


class Button(ViewElement):

    def __init__(self, name, description, label, buttonType, actionType, styling=None):
        super().__init__(name, description, styling)
        self.label = label
        self.buttonType = buttonType
        self.actionType = actionType


class InputField(ViewElement):

    def __init__(self, name, description, type, validationRules, styling=None):
        super().__init__(name, description, styling)
        self.type = type
        self.validationRules = validationRules


class MenuItem:

    def __init__(self, label):
        self.label = label


class Menu(ViewElement):

    def __init__(self, name, description, menuItems, styling=None):
        super().__init__(name, description, styling)
        self.menuItems = menuItems


class Screen:

    def __init__(self, name, description, view_elements, is_main_page, layout):
        self.name = name
        self.description = description
        self.view_elements = view_elements
        self.is_main_page = is_main_page
        self.layout = layout


class Module:

    def __init__(self, name, screens):
        self.name = name
        self.screens = screens


class GUIModel:

    def __init__(self, name, package, versionCode, versionName, description, screenCompatibility, modules):
        self.name = name
        self.package = package
        self.versionCode = versionCode
        self.versionName = versionName
        self.description = description
        self.screenCompatibility = screenCompatibility
        self.modules = modules


screen_layout = Layout(type=LayoutType.FLEX, orientation="vertical", gap="15px", alignment=JustificationType.CENTER)
button_color = Color(background_color="#007BFF", text_color="#FFFFFF", border_color="#0056b3")
button_position = Position(type=PositionType.RELATIVE, z_index=10)
button_size = Size(height="40px", padding="8px", margin="24px", font_size="14px")
button_styling = Styling(size=button_size, position=button_position, color=button_color)
search_input_field = InputField(name="SearchInputField", description="Search input field", type="Search", validationRules="maxlength:512,autocomplete:off,spellcheck:false", styling=Styling(size=Size(width="100%", height="40px")))
search_button = Button(name="SearchButton", description="Search the web", label="Search", buttonType=ButtonType.RAISED, actionType=ButtonActionType.SEARCH, styling=button_styling)
nav_menu = Menu(name="NavigationMenu", description="Main navigation menu", menuItems={MenuItem(label="Web"), MenuItem(label="Images"), MenuItem(label="Videos"), MenuItem(label="News")})
footer_links = Menu(name="FooterLinks", description="Footer navigation links", menuItems={MenuItem(label="Business"), MenuItem(label="About"), MenuItem(label="Privacy"), MenuItem(label="Terms"), MenuItem(label="Settings")})
index_page_screen = Screen(name="IndexPageScreen", description="Main search and navigation page", view_elements={search_input_field, search_button, nav_menu, footer_links}, is_main_page=True, layout=screen_layout, y_dpi="", x_dpi="", screen_size="")
my_module = Module(name="IndexModule", screens={index_page_screen})
gui_model = GUIModel(name="IndexApp", package="com.example.indexapp", versionCode="1.0.0", versionName="1.0", description="Main search and navigation application", screenCompatibility=True, modules={my_module})
