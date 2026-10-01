from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
inputFieldColor = Color(background_color="#FFFFFF", text_color="#000000", border_color="#CCCCCC")
inputFieldPosition = Position(type=PositionType.Relative, z_index=0)
inputFieldSize = Size(width="100%", height="35px", padding="8px", margin="5px", font_size="14px", unit_size=UnitSize.PIXELS)
inputFieldStyling = Styling(size=inputFieldSize, position=inputFieldPosition, color=inputFieldColor)
buttonColor = Color(background_color="#f5ba1a", text_color="#FFFFFF", border_color="#f5ba1a")
buttonPosition = Position(type=PositionType.Relative, z_index=0)
buttonSize = Size(width="100%", height="35px", padding="0px", margin="10px 0", font_size="16px", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=buttonColor)
registrationForm = Form(
    name="RegistrationForm",
    description="Responsive Registration Form",
    inputFields={
        InputField(name="email", description="Email", type=InputFieldType.Email, validationRules="required", styling=inputFieldStyling),
        InputField(name="password", description="Password", type=InputFieldType.Password, validationRules="required", styling=inputFieldStyling),
        InputField(name="retypePassword", description="Re-type Password", type=InputFieldType.Password, validationRules="required", styling=inputFieldStyling),
        InputField(name="firstName", description="First Name", type=InputFieldType.Text, validationRules="", styling=inputFieldStyling),
        InputField(name="lastName", description="Last Name", type=InputFieldType.Text, validationRules="required", styling=inputFieldStyling),
        InputField(name="gender", description="Gender", type=InputFieldType.Text, validationRules="", styling=inputFieldStyling),
        InputField(name="country", description="Country", type=InputFieldType.Text, validationRules="", styling=inputFieldStyling),
        InputField(name="agreeTerms", description="Agree with terms and conditions", type=InputFieldType.Boolean, validationRules="", styling=inputFieldStyling),
        InputField(name="receiveNewsletter", description="Receive the newsletter", type=InputFieldType.Boolean, validationRules="", styling=inputFieldStyling),
    },
)
registerButton = Button(name="RegisterButton", description="Register", label="Register", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.SubmitForm, styling=buttonStyling)
registrationScreen = Screen(name="RegistrationScreen", description="Screen for user registration", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={registrationForm, registerButton}, is_main_page=True, layout=ScreenLayout)
registrationModule = Module(name="RegistrationModule", screens={registrationScreen})
gui_model = GUIModel(name="RegistrationApp", package="com.example.registrationapp", versionCode="1", versionName="1.0", description="A web application for user registration.", screenCompatibility=True, modules={registrationModule})
