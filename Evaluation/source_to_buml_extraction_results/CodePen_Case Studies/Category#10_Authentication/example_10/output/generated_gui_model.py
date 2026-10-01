from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#007BFF", text_color="#FFFFFF", border_color="#0056b3")
buttonPosition = Position(type=PositionType.Relative, alignment="center", z_index=10)
buttonSize = Size(width="auto", height="40px", padding="8px", margin="24px", font_size="14px", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
inputFieldColor = Color(background_color="#FFFFFF", text_color="#000000", border_color="#CCCCCC")
inputFieldPosition = Position(type=PositionType.Relative, alignment="center", z_index=0)
inputFieldSize = Size(width="auto", height="30px", padding="5px", margin="10px", font_size="14px", unit_size=UnitSize.PIXELS)
inputFieldStyling = Styling(size=inputFieldSize, position=inputFieldPosition, color=inputFieldColor)
imagePosition = Position(type=PositionType.Relative, alignment="center", z_index=0)
imageSize = Size(width="200px", height="200px", unit_size=UnitSize.PIXELS)
imageStyling = Styling(size=imageSize, position=imagePosition)
userImage = Image(name="userImage", styling=imageStyling, description="")
googleAuthButton = Button(name="GoogleAuthButton", description="Sign up with Google", label="Sign up with Google", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Login, styling=buttonStyling)
signUpForm = Form(
    name="SignUpForm",
    description="User sign up form",
    inputFields={InputField(name="fname", description="First name", type="Text", styling=inputFieldStyling), InputField(name="lname", description="Last name", type="Text", styling=inputFieldStyling), InputField(name="uname", description="Username", type="Text", styling=inputFieldStyling), InputField(name="email", description="Email", type="Email", styling=inputFieldStyling), InputField(name="pword", description="Password", type="Password", styling=inputFieldStyling)},
)
submitButton = Button(name="SubmitButton", description="Submit sign up form", label="Sign Up", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.SubmitForm, styling=buttonStyling)
SignUpScreen = Screen(name="SignUpScreen", description="User sign up screen", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={userImage, googleAuthButton, signUpForm, submitButton}, is_main_page=True, layout=ScreenLayout)
SignUpModule = Module(name="SignUpModule", screens={SignUpScreen})
gui_model = GUIModel(name="UserSignUpApp", package="com.example.usersignup", versionCode="1", versionName="1.0", description="A web application for user sign up.", screenCompatibility=True, modules={SignUpModule})
