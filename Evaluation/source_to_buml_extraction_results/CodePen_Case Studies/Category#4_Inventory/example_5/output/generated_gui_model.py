from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
TableColor = Color(background_color="#FFFFFF", text_color="#000000", border_color="#CCCCCC")
TablePosition = Position(type=PositionType.Relative, top="20px", left="20px", right="20px", bottom="20px")
TableSize = Size(width="100%", height="auto", padding="10px", margin="10px", font_size="14")
TableStyling = Styling(size=TableSize, position=TablePosition, color=TableColor)
viewComponent: ViewComponent = ViewComponent(name="InventoryListView", description="Display a list of inventory items")
datasource_inventory: DataSourceElement = DataSourceElement(name="InventoryDataSource", dataSourceClass=InventoryItem, fields=[InventoryItem_itemName, InventoryItem_quantity, InventoryItem_supplier, InventoryItem_manufacturer, InventoryItem_id])
inventoryList: DataList = DataList(name="InventoryList", description="A list of inventory items", list_sources={datasource_inventory}, styling=TableStyling)
InventoryListScreen: Screen = Screen(name="InventoryListScreen", description="Screen displaying the inventory list", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={inventoryList}, layout=ScreenLayout, is_main_page=True)
InventoryModule: Module = Module(name="InventoryModule", screens={InventoryListScreen})
gui_model: GUIModel = GUIModel(name="InventoryManagementApp", package="com.example.inventorymanagement", versionCode="1", versionName="1.0", description="A web application for managing inventory items.", screenCompatibility=True, modules={InventoryModule})
