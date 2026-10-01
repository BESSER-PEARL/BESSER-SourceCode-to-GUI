from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#007BFF", text_color="#FFFFFF", border_color="#0056b3")
buttonPosition = Position(type=PositionType.Relative, z_index=10)
buttonSize = Size(height="40px", padding="8px", margin="24px", font_size="14px", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
inputFieldSize = Size(width="100%", padding="10px", unit_size=UnitSize.PIXELS)
inputFieldStyling = Styling(size=inputFieldSize)
checkboxSize = Size(width="20px", height="20px", unit_size=UnitSize.PIXELS)
checkboxStyling = Styling(size=checkboxSize)
viewComponent = ViewComponent(name="AuthView", description="Authentication form with signup and login options")
signupForm = Form(
    name="SignupForm",
    description="Form for creating a new account",
    inputFields={
        InputField(name="firstName", description="First Name", type="Text", validationRules="required", styling=inputFieldStyling),
        InputField(name="lastName", description="Last Name", type="Text", validationRules="required", styling=inputFieldStyling),
        InputField(name="emailAddress", description="Email Address", type="Email", validationRules="required", styling=inputFieldStyling),
        InputField(name="password", description="Password", type="Password", validationRules="required", styling=inputFieldStyling),
    },
    styling=None,
)
googleButton = Button(name="GoogleButton", description="Login with Google", label="Google", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Login, styling=buttonStyling)
facebookButton = Button(name="FacebookButton", description="Login with Facebook", label="Facebook", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Login, styling=buttonStyling)
termsCheckbox = InputField(name="terms", description="Agree to terms", type="Checkbox", validationRules="required", styling=checkboxStyling)
submitButton = Button(name="SubmitButton", description="Create Account", label="Create Account", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.SubmitForm, styling=buttonStyling)
loginForm = Form(name="LoginForm", description="Form for signing into an existing account", inputFields={InputField(name="emailAddress", description="Email Address", type="Email", validationRules="required", styling=inputFieldStyling), InputField(name="password", description="Password", type="Password", validationRules="required", styling=inputFieldStyling)}, styling=None)
rememberCheckbox = InputField(name="remember", description="Remember me", type="Checkbox", validationRules="", styling=checkboxStyling)
signInButton = Button(name="SignInButton", description="Sign In", label="Sign In", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.SubmitForm, styling=buttonStyling)
AuthScreen = Screen(name="AuthScreen", description="Screen for user authentication with signup and login forms", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={signupForm, googleButton, facebookButton, termsCheckbox, submitButton, loginForm, rememberCheckbox, signInButton}, is_main_page=True, layout=ScreenLayout)
AuthModule = Module(name="AuthModule", screens={AuthScreen})
gui_model = GUIModel(name="AuthApp", package="com.example.authapp", versionCode="1", versionName="1.0", description="An application for user authentication with signup and login features.", screenCompatibility=True, modules={AuthModule})
