from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#1b51ff", text_color="#FFFFFF", border_color="#0056b3")
buttonPosition = Position(type=PositionType.Relative, z_index=10)
buttonSize = Size(height="40px", padding="12px 20px", margin="8px 0", font_size="14px", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
InputFieldColor = Color(background_color="#FFFFFF", text_color="#000000", border_color="#132")
inputFieldPosition = Position(type=PositionType.Relative)
inputFieldSize = Size(height="30px", padding="2.5px 3.75px", margin="8px 0", font_size="14px", unit_size=UnitSize.PIXELS)
inputFieldStyling = Styling(size=inputFieldSize, position=inputFieldPosition, color=InputFieldColor)
viewComponent = ViewComponent(name="LoginView", description="User login form")
usernameInput = InputField(name="UsernameInput", description="Enter your username", type="Text", validationRules="required", styling=inputFieldStyling)
passwordInput = InputField(name="PasswordInput", description="Enter your password", type="Password", validationRules="required", styling=inputFieldStyling)
loginForm = Form(name="LoginForm", description="Form for user login", inputFields={usernameInput, passwordInput}, styling=None)
loginButton = Button(name="LoginButton", description="Submit login form", label="Enter", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Login, styling=buttonStyling)
signupLinkColor = Color(background_color="transparent", text_color="#1b51ff", border_color="transparent")
signupLinkStyling = Styling(size=None, position=None, color=signupLinkColor)
signupLink = Button(name="SignupLink", description="Navigate to signup page", label="Sign up", buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate, styling=signupLinkStyling)
LoginScreen = Screen(name="LoginScreen", description="Screen for user login", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={loginForm, loginButton, signupLink}, is_main_page=True, layout=ScreenLayout)
LoginModule = Module(name="LoginModule", screens={LoginScreen})
gui_model = GUIModel(name="LoginApp", package="com.example.loginapp", versionCode="1", versionName="1.0", description="A simple login application.", screenCompatibility=True, modules={LoginModule})
