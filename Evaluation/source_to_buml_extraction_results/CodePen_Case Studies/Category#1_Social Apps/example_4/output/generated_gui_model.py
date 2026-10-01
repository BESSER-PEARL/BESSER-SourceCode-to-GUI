from besser.BUML.notations.source_code_to_gui.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *
from enum import Enum


class LayoutType(Enum):
    Flex = "flex"


class PositionType(Enum):
    Relative = "relative"


class ButtonType(Enum):
    IconButton = "icon_button"
    RaisedButton = "raised_button"


class ButtonActionType(Enum):
    Login = "login"
    SubmitForm = "submit_form"


class InputFieldType(Enum):
    Email = "email"
    Password = "password"


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


class Position:

    def __init__(self, type, z_index=0):
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


class ViewContainer(ViewComponent):
    pass


class Button(ViewComponent):

    def __init__(self, name, description, label, buttonType, actionType, styling):
        super().__init__(name, description)
        self.label = label
        self.buttonType = buttonType
        self.actionType = actionType
        self.styling = styling


class InputField(ViewComponent):

    def __init__(self, name, description, type, validationRules, styling, property):
        super().__init__(name, description)
        self.type = type
        self.validationRules = validationRules
        self.styling = styling
        self.property = property


class Form(ViewComponent):

    def __init__(self, name, description, inputFields):
        super().__init__(name, description)
        self.inputFields = inputFields


class Screen(ViewContainer):

    def __init__(self, name, description, x_dpi, y_dpi, screen_size, is_main_page, view_elements, layout):
        super().__init__(name, description)
        self.x_dpi = x_dpi
        self.y_dpi = y_dpi
        self.screen_size = screen_size
        self.is_main_page = is_main_page
        self.view_elements = view_elements
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
buttonSize = Size(width="100%", height="40px", padding="8px", margin="24px", font_size="14px", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
inputFieldStyling = Styling(size=Size(width="100%", height="40px", padding="8px", margin="20px", font_size="16px", unit_size=UnitSize.PIXELS), position=Position(type=PositionType.Relative), color=Color(background_color="#FFFFFF", text_color="#000000", border_color="#CCCCCC"))
viewComponent = ViewComponent(name="SignUpView", description="Sign up page with social and traditional sign up options")
socialSignInSection = ViewContainer(name="SocialSignInSection", description="Social sign in options", view_elements="")
googleButton = Button(name="GoogleSignInButton", description="Sign in with Google", label="Google", buttonType=ButtonType.IconButton, actionType=ButtonActionType.Login, styling=buttonStyling)
twitterButton = Button(name="TwitterSignInButton", description="Sign in with Twitter", label="Twitter", buttonType=ButtonType.IconButton, actionType=ButtonActionType.Login, styling=buttonStyling)
facebookButton = Button(name="FacebookSignInButton", description="Sign in with Facebook", label="Facebook", buttonType=ButtonType.IconButton, actionType=ButtonActionType.Login, styling=buttonStyling)
linkedinButton = Button(name="LinkedInSignInButton", description="Sign in with LinkedIn", label="LinkedIn", buttonType=ButtonType.IconButton, actionType=ButtonActionType.Login, styling=buttonStyling)
signUpForm = Form(name="SignUpForm", description="Traditional sign up form", inputFields=set())
emailField = InputField(name="EmailField", description="Email input field", type=InputFieldType.Email, validationRules="required", styling=inputFieldStyling)
passwordField = InputField(name="PasswordField", description="Password input field", type=InputFieldType.Password, validationRules="required", styling=inputFieldStyling)
passwordConfirmationField = InputField(name="PasswordConfirmationField", description="Password confirmation input field", type=InputFieldType.Password, validationRules="required", styling=inputFieldStyling)
signUpForm.inputFields.update({emailField, passwordField, passwordConfirmationField})
submitButton = Button(name="SubmitButton", description="Submit sign up form", label="Sign Up", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.SubmitForm, styling=buttonStyling)
SignUpScreen = Screen(name="SignUpScreen", description="Screen for user sign up", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", is_main_page=True, view_elements={socialSignInSection, signUpForm, submitButton}, layout=ScreenLayout)
SignUpModule = Module(name="SignUpModule", screens={SignUpScreen})
gui_model = GUIModel(name="SignUpApp", package="com.example.signupapp", versionCode="1", versionName="1.0", description="An application for user sign up", screenCompatibility=True, modules={SignUpModule})
