from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
MenuColor = Color(background_color="#FFFFFF", text_color="#000000", border_color="#CCCCCC")
MenuPosition = Position(type=PositionType.Relative)
MenuSize = Size(width="100%", height="auto", padding="10px", font_size="14", unit_size=UnitSize.PIXELS)
MenuStyling = Styling(size=MenuSize, position=MenuPosition, color=MenuColor)
FormColor = Color(background_color="#FFFFFF", text_color="#000000", border_color="#CCCCCC")
FormPosition = Position(type=PositionType.Relative)
FormSize = Size(width="100%", height="auto", padding="10px", font_size="14", unit_size=UnitSize.PIXELS)
FormStyling = Styling(size=FormSize, position=FormPosition, color=FormColor)
InputFieldColor = Color(background_color="#FFFFFF", text_color="#000000", border_color="#CCCCCC")
InputFieldPosition = Position(type=PositionType.Relative)
InputFieldSize = Size(width="100%", height="auto", padding="10px", font_size="14", unit_size=UnitSize.PIXELS)
InputFieldStyling = Styling(size=InputFieldSize, position=InputFieldPosition, color=InputFieldColor)
viewComponent: ViewComponent = ViewComponent(name="WebPageView", description="Display a web page with menu and form")
mainMenu: Menu = Menu(name="MainMenu", description="Main navigation menu", menuItems={MenuItem(label="Home"), MenuItem(label="Messages"), MenuItem(label="Friends"), MenuItem(label="Logout")}, styling=MenuStyling)
searchInput: SearchInput = SearchInput(name="SearchInput", description="Search input field", type=InputFieldType.Text, validationRules="", styling=InputFieldStyling, attributes={SearchInput_placeholder})
mainForm: Form = Form(name="MainForm", description="Main form with text fields", inputFields={TextField(name="FirstName", description="First name input field", type=InputFieldType.Text, validationRules="", styling=InputFieldStyling, attributes={TextField_name, TextField_placeholder}), TextArea(name="ExampleText", description="Example text area", type=InputFieldType.Text, validationRules="", styling=InputFieldStyling, attributes={TextArea_placeholder})}, styling=FormStyling)
WebPageScreen: Screen = Screen(name="WebPageScreen", description="Web page screen with menu and form", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={mainMenu, searchInput, mainForm}, is_main_page=True, layout=ScreenLayout)
WebPageModule: Module = Module(name="WebPageModule", screens={WebPageScreen})
gui_model: GUIModel = GUIModel(name="WebApp", package="com.example.webapp", versionCode="1", versionName="1.0", description="A web application with a menu and form.", screenCompatibility=True, modules={WebPageModule})
