from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *
from enum import Enum


class LayoutType(Enum):
    Flex = "flex"


class PositionType(Enum):
    Relative = "relative"


class UnitSize(Enum):
    PIXELS = "px"


class JustificationType(Enum):
    Center = "center"


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


ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
TableColor = Color(background_color="#FFFFFF", text_color="#000000", border_color="#CCCCCC")
TablePosition = Position(type=PositionType.Relative)
TableSize = Size(width="50%", height="auto", padding="12px", margin="auto", font_size="14", unit_size=UnitSize.PIXELS)
TableStyling = Styling(size=TableSize, position=TablePosition, color=TableColor)
ImageSize = Size(width="78px", height="27px", padding="0", margin="0", font_size="0", unit_size=UnitSize.PIXELS)
ImageStyling = Styling(size=ImageSize, position=TablePosition, color=TableColor)


class ViewComponent:

    def __init__(self, name, description):
        self.name = name
        self.description = description


viewComponent = ViewComponent(name="TaksitOptionsView", description="Display installment options for different credit cards")


class DataList(ViewComponent):

    def __init__(self, name, description, list_sources, styling):
        super().__init__(name, description)
        self.list_sources = list_sources
        self.styling = styling


tableHeader = DataList(name="TableHeader", description="Table header for installment options", list_sources=set(), styling=TableStyling)
akbankRow = DataList(name="AkbankRow", description="Installment options for Akbank", list_sources={"Taksit_ikiTaksitAkbank", "Taksit_ucTaksitAkbank", "Taksit_dortTaksitAkbank", "Taksit_besTaksitAkbank", "Taksit_altiTaksitAkbank"}, styling=TableStyling)


class Image(ViewComponent):

    def __init__(self, name, styling):
        super().__init__(name, "")
        self.styling = styling


akbankImage = Image(name="AkbankImage", styling=ImageStyling, description="")


class Screen(ViewComponent):

    def __init__(self, name, description, x_dpi, y_dpi, screen_size, view_elements, is_main_page, layout):
        super().__init__(name, description)
        self.x_dpi = x_dpi
        self.y_dpi = y_dpi
        self.screen_size = screen_size
        self.view_elements = view_elements
        self.is_main_page = is_main_page
        self.layout = layout


TaksitScreen = Screen(name="TaksitScreen", description="Screen displaying installment options for various credit cards", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={tableHeader, akbankRow, akbankImage}, is_main_page=True, layout=ScreenLayout)


class Module(ViewComponent):

    def __init__(self, name, screens):
        super().__init__(name, "")
        self.screens = screens


TaksitModule = Module(name="TaksitModule", screens={TaksitScreen})


class GUIModel(ViewComponent):

    def __init__(self, name, package, versionCode, versionName, description, screenCompatibility, modules):
        super().__init__(name, description)
        self.package = package
        self.versionCode = versionCode
        self.versionName = versionName
        self.screenCompatibility = screenCompatibility
        self.modules = modules


gui_model = GUIModel(name="TaksitApp", package="com.example.taksitapp", versionCode="1", versionName="1.0", description="Application for displaying installment options for credit cards.", screenCompatibility=True, modules={TaksitModule})
