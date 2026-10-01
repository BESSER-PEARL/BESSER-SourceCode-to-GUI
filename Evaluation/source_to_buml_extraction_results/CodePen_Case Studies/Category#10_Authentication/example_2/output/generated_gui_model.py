from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#007BFF", text_color="#FFFFFF", border_color="#0056b3")
buttonPosition = Position(type=PositionType.Relative, alignment="center", z_index=10)
buttonSize = Size(width="100px", height="40px", padding="8px", margin="24px", font_size="14px", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
inputFieldColor = Color(background_color="#FFFFFF", text_color="#000000", border_color="#CCCCCC")
inputFieldPosition = Position(type=PositionType.Relative, alignment="center", z_index=0)
inputFieldSize = Size(width="100%", height="auto", padding="10px", margin="5px", font_size="14px", unit_size=UnitSize.PIXELS)
inputFieldStyling = Styling(size=inputFieldSize, position=inputFieldPosition, color=inputFieldColor)
viewComponent = ViewComponent(name="AuthenticationView", description="User authentication form")
usernameField = InputField(name="username", description="Enter your username", type="Text", validationRules="minlength=3 maxlength=15 pattern=[a-zA-Z0-9]+ required", styling=inputFieldStyling)
passwordField = InputField(name="password", description="Enter your password", type="Password", validationRules="minlength=8 maxlength=15 pattern=[a-zA-Z0-9]+ required", styling=inputFieldStyling)
authenticationForm = Form(name="authenticationForm", description="User authentication form", inputFields={usernameField, passwordField}, styling=None)
submitButton = Button(name="submitButton", description="Submit the form", label="Submit", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Submit, styling=buttonStyling)
rulesButton = Button(name="rulesButton", description="Show rules", label="Rules", buttonType=ButtonType.TextButton, actionType=ButtonActionType.ShowList, styling=buttonStyling)
rulesList = DataList(name="rulesList", description="Authentication rules", list_sources=set(), styling=None)
AuthenticationScreen = Screen(name="AuthenticationScreen", description="User authentication page", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={authenticationForm, submitButton, rulesButton, rulesList}, is_main_page=True, layout=ScreenLayout)
AuthenticationModule = Module(name="AuthenticationModule", screens={AuthenticationScreen})
gui_model = GUIModel(name="AuthenticationApp", package="com.example.authentication", versionCode="1", versionName="1.0", description="A simple authentication application.", screenCompatibility=True, modules={AuthenticationModule})
