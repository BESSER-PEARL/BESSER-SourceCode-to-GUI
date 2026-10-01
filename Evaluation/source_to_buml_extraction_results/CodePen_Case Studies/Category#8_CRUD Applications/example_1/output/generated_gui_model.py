from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#007BFF", text_color="#FFFFFF", border_color="#0056b3")
buttonPosition = Position(type=PositionType.Relative, z_index=10)
buttonSize = Size(height="40px", padding="8px", font_size="14px", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
viewComponent = ViewComponent(name="ProductListView", description="Display a list of products with actions")
addProductButton = Button(name="AddProductButton", description="Add a new product", label="Add product", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add, styling=buttonStyling)
editProductButton = Button(name="EditProductButton", description="Edit a product", label="Edit", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Edit, styling=buttonStyling)
deleteProductButton = Button(name="DeleteProductButton", description="Delete a product", label="Delete", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Delete, styling=buttonStyling)
datasource_product = DataSourceElement(name="ProductDataSource", dataSourceClass=Product, fields=[Product_name, Product_description, Product_price])
productList = DataList(name="ProductList", description="A list of products", list_sources={datasource_product}, styling=Styling(size=Size(width="100%", unit_size=UnitSize.PERCENT)))
ProductScreen = Screen(name="ProductScreen", description="Manage products", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", is_main_page=True, view_elements={addProductButton, editProductButton, deleteProductButton, productList}, layout=ScreenLayout)
ProductModule = Module(name="ProductModule", screens={ProductScreen})
gui_model = GUIModel(name="ProductManagementApp", package="com.example.productmanagement", versionCode="1", versionName="1.0", description="A web application for managing products.", screenCompatibility=True, modules={ProductModule})
