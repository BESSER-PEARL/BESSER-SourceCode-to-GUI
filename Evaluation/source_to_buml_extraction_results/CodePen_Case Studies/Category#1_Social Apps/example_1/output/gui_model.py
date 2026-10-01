from besser.BUML.notations.sourceCode_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
InputFieldColor = Color(background_color="#FFFFFF", text_color="#000000", border_color="#CED4DA")
InputFieldPosition = Position(type=PositionType.Relative, alignment="center")
InputFieldSize = Size(width="100%", height="40px", padding="10px", margin="10px", font_size="16px", unit_size=UnitSize.PIXELS)
InputFieldStyling = Styling(size=InputFieldSize, position=InputFieldPosition, color=InputFieldColor)
FooterColor = Color(background_color="#F8F9FA", text_color="#6C757D", border_color="#E9ECEF")
FooterPosition = Position(type=PositionType.Fixed, bottom="20px", alignment="center")
FooterSize = Size(width="100%", height="auto", padding="10px", font_size="14px", unit_size=UnitSize.PIXELS)
FooterStyling = Styling(size=FooterSize, position=FooterPosition, color=FooterColor)
viewComponent = ViewComponent(name="InventoryPageView", description="Inventory and stock list page")
searchInputField = InputField(name="SearchInputField", description="Search for part number", type="Text", validationRules="", styling=InputFieldStyling)
footer = ViewComponent(name="Footer", description="Footer content", styling=FooterStyling)
InventoryPageScreen = Screen(name="InventoryPage", description="Page for managing inventory and stock list", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={searchInputField, footer}, is_main_page=True, layout=ScreenLayout)
InventoryModule = Module(name="InventoryModule", screens={InventoryPageScreen})
gui_model = GUIModel(name="InventoryManagementApp", package="com.example.inventorymanagement", versionCode="1", versionName="1.0", description="An application for managing inventory and stock lists.", screenCompatibility=True, modules={InventoryModule})
