from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#0062cc", text_color="#FFFFFF", border_color="#0056b3")
buttonPosition = Position(type=PositionType.Relative, z_index=10)
buttonSize = Size(height="40px", padding="8px", margin="24px", font_size="14px", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
inputFieldColor = Color(background_color="#FFFFFF", text_color="#000000", border_color="#CCCCCC")
inputFieldPosition = Position(type=PositionType.Relative)
inputFieldSize = Size(width="100%", padding="10px", margin="5px", font_size="14px", unit_size=UnitSize.PIXELS)
inputFieldStyling = Styling(size=inputFieldSize, position=inputFieldPosition, color=inputFieldColor)
viewComponent = ViewComponent(name="UserRegistrationView", description="User registration form for employees and hirers")
employeeForm = Form(
    name="EmployeeForm",
    description="Form for employee registration",
    inputFields={
        InputField(name="firstName", description="First Name", type=InputFieldType.Text, styling=inputFieldStyling),
        InputField(name="lastName", description="Last Name", type=InputFieldType.Text, styling=inputFieldStyling),
        InputField(name="password", description="Password", type=InputFieldType.Password, styling=inputFieldStyling),
        InputField(name="confirmPassword", description="Confirm Password", type=InputFieldType.Password, styling=inputFieldStyling),
        InputField(name="gender", description="Gender", type=InputFieldType.Text, styling=inputFieldStyling),
        InputField(name="email", description="Email", type=InputFieldType.Email, styling=inputFieldStyling),
        InputField(name="phone", description="Phone", type=InputFieldType.Text, styling=inputFieldStyling),
        InputField(name="securityQuestion", description="Security Question", type=InputFieldType.Text, styling=inputFieldStyling),
        InputField(name="securityAnswer", description="Security Answer", type=InputFieldType.Text, styling=inputFieldStyling),
    },
)
hirerForm = Form(
    name="HirerForm",
    description="Form for hirer registration",
    inputFields={
        InputField(name="firstName", description="First Name", type=InputFieldType.Text, styling=inputFieldStyling),
        InputField(name="lastName", description="Last Name", type=InputFieldType.Text, styling=inputFieldStyling),
        InputField(name="email", description="Email", type=InputFieldType.Email, styling=inputFieldStyling),
        InputField(name="phone", description="Phone", type=InputFieldType.Text, styling=inputFieldStyling),
        InputField(name="password", description="Password", type=InputFieldType.Password, styling=inputFieldStyling),
        InputField(name="confirmPassword", description="Confirm Password", type=InputFieldType.Password, styling=inputFieldStyling),
        InputField(name="securityQuestion", description="Security Question", type=InputFieldType.Text, styling=inputFieldStyling),
        InputField(name="securityAnswer", description="Security Answer", type=InputFieldType.Text, styling=inputFieldStyling),
    },
)
loginButton = Button(name="LoginButton", description="Login button", label="Login", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Login, styling=buttonStyling)
registerButton = Button(name="RegisterButton", description="Register button", label="Register", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.SubmitForm, styling=buttonStyling)
UserRegistrationScreen = Screen(name="UserRegistrationScreen", description="Screen for user registration", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={employeeForm, hirerForm, loginButton, registerButton}, is_main_page=True, layout=ScreenLayout)
UserRegistrationModule = Module(name="UserRegistrationModule", screens={UserRegistrationScreen})
gui_model = GUIModel(name="UserRegistrationApp", package="com.example.userregistration", versionCode="1", versionName="1.0", description="Application for user registration", screenCompatibility=True, modules={UserRegistrationModule})
