from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
inputFieldColor = Color(background_color="#0a0a23", text_color="#ffffff", border_color="#0a0a23")
inputFieldPosition = Position(type=PositionType.Relative, alignment="left")
inputFieldSize = Size(width="100%", height="40px", padding="10px", margin="5px", font_size="16px", unit_size=UnitSize.PIXELS)
inputFieldStyling = Styling(size=inputFieldSize, position=inputFieldPosition, color=inputFieldColor)
buttonColor = Color(background_color="#3b3b4f", text_color="#FFFFFF", border_color="white")
buttonPosition = Position(type=PositionType.Relative, alignment="center")
buttonSize = Size(width="60%", height="40px", padding="10px", margin="20px auto", font_size="1.1rem", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=buttonColor)
registrationForm = Form(
    name="RegistrationForm",
    description="User registration form",
    inputFields={
        InputField(name="RegistrationForm_firstName", description="Enter Your First Name", type="Text", validationRules="required", styling=inputFieldStyling),
        InputField(name="RegistrationForm_lastName", description="Enter Your Last Name", type="Text", validationRules="required", styling=inputFieldStyling),
        InputField(name="RegistrationForm_email", description="Enter Your Email", type="Email", validationRules="required", styling=inputFieldStyling),
        InputField(name="RegistrationForm_newPassword", description="Create a New Password", type="Password", validationRules="pattern=[a-z0-5]{8,}", styling=inputFieldStyling),
        InputField(name="RegistrationForm_accountType", description="Select Account Type", type="Radio", validationRules="required", styling=inputFieldStyling),
        InputField(name="RegistrationForm_profilePicture", description="Upload a profile picture", type="File", styling=inputFieldStyling),
        InputField(name="RegistrationForm_age", description="Input your age (years)", type="Number", validationRules="min=13 max=120", styling=inputFieldStyling),
        InputField(name="RegistrationForm_referrer", description="How did you hear about us?", type="Select", styling=inputFieldStyling),
        InputField(name="RegistrationForm_bio", description="Provide a bio", type="Text", styling=inputFieldStyling),
        InputField(name="RegistrationForm_termsAndConditions", description="I accept the terms and conditions", type="Checkbox", validationRules="required", styling=inputFieldStyling),
    },
)
submitButton = Button(name="SubmitButton", description="Submit the registration form", label="Submit", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Submit, styling=buttonStyling)
RegistrationScreen = Screen(name="RegistrationScreen", description="User registration screen", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={registrationForm, submitButton}, is_main_page=True, layout=ScreenLayout)
RegistrationModule = Module(name="RegistrationModule", screens={RegistrationScreen})
gui_model = GUIModel(name="RegistrationApp", package="com.example.registrationapp", versionCode="1", versionName="1.0", description="A user registration application.", screenCompatibility=True, modules={RegistrationModule})
