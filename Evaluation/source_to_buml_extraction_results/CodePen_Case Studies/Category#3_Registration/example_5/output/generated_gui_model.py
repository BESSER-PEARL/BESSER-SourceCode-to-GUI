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


class ButtonType(Enum):
    RaisedButton = "raised"


class ButtonActionType(Enum):
    Submit = "submit"


class JustificationType(Enum):
    Center = "center"


class Layout:

    def __init__(self, type, orientation, gap, alignment):
        self.type = type
        self.orientation = orientation
        self.gap = gap
        self.alignment = alignment


class Color:

    def __init__(self, background_color, text_color, border_color):
        self.background_color = background_color
        self.text_color = text_color
        self.border_color = border_color


class Position:

    def __init__(self, type, z_index=0):
        self.type = type
        self.z_index = z_index


class Size:

    def __init__(self, width, height, padding, margin, font_size, unit_size):
        self.width = width
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


class ViewComponent:

    def __init__(self, name, description):
        self.name = name
        self.description = description


class InputField(ViewComponent):

    def __init__(self, name, description, type, validationRules, styling, property):
        super().__init__(name, description)
        self.type = type
        self.validationRules = validationRules
        self.styling = styling
        self.property = property


class Button(ViewComponent):

    def __init__(self, name, description, label, buttonType, actionType, styling):
        super().__init__(name, description)
        self.label = label
        self.buttonType = buttonType
        self.actionType = actionType
        self.styling = styling


class Form(ViewComponent):

    def __init__(self, name, description, inputFields, styling):
        super().__init__(name, description)
        self.inputFields = inputFields
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
inputFieldColor = Color(background_color="#FFFFFF", text_color="#8D8D8D", border_color="#CED4DA")
inputFieldPosition = Position(type=PositionType.Relative)
inputFieldSize = Size(width="100%", height="40px", padding="9px 20px", margin="16px 0", font_size="15px", unit_size=UnitSize.PIXELS)
inputFieldStyling = Styling(size=inputFieldSize, position=inputFieldPosition, color=inputFieldColor)
buttonColor = Color(background_color="#6C757D", text_color="#FFFFFF", border_color="#495056")
buttonPosition = Position(type=PositionType.Relative, z_index=10)
buttonSize = Size(width="100%", height="40px", padding="8px", margin="24px 0", font_size="14px", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=buttonColor)
nameInput = InputField(name="nameInput", description="Full Name", type="Text", validationRules="required", styling=inputFieldStyling)
emailInput = InputField(name="emailInput", description="E-mail Address", type="Email", validationRules="required", styling=inputFieldStyling)
positionSelect = InputField(name="positionSelect", description="Position", type="Text", validationRules="required", styling=inputFieldStyling)
passwordInput = InputField(name="passwordInput", description="Password", type="Password", validationRules="required", styling=inputFieldStyling)
genderInput = InputField(name="genderInput", description="Gender", type="Text", validationRules="required", styling=inputFieldStyling)
confirmDataInput = InputField(name="confirmDataInput", description="Confirm Data", type="Boolean", validationRules="required", styling=inputFieldStyling)
registrationForm = Form(name="RegistrationForm", description="User registration form", inputFields={nameInput, emailInput, positionSelect, passwordInput, genderInput, confirmDataInput}, styling=None)
registerButton = Button(name="registerButton", description="Register", label="Register", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Submit, styling=buttonStyling)
RegistrationScreen = Screen(name="RegistrationScreen", description="User registration screen", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={registrationForm, registerButton}, is_main_page=True, layout=ScreenLayout)
RegistrationModule = Module(name="RegistrationModule", screens={RegistrationScreen})
gui_model = GUIModel(name="RegistrationApp", package="com.example.registrationapp", versionCode="1", versionName="1.0", description="A user registration application.", screenCompatibility=True, modules={RegistrationModule})
