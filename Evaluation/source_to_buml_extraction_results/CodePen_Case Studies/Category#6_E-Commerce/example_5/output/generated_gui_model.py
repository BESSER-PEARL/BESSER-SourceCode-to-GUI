from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="horizontal", gap="10px", alignment=JustificationType.Center)
ImagePosition = Position(type=PositionType.Relative, z_index=0)
ImageSize = Size(width="100%", height="auto", padding="0", margin="0", unit_size=UnitSize.PERCENT)
ImageColor = Color(background_color="", text_color="", border_color="")
ImageStyling = Styling(size=ImageSize, position=ImagePosition, color=ImageColor)
ButtonColor = Color(background_color="#007BFF", text_color="#FFFFFF", border_color="#0056b3")
ButtonPosition = Position(type=PositionType.Relative, z_index=10)
ButtonSize = Size(width="100%", height="40px", padding="8px", margin="24px", font_size="14px", unit_size=UnitSize.PIXELS)
ButtonStyling = Styling(size=ButtonSize, position=ButtonPosition, color=ButtonColor)
viewComponent = ViewComponent(name="ProductView", description="Display product details with purchase option")
productImage = Image(name="ProductImage", description="Product image", styling=ImageStyling)
purchaseButton = Button(name="PurchaseButton", description="Proceed to checkout", label="Proceed to checkout", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, styling=ButtonStyling)
datasource_product = DataSourceElement(name="ProductDataSource", dataSourceClass=Right, fields=[Right_title, Right_price, Right_description])
productList = DataList(name="ProductList", description="List of product features", list_sources={datasource_product}, styling=ImageStyling)
ProductScreen = Screen(name="ProductScreen", description="Product details and purchase option", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", is_main_page=True, view_elements={productImage, purchaseButton, productList}, layout=ScreenLayout)
ProductModule = Module(name="ProductModule", screens={ProductScreen})
gui_model = GUIModel(name="ProductApp", package="com.example.productapp", versionCode="1", versionName="1.0", description="A web application for displaying product details and purchasing options.", screenCompatibility=True, modules={ProductModule})
