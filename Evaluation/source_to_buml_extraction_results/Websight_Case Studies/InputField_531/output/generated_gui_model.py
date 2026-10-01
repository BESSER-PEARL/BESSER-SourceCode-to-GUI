from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
HeaderColor = Color(background_color="#FFFFFF", text_color="#000000", border_color="#CCCCCC")
HeaderPosition = Position(type=PositionType.Relative, top="0", left="0", right="0", bottom="", alignment="center", z_index=10)
HeaderSize = Size(width="100%", height="auto", padding="10px", margin="0", font_size="16px", icon_size="", unit_size=UnitSize.PIXELS)
HeaderStyling = Styling(size=HeaderSize, position=HeaderPosition, color=HeaderColor)
ButtonColor = Color(background_color="#EF4444", text_color="#FFFFFF", border_color="#DC2626")
ButtonPosition = Position(type=PositionType.Relative, top="", left="", right="", bottom="", alignment="", z_index=0)
ButtonSize = Size(width="auto", height="40px", padding="8px", margin="4px", font_size="14px", icon_size="", unit_size=UnitSize.PIXELS)
ButtonStyling = Styling(size=ButtonSize, position=ButtonPosition, color=ButtonColor)
InputFieldColor = Color(background_color="#FFFFFF", text_color="#000000", border_color="#CCCCCC")
InputFieldPosition = Position(type=PositionType.Relative, top="", left="", right="", bottom="", alignment="", z_index=0)
InputFieldSize = Size(width="auto", height="40px", padding="8px", margin="4px", font_size="14px", icon_size="", unit_size=UnitSize.PIXELS)
InputFieldStyling = Styling(size=InputFieldSize, position=InputFieldPosition, color=InputFieldColor)
MainColor = Color(background_color="#F3F4F6", text_color="#000000", border_color="#CCCCCC")
MainPosition = Position(type=PositionType.Relative, top="0", left="0", right="0", bottom="", alignment="center", z_index=0)
MainSize = Size(width="100%", height="auto", padding="10px", margin="0", font_size="16px", icon_size="", unit_size=UnitSize.PIXELS)
MainStyling = Styling(size=MainSize, position=MainPosition, color=MainColor)
FooterColor = Color(background_color="#FFFFFF", text_color="#000000", border_color="#CCCCCC")
FooterPosition = Position(type=PositionType.Relative, top="", left="0", right="0", bottom="0", alignment="center", z_index=10)
FooterSize = Size(width="100%", height="auto", padding="10px", margin="0", font_size="16px", icon_size="", unit_size=UnitSize.PIXELS)
FooterStyling = Styling(size=FooterSize, position=FooterPosition, color=FooterColor)
headerComponent = ViewComponent(name="Header", description="Header section with logo and navigation", styling=HeaderStyling)
mainComponent = ViewComponent(name="Main", description="Main content area", styling=MainStyling)
footerComponent = ViewComponent(name="Footer", description="Footer section with social links", styling=FooterStyling)
signUpButton = Button(name="SignUpButton", description="Sign up button", label="Sign Up", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, styling=ButtonStyling)
searchInputField = InputField(name="SearchInput", description="Search input field", type="Text", validationRules="", styling=InputFieldStyling)
menuItems = {MenuItem(label="Home"), MenuItem(label="About"), MenuItem(label="Services"), MenuItem(label="Contact")}
navigationMenu = Menu(name="NavigationMenu", description="Navigation menu", menuItems=menuItems, styling=HeaderStyling)
HomeScreen = Screen(name="HomeScreen", description="Home screen with header, main content, and footer", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={headerComponent, mainComponent, footerComponent, signUpButton, searchInputField, navigationMenu}, is_main_page=True, layout=ScreenLayout)
MyModule = Module(name="MainModule", screens={HomeScreen})
gui_model = GUIModel(name="TechCompanyApp", package="com.example.techcompany", versionCode="1", versionName="1.0", description="A web application for a tech company", screenCompatibility=True, modules={MyModule})
WebPage_header.type = Header
WebPage_main.type = Main
WebPage_footer.type = Footer
