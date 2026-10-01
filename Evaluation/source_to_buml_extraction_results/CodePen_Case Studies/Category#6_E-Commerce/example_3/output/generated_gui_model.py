from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *
from enum import Enum


class LayoutType(Enum):
    Flex = "flex"


class JustificationType(Enum):
    Center = "center"


class PositionType(Enum):
    Relative = "relative"


class UnitSize(Enum):
    PIXELS = "px"


class Layout:

    def __init__(self, type, orientation, gap, alignment):
        self.type = type
        self.orientation = orientation
        self.gap = gap
        self.alignment = alignment


class Size:

    def __init__(self, width, height, padding, margin, font_size, unit_size):
        self.width = width
        self.height = height
        self.padding = padding
        self.margin = margin
        self.font_size = font_size
        self.unit_size = unit_size


class Color:

    def __init__(self, background_color, text_color, border_color):
        self.background_color = background_color
        self.text_color = text_color
        self.border_color = border_color


class Styling:

    def __init__(self, size, position, color):
        self.size = size
        self.position = position
        self.color = color


class Position:

    def __init__(self, type):
        self.type = type


class ViewComponent:

    def __init__(self, name, description, styling, properties):
        self.name = name
        self.description = description
        self.styling = styling
        self.properties = properties


class ViewContainer:

    def __init__(self, name, description, layout, view_elements, properties):
        self.name = name
        self.description = description
        self.layout = layout
        self.view_elements = view_elements
        self.properties = properties


class Screen:

    def __init__(self, name, description, x_dpi, y_dpi, screen_size, view_elements, is_main_page, layout):
        self.name = name
        self.description = description
        self.x_dpi = x_dpi
        self.y_dpi = y_dpi
        self.screen_size = screen_size
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


ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ColumnColor = Color(background_color="#FFFFFF", text_color="#000000", border_color="#222")
ColumnPosition = Position(type=PositionType.Relative)
ColumnSize = Size(width="235px", height="auto", padding="10px 0", margin="0 0 20px", font_size="16px", unit_size=UnitSize.PIXELS)
ColumnStyling = Styling(size=ColumnSize, position=ColumnPosition, color=ColumnColor)
columns = [ViewComponent(name=f"Column{i + 1}", description="Wow! I'm A Column", styling=ColumnStyling) for i in range(6)]
section = ViewContainer(name="MainSection", description="Main section with columns", layout=ScreenLayout, view_elements=set(columns))
ResponsiveScreen = Screen(name="ResponsiveScreen", description="Responsive web design screen with multiple columns", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={section}, is_main_page=True, layout=ScreenLayout)
ResponsiveModule = Module(name="ResponsiveModule", screens={ResponsiveScreen})
gui_model = GUIModel(name="ResponsiveWebApp", package="com.example.responsivewebapp", versionCode="1", versionName="1.0", description="A responsive web application with multiple columns.", screenCompatibility=True, modules={ResponsiveModule})
