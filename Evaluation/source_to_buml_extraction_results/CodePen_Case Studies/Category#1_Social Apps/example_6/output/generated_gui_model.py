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
    Login = "login"


class UnitSize(Enum):
    PIXELS = "px"


class JustificationType(Enum):
    Center = "center"


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


class Button(ViewComponent):

    def __init__(self, name, description, label, buttonType, actionType, styling):
        super().__init__(name, description)
        self.label = label
        self.buttonType = buttonType
        self.actionType = actionType
        self.styling = styling


class InputField(ViewComponent):

    def __init__(self, name, description, type, validationRules, styling):
        super().__init__(name, description)
        self.type = type
        self.validationRules = validationRules
        self.styling = styling


class Form(ViewComponent):

    def __init__(self, name, description, inputFields, styling=None):
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


ScreenLayout = Layout(type=LayoutType.Flex, orientation="horizontal", gap="20px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#3b5998", text_color="#FFFFFF", border_color="#2d4373")
ButtonPosition = Position(type=PositionType.Relative)
ButtonSize = Size(width="100%", height="50", padding="0.7em", margin="0.6em 0", font_size="0.9em", unit_size=UnitSize.PIXELS)
ButtonStyling = Styling(size=ButtonSize, position=ButtonPosition, color=ButtonColor)
InputFieldColor = Color(background_color="#FFFFFF", text_color="#000000", border_color="#dddddd")
InputFieldPosition = Position(type=PositionType.Relative)
InputFieldSize = Size(width="100%", height="40", padding="0.7em", margin="0.6em 0", font_size="0.9em", unit_size=UnitSize.PIXELS)
InputFieldStyling = Styling(size=InputFieldSize, position=InputFieldPosition, color=InputFieldColor)
facebookButton = Button(name="FacebookLoginButton", description="Sign in with Facebook", label="Sign in with Facebook", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Login, styling=ButtonStyling)
twitterButton = Button(name="TwitterLoginButton", description="Sign in with Twitter", label="Sign in with Twitter", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Login, styling=ButtonStyling)
googleButton = Button(name="GoogleLoginButton", description="Sign in with Google", label="Sign in with Google", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Login, styling=ButtonStyling)
userNameField = InputField(name="UserNameField", description="User Name", type="Text", validationRules="", styling=InputFieldStyling)
passwordField = InputField(name="PasswordField", description="Password", type="Password", validationRules="", styling=InputFieldStyling)
rememberMeField = InputField(name="RememberMeField", description="Remember Me", type="Checkbox", validationRules="", styling=InputFieldStyling)
loginForm = Form(name="LoginForm", description="User login form", inputFields={userNameField, passwordField, rememberMeField})
LoginScreen = Screen(name="LoginScreen", description="Screen for user login", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={facebookButton, twitterButton, googleButton, loginForm}, is_main_page=True, layout=ScreenLayout)
MyModule = Module(name="UserAuthenticationModule", screens={LoginScreen})
gui_model = GUIModel(name="UserAuthenticationApp", package="com.example.userauthentication", versionCode="1", versionName="1.0", description="An application for user authentication with social media options.", screenCompatibility=True, modules={MyModule})
