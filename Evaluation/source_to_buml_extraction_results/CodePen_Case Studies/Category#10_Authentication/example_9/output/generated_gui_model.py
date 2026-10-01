from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *
from enum import Enum


class LayoutType(Enum):
    Flex = "flex"
    Grid = "grid"


class JustificationType(Enum):
    Center = "center"
    Left = "left"


class PositionType(Enum):
    Relative = "relative"
    Absolute = "absolute"


class UnitSize(Enum):
    PIXELS = "px"
    PERCENT = "%"


class ButtonType(Enum):
    RaisedButton = "raised"
    TextButton = "text"


class ButtonActionType(Enum):
    Login = "login"
    Add = "add"


class InputFieldType(Enum):
    Email = "email"
    Password = "password"
    Text = "text"
    Boolean = "boolean"


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


ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#0C4B33", text_color="#FFFFFF", border_color="#0A3A28")
buttonPosition = Position(type=PositionType.Relative, z_index=10)
buttonSize = Size(width="100%", height="40px", padding="8px", margin="24px", font_size="14px", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
inputFieldSize = Size(width="100%", height="40px", padding="8px", margin="8px", font_size="14px", unit_size=UnitSize.PIXELS)
inputFieldColor = Color(background_color="#FFFFFF", text_color="#000000", border_color="#CCCCCC")
inputFieldStyling = Styling(size=inputFieldSize, color=inputFieldColor)


class ViewComponent:

    def __init__(self, name, description):
        self.name = name
        self.description = description


viewComponent = ViewComponent(name="LoginRegisterView", description="Login and Register forms with social login options")


class Button:

    def __init__(self, name, description, label, buttonType, actionType, styling):
        self.name = name
        self.description = description
        self.label = label
        self.buttonType = buttonType
        self.actionType = actionType
        self.styling = styling


loginButton = Button(name="LoginButton", description="Submit login form", label="Login", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Login, styling=buttonStyling)
registerButton = Button(name="RegisterButton", description="Submit register form", label="Register", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add, styling=buttonStyling)


class InputField:

    def __init__(self, name, description, type, styling, property):
        self.name = name
        self.description = description
        self.type = type
        self.styling = styling
        self.property = property


emailInput = InputField(name="EmailInput", description="Email input field", type=InputFieldType.Email, styling=inputFieldStyling)
passwordInput = InputField(name="PasswordInput", description="Password input field", type=InputFieldType.Password, styling=inputFieldStyling)
rememberMeInput = InputField(name="RememberMeInput", description="Remember me checkbox", type=InputFieldType.Boolean, styling=inputFieldStyling)
fullNameInput = InputField(name="FullNameInput", description="Full name input field", type=InputFieldType.Text, styling=inputFieldStyling)
regEmailInput = InputField(name="RegEmailInput", description="Email input field", type=InputFieldType.Email, styling=inputFieldStyling)
regPasswordInput = InputField(name="RegPasswordInput", description="Password input field", type=InputFieldType.Password, styling=inputFieldStyling)
termsAgreeInput = InputField(name="TermsAgreeInput", description="Terms agreement checkbox", type=InputFieldType.Boolean, styling=inputFieldStyling)


class Form:

    def __init__(self, name, description, inputFields, styling):
        self.name = name
        self.description = description
        self.inputFields = inputFields
        self.styling = styling


loginForm = Form(name="LoginForm", description="Form for user login", inputFields={emailInput, passwordInput, rememberMeInput}, styling=None)
registerForm = Form(name="RegisterForm", description="Form for user registration", inputFields={fullNameInput, regEmailInput, regPasswordInput, termsAgreeInput}, styling=None)


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


LoginRegisterScreen = Screen(name="LoginRegisterScreen", description="Screen for login and registration", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={loginButton, registerButton, loginForm, registerForm}, is_main_page=True, layout=ScreenLayout)


class Module:

    def __init__(self, name, screens):
        self.name = name
        self.screens = screens


MyModule = Module(name="UserAuthModule", screens={LoginRegisterScreen})


class GUIModel:

    def __init__(self, name, package, versionCode, versionName, description, screenCompatibility, modules):
        self.name = name
        self.package = package
        self.versionCode = versionCode
        self.versionName = versionName
        self.description = description
        self.screenCompatibility = screenCompatibility
        self.modules = modules


gui_model = GUIModel(name="UserAuthApp", package="com.example.userauth", versionCode="1", versionName="1.0", description="User authentication application with login and registration", screenCompatibility=True, modules={MyModule})
