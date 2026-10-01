from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#28a745", text_color="#FFFFFF", border_color="#218838")
buttonPosition = Position(type=PositionType.Relative, top="", left="", right="", bottom="", alignment="", z_index=0)
buttonSize = Size(width="100%", height="40px", padding="10px", margin="0", font_size="14px", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
TableColor = Color(background_color="#FFFFFF", text_color="#343A40", border_color="#ddd")
tablePosition = Position(type=PositionType.Relative, top="20px", left="", right="", bottom="", alignment="", z_index=0)
tableSize = Size(width="100%", height="auto", padding="10px", margin="20px 0", font_size="14px", unit_size=UnitSize.PIXELS)
tableStyling = Styling(size=tableSize, position=tablePosition, color=TableColor)
AlertColor = Color(background_color="#f8d7da", text_color="#721c24", border_color="#f5c6cb")
alertStyling = Styling(size=tableSize, position=tablePosition, color=AlertColor)
viewComponent: ViewComponent = ViewComponent(name="GroceryInventoryTrackerView", description="Manage grocery inventory with CRUD operations")
addItemForm: Form = Form(
    name="AddItemForm", description="Form to add new items to the inventory", inputFields={InputField(name="ItemName", description="Name of the item", type="Text", validationRules="required", styling=None), InputField(name="ItemQuantity", description="Quantity of the item", type="Number", validationRules="required", styling=None), InputField(name="ItemThreshold", description="Alert threshold for the item", type="Number", validationRules="required", styling=None)}, styling=None
)
addItemButton: Button = Button(name="AddItemButton", description="Button to add item to the inventory", label="Add Item", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add, styling=buttonStyling)
inventoryTable: DataList = DataList(name="InventoryTable", description="Table displaying the list of items in the inventory", list_sources={DataSourceElement(name="ItemDataSource", dataSourceClass=Item, fields=[Item_name, Item_quantity, Item_threshold])}, styling=tableStyling)
GroceryInventoryTrackerScreen: Screen = Screen(name="GroceryInventoryTrackerScreen", description="Screen to manage grocery inventory", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={addItemForm, addItemButton, inventoryTable}, is_main_page=True, layout=ScreenLayout)
GroceryModule: Module = Module(name="GroceryModule", screens={GroceryInventoryTrackerScreen})
gui_model: GUIModel = GUIModel(name="GroceryInventoryApp", package="com.example.groceryinventory", versionCode="1", versionName="1.0", description="A web application for managing grocery inventory.", screenCompatibility=True, modules={GroceryModule})
