from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *
from enum import Enum


class LayoutType(Enum):
    Flex = "flex"
    Grid = "grid"


class PositionType(Enum):
    Relative = "relative"
    Absolute = "absolute"


class UnitSize(Enum):
    PIXELS = "px"
    PERCENT = "%"


class JustificationType(Enum):
    Center = "center"


class Color:

    def __init__(self, background_color, text_color, border_color):
        self.background_color = background_color
        self.text_color = text_color
        self.border_color = border_color


class Position:

    def __init__(self, type, right=None, top=None):
        self.type = type
        self.right = right
        self.top = top


class Size:

    def __init__(self, width, height, padding, font_size, unit_size):
        self.width = width
        self.height = height
        self.padding = padding
        self.font_size = font_size
        self.unit_size = unit_size


class Styling:

    def __init__(self, size, position, color):
        self.size = size
        self.position = position
        self.color = color


class Layout:

    def __init__(self, type, orientation, gap, alignment):
        self.type = type
        self.orientation = orientation
        self.gap = gap
        self.alignment = alignment


ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
MenuColor = Color(background_color="#2C3E50", text_color="#FFFFFF", border_color="#CCCCCC")
MenuPosition = Position(type=PositionType.Relative)
MenuSize = Size(width="20%", height="100vh", padding="10px", font_size="12.5", unit_size=UnitSize.PIXELS)
MenuStyling = Styling(size=MenuSize, position=MenuPosition, color=MenuColor)
AccountColor = Color(background_color="#2C3E50", text_color="#FFFFFF", border_color="#CCCCCC")
AccountPosition = Position(type=PositionType.Absolute, right="0", top="20px")
AccountSize = Size(width="35px", height="35px", padding="10px", font_size="15", unit_size=UnitSize.PIXELS)
AccountStyling = Styling(size=AccountSize, position=AccountPosition, color=AccountColor)
DashboardColor = Color(background_color="#2C3E50", text_color="#FFFFFF", border_color="#CCCCCC")
DashboardPosition = Position(type=PositionType.Relative)
DashboardSize = Size(width="80%", height="100vh", padding="10px", font_size="14", unit_size=UnitSize.PIXELS)
DashboardStyling = Styling(size=DashboardSize, position=DashboardPosition, color=DashboardColor)


class ViewComponent:

    def __init__(self, name, description, styling):
        self.name = name
        self.description = description
        self.styling = styling


menu = ViewComponent(name="MainMenu", description="Main navigation menu", styling=MenuStyling)
account = ViewComponent(name="Account", description="User account section", styling=AccountStyling)
dashboard = ViewComponent(name="Dashboard", description="Main dashboard area", styling=DashboardStyling)


class Screen:

    def __init__(self, name, description, view_elements, layout):
        self.name = name
        self.description = description
        self.view_elements = view_elements
        self.layout = layout


MainScreen = Screen(name="MainScreen", description="Main application screen with dashboard and menu", view_elements={menu, account, dashboard}, layout=ScreenLayout, y_dpi="", screen_size="", x_dpi="")


class Module:

    def __init__(self, name, screens):
        self.name = name
        self.screens = screens


MainModule = Module(name="MainModule", screens={MainScreen})


class GUIModel:

    def __init__(self, name, package, versionCode, versionName, description, modules):
        self.name = name
        self.package = package
        self.versionCode = versionCode
        self.versionName = versionName
        self.description = description
        self.modules = modules


gui_model = GUIModel(name="DashboardApp", package="com.example.dashboardapp", versionCode="1", versionName="1.0", description="A web application for managing analytics and reports.", modules={MainModule})
