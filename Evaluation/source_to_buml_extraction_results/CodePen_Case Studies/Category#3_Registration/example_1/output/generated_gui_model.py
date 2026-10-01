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


class ButtonType(Enum):
    RaisedButton = "raised"


class ButtonActionType(Enum):
    Submit = "submit"


class InputFieldType(Enum):
    Text = "text"
    Password = "password"
    Email = "email"


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

    def __init__(self, type):
        self.type = type


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


inputFieldStyling = Styling(size=Size("100%", "40px", "15px", "0 0 15px", "14px", UnitSize.PIXELS), position=Position(PositionType.Relative), color=Color("#f2f2f2", "#000000", "#CCCCCC", background_color="", text_color="", border_color=""))
buttonStyling = Styling(size=Size("100%", "40px", "15px", "0 0 15px", "14px", UnitSize.PIXELS), position=Position(PositionType.Relative), color=Color("#4CAF50", "#FFFFFF", "#43A047", background_color="", text_color="", border_color=""))


class InputField:

    def __init__(self, name, description, type, styling):
        self.name = name
        self.description = description
        self.type = type
        self.styling = styling


class Button:

    def __init__(self, name, description, label, buttonType, actionType, styling):
        self.name = name
        self.description = description
        self.label = label
        self.buttonType = buttonType
        self.actionType = actionType
        self.styling = styling


class Form:

    def __init__(self, name, description, inputFields, styling=None):
        self.name = name
        self.description = description
        self.inputFields = inputFields
        self.styling = styling


registerForm = Form(
    name="RegisterForm",
    description="Form for user registration",
    inputFields={
        InputField("name", "Name input field", InputFieldType.Text, inputFieldStyling, type="", name="", description=""),
        InputField("password", "Password input field", InputFieldType.Password, inputFieldStyling, type="", name="", description=""),
        InputField("emailAddress", "Email input field", InputFieldType.Email, inputFieldStyling, type="", name="", description=""),
        Button("createButton", "Create account button", "Create", ButtonType.RaisedButton, ButtonActionType.Submit, buttonStyling, name="", description="", label="", buttonType="", actionType=""),
    },
)
loginForm = Form(
    name="LoginForm", description="Form for user login", inputFields={InputField("username", "Username input field", InputFieldType.Text, inputFieldStyling, type="", name="", description=""), InputField("password", "Password input field", InputFieldType.Password, inputFieldStyling, type="", name="", description=""), Button("loginButton", "Login button", "Login", ButtonType.RaisedButton, ButtonActionType.Submit, buttonStyling, name="", description="", label="", buttonType="", actionType="")}
)
ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)


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


loginPageScreen = Screen(name="LoginPage", description="Screen for user login and registration", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={registerForm, loginForm}, is_main_page=True, layout=ScreenLayout)


class Module:

    def __init__(self, name, screens):
        self.name = name
        self.screens = screens


loginModule = Module(name="LoginModule", screens={loginPageScreen})


class GUIModel:

    def __init__(self, name, package, versionCode, versionName, description, screenCompatibility, modules):
        self.name = name
        self.package = package
        self.versionCode = versionCode
        self.versionName = versionName
        self.description = description
        self.screenCompatibility = screenCompatibility
        self.modules = modules


gui_model = GUIModel(name="LoginApp", package="com.example.loginapp", versionCode="1", versionName="1.0", description="A web application for user login and registration.", screenCompatibility=True, modules={loginModule})
