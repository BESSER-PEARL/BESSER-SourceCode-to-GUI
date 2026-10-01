from besser.BUML.notations.source_code_to_buml.output.buml.model import *from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *
from enum import Enum


class LayoutType(Enum):
    Flex = "flex"


class PositionType(Enum):
    Relative = "relative"


class ButtonType(Enum):
    RaisedButton = "raised"
    TextButton = "text"
    IconButton = "icon"


class ButtonActionType(Enum):
    Submit = "submit"
    Navigate = "navigate"
    Login = "login"


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


class Position:

    def __init__(self, type, alignment, z_index=0):
        self.type = type
        self.alignment = alignment
        self.z_index = z_index


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


ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#dd9966", text_color="#FFFFFF", border_color="#cc8855")
buttonPosition = Position(type=PositionType.Relative, alignment="center", z_index=10)
buttonSize = Size(width="100%", height="40px", padding="15px", margin="24px", font_size="16px", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
inputFieldColor = Color(background_color="#f8f8f8", text_color="#000000", border_color="#CCCCCC")
inputFieldPosition = Position(type=PositionType.Relative, alignment="center")
inputFieldSize = Size(width="100%", height="40px", padding="12px", margin="25px", font_size="16px", unit_size=UnitSize.PIXELS)
inputFieldStyling = Styling(size=inputFieldSize, position=inputFieldPosition, color=inputFieldColor)


class ViewComponent:

    def __init__(self, name, description):
        self.name = name
        self.description = description


class Image(ViewComponent):
    pass


class Form(ViewComponent):

    def __init__(self, name, description, inputFields):
        super().__init__(name, description)
        self.inputFields = inputFields


class InputField(ViewComponent):

    def __init__(self, name, description, type, validationRules, styling, property):
        super().__init__(name, description)
        self.type = type
        self.validationRules = validationRules
        self.styling = styling
        self.property = property


class Button(ViewComponent):

    def __init__(self, name, description, label, buttonType, actionType, styling=None):
        super().__init__(name, description)
        self.label = label
        self.buttonType = buttonType
        self.actionType = actionType
        self.styling = styling


loginImage = Image(name="LoginImage", description="African woman in headwrap")
loginForm = Form(name="LoginForm", description="User login form", inputFields={InputField(name="UsernameField", description="Enter your username", type="Text", validationRules="required", styling=inputFieldStyling), InputField(name="PasswordField", description="Enter your password", type="Password", validationRules="required", styling=inputFieldStyling)})
submitButton = Button(name="SubmitButton", description="Submit login form", label="SUBMIT", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Submit, styling=buttonStyling)
forgotPasswordButton = Button(name="ForgotPasswordButton", description="Forgot password link", label="Forgot your password?", buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate)
createAccountButton = Button(name="CreateAccountButton", description="Create an account link", label="Create an Account", buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate)
googleLoginButton = Button(name="GoogleLoginButton", description="Login with Google", label="Google", buttonType=ButtonType.IconButton, actionType=ButtonActionType.Login)
facebookLoginButton = Button(name="FacebookLoginButton", description="Login with Facebook", label="Facebook", buttonType=ButtonType.IconButton, actionType=ButtonActionType.Login)


class Screen(ViewComponent):

    def __init__(self, name, description, x_dpi, y_dpi, screen_size, view_elements, is_main_page, layout):
        super().__init__(name, description)
        self.x_dpi = x_dpi
        self.y_dpi = y_dpi
        self.screen_size = screen_size
        self.view_elements = view_elements
        self.is_main_page = is_main_page
        self.layout = layout


LoginScreen = Screen(name="LoginScreen", description="User login screen", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={loginImage, loginForm, submitButton, forgotPasswordButton, createAccountButton, googleLoginButton, facebookLoginButton}, is_main_page=True, layout=ScreenLayout)


class Module(ViewComponent):

    def __init__(self, name, screens):
        super().__init__(name, "")
        self.screens = screens


LoginModule = Module(name="LoginModule", screens={LoginScreen})


class GUIModel(ViewComponent):

    def __init__(self, name, package, versionCode, versionName, description, screenCompatibility, modules):
        super().__init__(name, description)
        self.package = package
        self.versionCode = versionCode
        self.versionName = versionName
        self.screenCompatibility = screenCompatibility
        self.modules = modules


gui_model = GUIModel(name="LoginApp", package="com.example.loginapp", versionCode="1", versionName="1.0", description="A user login application", screenCompatibility=True, modules={LoginModule})
