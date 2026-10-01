from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#1DA1F2", text_color="#FFFFFF", border_color="#1A91DA")
buttonPosition = Position(type=PositionType.Relative, z_index=10)
buttonSize = Size(width="100%", height="40", padding="8px", margin="24", font_size="14", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
inputFieldColor = Color(background_color="#FFFFFF", text_color="#000000", border_color="#CCCCCC")
inputFieldPosition = Position(type=PositionType.Relative, z_index=0)
inputFieldSize = Size(width="100%", height="40", padding="8px", margin="10", font_size="14", unit_size=UnitSize.PIXELS)
inputFieldStyling = Styling(size=inputFieldSize, position=inputFieldPosition, color=inputFieldColor)
viewComponent = ViewComponent(name="AccountAuthenticationView", description="Authenticate your Twitter account")
usernameInput = InputField(name="UsernameInput", description="Enter your username", type="Text", validationRules="required", styling=inputFieldStyling)
passwordInput = InputField(name="PasswordInput", description="Enter your password", type="Password", validationRules="required", styling=inputFieldStyling)
submitButton = Button(name="SubmitButton", description="Submit the form", label="Submit", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Submit, styling=buttonStyling)
authenticationForm = Form(name="AuthenticationForm", description="Form to authenticate user", inputFields={usernameInput, passwordInput}, styling=None)
AuthenticationScreen = Screen(name="AuthenticationScreen", description="Screen for account authentication", x_dpi=AccountAuthentication_success_url, y_dpi=AccountAuthentication_error_url, screen_size="Medium", view_elements={authenticationForm, submitButton}, is_main_page=True, layout=ScreenLayout)
AuthenticationModule = Module(name="AuthenticationModule", screens={AuthenticationScreen})
gui_model = GUIModel(name="TwitterAuthenticationApp", package="com.example.twitterauth", versionCode=AccountAuthentication_authenticity_token, versionName=AccountAuthentication_subject, description=AccountAuthentication_text, screenCompatibility=True, modules={AuthenticationModule})
