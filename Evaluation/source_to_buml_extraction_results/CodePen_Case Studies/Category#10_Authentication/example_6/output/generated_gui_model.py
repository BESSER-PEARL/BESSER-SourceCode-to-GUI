from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#ffbaac", text_color="#FFFFFF", border_color="#0056b3")
buttonPosition = Position(type=PositionType.Relative, alignment="center", z_index=10)
buttonSize = Size(width="100px", height="40px", padding="8px", margin="24px", font_size="14px", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
viewComponent = ViewComponent(name="AuthenticationView", description="User authentication interface")
loginForm = Form(name="LoginForm", description="User login form", inputFields={InputField(name="email", description="User email", type=InputFieldType.Email), InputField(name="password", description="User password", type=InputFieldType.Password)})
registerForm = Form(name="RegisterForm", description="User registration form", inputFields={InputField(name="email", description="User email", type=InputFieldType.Email), InputField(name="password", description="User password", type=InputFieldType.Password), InputField(name="confirmPassword", description="Confirm password", type=InputFieldType.Password)})
loginButton = Button(name="LoginButton", description="Submit login form", label="Login", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.SubmitForm, styling=buttonStyling)
registerButton = Button(name="RegisterButton", description="Submit registration form", label="Create", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.SubmitForm, styling=buttonStyling)
createAccountLink = Button(name="CreateAccountLink", description="Switch to registration form", label="Create Account", buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate)
alreadyHaveAccountLink = Button(name="AlreadyHaveAccountLink", description="Switch to login form", label="Already have an account?", buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate)
loginNote = ViewComponent(name="LoginNote", description="Login note", styling=None)
registerNote = ViewComponent(name="RegisterNote", description="Register note", styling=None)
AuthenticationScreen = Screen(name="AuthenticationScreen", description="User authentication screen", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={loginForm, registerForm, loginButton, registerButton, createAccountLink, alreadyHaveAccountLink, loginNote, registerNote}, is_main_page=True, layout=ScreenLayout)
AuthenticationModule = Module(name="AuthenticationModule", screens={AuthenticationScreen})
gui_model = GUIModel(name="AuthenticationApp", package="com.example.authentication", versionCode="1", versionName="1.0", description="User authentication application", screenCompatibility=True, modules={AuthenticationModule})
