from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#dc3545", text_color="#FFFFFF", border_color="#bd2130")
ButtonPosition = Position(type=PositionType.Relative, alignment="center", z_index=0)
ButtonSize = Size(width="100%", height="40px", padding="8px", margin="24px", font_size="14px", unit_size=UnitSize.PIXELS)
ButtonStyling = Styling(size=ButtonSize, position=ButtonPosition, color=ButtonColor)
viewComponent = ViewComponent(name="InventoryManagerView", description="Manage inventory, incoming purchases, and outgoing orders")
clearAllButton = Button(name="ClearAllButton", description="Clear all inventory data", label="Clear All", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Delete, styling=ButtonStyling)
currentInventoryTab = Button(name="CurrentInventoryTab", description="View current inventory", label="Current Inventory", buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate)
incomingPurchaseTab = Button(name="IncomingPurchaseTab", description="View incoming purchases", label="Incoming Purchase", buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate)
outgoingOrdersTab = Button(name="OutgoingOrdersTab", description="View outgoing orders", label="Outgoing Orders", buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate)
currentInventoryForm = Form(
    name="CurrentInventoryForm",
    description="Form to add current inventory items",
    inputFields={
        InputField(name="ProductName", description="Name of the product", type=InputFieldType.Text, validationRules="required"),
        InputField(name="ProductBrand", description="Brand of the product", type=InputFieldType.Text, validationRules="required"),
        InputField(name="Quantity", description="Quantity of the product", type=InputFieldType.Number, validationRules="required"),
        InputField(name="ProductPrice", description="Price of the product", type=InputFieldType.Number, validationRules="required"),
    },
)
currentInventoryDataSource = DataSourceElement(name="CurrentInventoryDataSource", dataSourceClass=CurrentInventory, fields={CurrentInventory_productName, CurrentInventory_productBrand, CurrentInventory_quantity, CurrentInventory_productPrice})
currentInventoryList = DataList(name="CurrentInventoryList", list_sources={currentInventoryDataSource}, description="")
incomingPurchaseForm = Form(
    name="IncomingPurchaseForm",
    description="Form to add incoming purchase items",
    inputFields={
        InputField(name="ProductName", description="Name of the product", type=InputFieldType.Text, validationRules="required"),
        InputField(name="ProductBrand", description="Brand of the product", type=InputFieldType.Text, validationRules="required"),
        InputField(name="Quantity", description="Quantity of the product", type=InputFieldType.Number, validationRules="required"),
        InputField(name="ProductPrice", description="Price of the product", type=InputFieldType.Number, validationRules="required"),
    },
)
incomingPurchaseDataSource = DataSourceElement(name="IncomingPurchaseDataSource", dataSourceClass=IncomingPurchase, fields={IncomingPurchase_productName, IncomingPurchase_productBrand, IncomingPurchase_quantity, IncomingPurchase_productPrice})
incomingPurchaseList = DataList(name="IncomingPurchaseList", list_sources={incomingPurchaseDataSource}, description="")
outgoingOrdersForm = Form(
    name="OutgoingOrdersForm",
    description="Form to add outgoing order items",
    inputFields={
        InputField(name="ProductName", description="Name of the product", type=InputFieldType.Text, validationRules="required"),
        InputField(name="ProductBrand", description="Brand of the product", type=InputFieldType.Text, validationRules="required"),
        InputField(name="Quantity", description="Quantity of the product", type=InputFieldType.Number, validationRules="required"),
        InputField(name="ProductPrice", description="Price of the product", type=InputFieldType.Number, validationRules="required"),
    },
)
outgoingOrdersDataSource = DataSourceElement(name="OutgoingOrdersDataSource", dataSourceClass=OutgoingOrders, fields={OutgoingOrders_productName, OutgoingOrders_productBrand, OutgoingOrders_quantity, OutgoingOrders_productPrice})
outgoingOrdersList = DataList(name="OutgoingOrdersList", list_sources={outgoingOrdersDataSource}, description="")
InventoryManagementScreen = Screen(name="InventoryManagementScreen", description="Manage inventory, incoming purchases, and outgoing orders", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", is_main_page=True, view_elements={clearAllButton, currentInventoryTab, incomingPurchaseTab, outgoingOrdersTab, currentInventoryForm, currentInventoryList, incomingPurchaseForm, incomingPurchaseList, outgoingOrdersForm, outgoingOrdersList}, layout=ScreenLayout)
InventoryManagementModule = Module(name="InventoryManagementModule", screens={InventoryManagementScreen})
gui_model = GUIModel(name="InventoryManagementApp", package="com.example.inventorymanagement", versionCode="1", versionName="1.0", description="A comprehensive web application for managing inventory.", screenCompatibility=True, modules={InventoryManagementModule})
