from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

searchInputColor = Color(background_color="#FFFFFF", text_color="#000000", border_color="#CCCCCC")
searchInputPosition = Position(type=PositionType.Relative, alignment="center", z_index=0)
searchInputSize = Size(width="100%", height="40px", padding="20px", margin="10px", font_size="14px", unit_size=UnitSize.PIXELS)
searchInputStyling = Styling(size=searchInputSize, position=searchInputPosition, color=searchInputColor)
tableColor = Color(background_color="#FFFFFF", text_color="#000000", border_color="#CCCCCC")
tablePosition = Position(type=PositionType.Relative, alignment="center", z_index=0)
tableSize = Size(width="100%", height="auto", padding="10px", margin="10px", font_size="14px", unit_size=UnitSize.PIXELS)
tableStyling = Styling(size=tableSize, position=tablePosition, color=tableColor)
buttonColor = Color(background_color="#007BFF", text_color="#FFFFFF", border_color="#0056b3")
buttonPosition = Position(type=PositionType.Inline, z_index=0)
buttonSize = Size(width="40px", height="40px", padding="5px", margin="5px", font_size="14px", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=buttonColor)
searchInputField = InputField(name="SearchInput", description="Search inventory", type=InputFieldType.Search, validationRules="", styling=searchInputStyling)
minusButton = Button(name="MinusButton", description="Decrease quantity", label="-", buttonType=ButtonType.IconButton, actionType=ButtonActionType.Edit, styling=buttonStyling)
plusButton = Button(name="PlusButton", description="Increase quantity", label="+", buttonType=ButtonType.IconButton, actionType=ButtonActionType.Edit, styling=buttonStyling)
inventoryDataSource = DataSourceElement(name="InventoryDataSource", dataSourceClass=InventoryItem, fields={InventoryItem_number, InventoryItem_name, InventoryItem_price, InventoryItem_quantity})
inventoryList = DataList(name="InventoryList", description="List of inventory items", list_sources={inventoryDataSource}, styling=tableStyling)
InventoryScreen = Screen(name="InventoryScreen", description="Manage inventory items", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", is_main_page=True, view_elements={searchInputField, inventoryList, minusButton, plusButton})
InventoryModule = Module(name="InventoryModule", screens={InventoryScreen})
gui_model = GUIModel(name="InventoryApp", package="com.example.inventoryapp", versionCode="1", versionName="1.0", description="An application to manage inventory items.", screenCompatibility=True, modules={InventoryModule})
