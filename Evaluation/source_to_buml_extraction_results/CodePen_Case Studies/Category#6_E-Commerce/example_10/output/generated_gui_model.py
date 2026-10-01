from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ImageStyling = Styling(size=Size(width="100%", height="auto", padding="0", margin="0", unit_size=UnitSize.PIXELS), position=Position(type=PositionType.Relative, z_index=0), color=Color(background_color="", border_color="", text_color=""))
ButtonStyling = Styling(size=Size(width="auto", height="40px", padding="8px", margin="24px", font_size="14px", unit_size=UnitSize.PIXELS), position=Position(type=PositionType.Relative, z_index=10), color=Color(background_color="#007BFF", text_color="#FFFFFF", border_color="#0056b3"))
viewComponent = ViewComponent(name="ProductView", description="Display product details with actions")
productImage = Image(name="ProductImage", description="Wood and Metal Necklace", styling=ImageStyling)
addToCartButton = Button(name="AddToCartButton", description="Add product to cart", label="Add to Cart", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add, styling=ButtonStyling)
datasource_product = DataSourceElement(name="ProductDataSource", dataSourceClass=Product, fields=[Product_image, Product_price, Product_quantity, Product_description, Product_dimensions, Product_materials, Product_title])
productInfo = DataList(name="ProductInfo", description="Product details", list_sources={datasource_product}, styling=ImageStyling)
ProductScreen = Screen(name="ProductScreen", description="Product details and actions", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={productImage, addToCartButton, productInfo}, layout=ScreenLayout, is_main_page=True)
MyModule = Module(name="ProductModule", screens={ProductScreen})
gui_model = GUIModel(name="ProductApp", package="com.example.productapp", versionCode="1", versionName="1.0", description="A web application for displaying product details.", screenCompatibility=True, modules={MyModule})
