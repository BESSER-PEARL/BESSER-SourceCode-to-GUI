from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *
from enum import Enum


class LayoutType(Enum):
    Flex = "flex"


class PositionType(Enum):
    Relative = "relative"


class ButtonType(Enum):
    RaisedButton = "raised"


class ButtonActionType(Enum):
    Add = "add"


class JustificationType(Enum):
    Center = "center"


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


class Position:

    def __init__(self, type, z_index):
        self.type = type
        self.z_index = z_index


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


class ViewComponent:

    def __init__(self, name, description):
        self.name = name
        self.description = description


class Image(ViewComponent):
    pass


class Tab(ViewComponent):

    def __init__(self, name, description, tabId, tabName):
        super().__init__(name, description)
        self.tabId = tabId
        self.tabName = tabName


class Content(ViewComponent):
    pass


class Button(ViewComponent):

    def __init__(self, name, description, label, buttonType, actionType, styling):
        super().__init__(name, description)
        self.label = label
        self.buttonType = buttonType
        self.actionType = actionType
        self.styling = styling


ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#0C4B33", text_color="#FFFFFF", border_color="#0A3A28")
buttonPosition = Position(type=PositionType.Relative, z_index=10)
buttonSize = Size(width="auto", height="40px", padding="10px", margin="15px", font_size="1em", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
viewComponent = ViewComponent(name="ProductInfoView", description="Display product information with tabs and actions")
image1 = Image(name="Image1", description="Product image 1")
image2 = Image(name="Image2", description="Product image 2")
descriptionTab = Tab(name="DescriptionTab", description="Product description", tabId="descTab", tabName="Description")
detailsTab = Tab(name="DetailsTab", description="Product details", tabId="detailsTab", tabName="Details")
descriptionContent = Content(name="DescriptionContent", description="Detailed product description")
detailsContent = Content(name="DetailsContent", description="Detailed product specifications")
addToChartButton = Button(name="AddToChartButton", description="Add product to chart", label="Add to Chart", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add, styling=buttonStyling)


class Screen(ViewComponent):

    def __init__(self, name, description, x_dpi, y_dpi, screen_size, is_main_page, view_elements, layout):
        super().__init__(name, description)
        self.x_dpi = x_dpi
        self.y_dpi = y_dpi
        self.screen_size = screen_size
        self.is_main_page = is_main_page
        self.view_elements = view_elements
        self.layout = layout


ProductInfoScreen = Screen(name="ProductInfoScreen", description="Screen displaying product information with images and tabs", x_dpi="160", y_dpi="160", screen_size="Medium", is_main_page=True, view_elements={image1, image2, descriptionTab, detailsTab, descriptionContent, detailsContent, addToChartButton}, layout=ScreenLayout)


class Module(ViewComponent):

    def __init__(self, name, screens):
        super().__init__(name, "")
        self.screens = screens


ProductModule = Module(name="ProductModule", screens={ProductInfoScreen})


class GUIModel(ViewComponent):

    def __init__(self, name, package, versionCode, versionName, description, screenCompatibility, modules):
        super().__init__(name, description)
        self.package = package
        self.versionCode = versionCode
        self.versionName = versionName
        self.screenCompatibility = screenCompatibility
        self.modules = modules


gui_model = GUIModel(name="ProductApp", package="com.example.productapp", versionCode="1", versionName="1.0", description="An application to display product information with images and tabs.", screenCompatibility=True, modules={ProductModule})
