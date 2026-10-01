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


class ButtonType(Enum):
    RaisedButton = "raised"
    TextButton = "text"


class ButtonActionType(Enum):
    Share = "share"


class JustificationType(Enum):
    Center = "center"


class UnitSize(Enum):
    PIXELS = "px"


class Color:

    def __init__(self, background_color, text_color, border_color):
        self.background_color = background_color
        self.text_color = text_color
        self.border_color = border_color


class Position:

    def __init__(self, type, z_index):
        self.type = type
        self.z_index = z_index


class Size:

    def __init__(self, height, padding, margin, font_size, unit_size):
        self.height = height
        self.padding = padding
        self.margin = margin
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


class ViewComponent:

    def __init__(self, name, description):
        self.name = name
        self.description = description


class InputField(ViewComponent):

    def __init__(self, name, description, type, validationRules, styling):
        super().__init__(name, description)
        self.type = type
        self.validationRules = validationRules
        self.styling = styling


class Button(ViewComponent):

    def __init__(self, name, description, label, buttonType, actionType, styling):
        super().__init__(name, description)
        self.label = label
        self.buttonType = buttonType
        self.actionType = actionType
        self.styling = styling


class Screen(ViewComponent):

    def __init__(self, name, description, x_dpi, y_dpi, screen_size, view_elements, is_main_page, layout):
        super().__init__(name, description)
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
ButtonColor = Color(background_color="#007BFF", text_color="#FFFFFF", border_color="#0056b3")
buttonPosition = Position(type=PositionType.Relative, z_index=10)
buttonSize = Size(height="40px", padding="8px", margin="24px", font_size="14px", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
urlInputField = InputField(name="URLInput", description="Input for URL", type="URL", validationRules="", styling=None)
textInputField = InputField(name="TextInput", description="Input for Text", type="Text", validationRules="", styling=None)
viaInputField = InputField(name="ViaInput", description="Input for Via", type="Text", validationRules="", styling=None)
linkedinButton = Button(name="LinkedInButton", description="Share on LinkedIn", label="Share on LinkedIn", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Share, styling=buttonStyling)
facebookButton = Button(name="FacebookButton", description="Share on Facebook", label="Share on Facebook", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Share, styling=buttonStyling)
twitterButton = Button(name="TwitterButton", description="Tweet", label="Tweet", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Share, styling=buttonStyling)
googlePlusButton = Button(name="GooglePlusButton", description="Share on Google+", label="Share on Google+", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Share, styling=buttonStyling)
ShareLinksScreen = Screen(name="ShareLinksScreen", description="Screen for sharing links", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={urlInputField, textInputField, viaInputField, linkedinButton, facebookButton, twitterButton, googlePlusButton}, is_main_page=True, layout=ScreenLayout)
ShareLinksModule = Module(name="ShareLinksModule", screens={ShareLinksScreen})
gui_model = GUIModel(name="ShareLinksApp", package="com.example.sharelinks", versionCode="1", versionName="1.0", description="An application for sharing links on social media.", screenCompatibility=True, modules={ShareLinksModule})
