from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#4F46E5", text_color="#FFFFFF", border_color="#4338CA")
buttonPosition = Position(type=PositionType.Relative, z_index=0)
buttonSize = Size(width="100%", height="40px", padding="8px", margin="24px", font_size="14px", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
InputFieldColor = Color(background_color="#FFFFFF", text_color="#000000", border_color="#D1D5DB")
inputFieldPosition = Position(type=PositionType.Relative, z_index=0)
inputFieldSize = Size(width="100%", height="40px", padding="8px", margin="24px", font_size="14px", unit_size=UnitSize.PIXELS)
inputFieldStyling = Styling(size=inputFieldSize, position=inputFieldPosition, color=InputFieldColor)
viewComponent = ViewComponent(name="StartupPage", description="Welcome page for the technology startup")
learnMoreButton = Button(name="LearnMoreButton", description="Button to learn more about the startup", label="Learn More", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, styling=buttonStyling)
emailInputField = InputField(name="EmailInputField", description="Input field for email subscription", type="Email", validationRules="required|email", styling=inputFieldStyling)
signUpButton = Button(name="SignUpButton", description="Button to sign up for email subscription", label="Sign up", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.SubmitForm, styling=buttonStyling)
emailForm = Form(name="EmailSubscriptionForm", description="Form for email subscription", inputFields={emailInputField}, styling=None)
StartupScreen = Screen(name="StartupScreen", description="Main screen for the technology startup", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={learnMoreButton, emailForm, signUpButton}, is_main_page=True, layout=ScreenLayout)
StartupModule = Module(name="StartupModule", screens={StartupScreen})
gui_model = GUIModel(name="StartupApp", package="com.example.startup", versionCode="1", versionName="1.0", description="A web application for a technology startup.", screenCompatibility=True, modules={StartupModule})
emailForm.attributes = {EmailForm_email}
