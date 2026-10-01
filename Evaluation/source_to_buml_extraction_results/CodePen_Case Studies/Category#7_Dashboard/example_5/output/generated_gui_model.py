from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#007BFF", text_color="#FFFFFF", border_color="#0056b3")
buttonPosition = Position(type=PositionType.Relative, z_index=10)
buttonSize = Size(width="auto", height="40px", padding="8px", margin="24px", font_size="14px", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
viewComponent = ViewComponent(name="NavbarView", description="Display a navigation bar with dropdowns and notifications")
navbarBrandButton = Button(name="NavbarBrandButton", description="Brand button", label="Brand", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, styling=buttonStyling)
navbarActivityButton = Button(name="NavbarActivityButton", description="Activity dropdown", label="Activity", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, styling=buttonStyling)
navbarNotificationButton = Button(name="NavbarNotificationButton", description="Notifications", label="Notifications", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, styling=buttonStyling)
navbarUserButton = Button(name="NavbarUserButton", description="User menu", label="User", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, styling=buttonStyling)
NavbarScreen = Screen(name="NavbarScreen", description="Navigation bar with dropdowns and notifications", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={navbarBrandButton, navbarActivityButton, navbarNotificationButton, navbarUserButton}, is_main_page=True, layout=ScreenLayout)
MyModule = Module(name="NavbarModule", screens={NavbarScreen})
gui_model = GUIModel(name="NavbarApp", package="com.example.navbarapp", versionCode="1", versionName="1.0", description="A web application with a navigation bar.", screenCompatibility=True, modules={MyModule})
