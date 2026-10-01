from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="transparent", text_color="#FFFFFF", border_color="black")
buttonPosition = Position(type=PositionType.Relative, z_index=10)
buttonSize = Size(width="170px", height="32px", padding="8px", margin="20px", font_size="0.75em", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
viewComponent = ViewComponent(name="ProductView", description="Display product details with actions")
addToCartButton = Button(name="AddToCartButton", description="Add product to cart", label="Add to cart", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add, styling=buttonStyling)
buyNowButton = Button(name="BuyNowButton", description="Buy product now", label="$35.00 Buy now", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Purchase, styling=Styling(size=Size(width="170px", height="32px", margin="20px", font_size="0.75em", unit_size=UnitSize.PIXELS), color=Color(background_color="black", text_color="white", border_color="black")))
productImage = Image(name="ProductImage", description="Product image", styling=Styling(size=Size(width="100%", height="auto", unit_size=UnitSize.PIXELS)))
productTitle = ViewComponent(name="ProductTitle", description="Product title", styling=Styling(size=Size(font_size="4.5em", unit_size=UnitSize.PIXELS), color=Color(text_color="#353997", background_color="", border_color="")))
productDescription = ViewComponent(name="ProductDescription", description="Product description", styling=Styling(size=Size(font_size="16px", unit_size=UnitSize.PIXELS), color=Color(text_color="#333", background_color="", border_color="")))
menuItems = {MenuItem(label="Home"), MenuItem(label="Our brand"), MenuItem(label="Shop"), MenuItem(label="Contact")}
mainMenu = Menu(name="MainMenu", description="Main navigation menu", menuItems=menuItems, styling=Styling(size=Size(width="auto", height="auto", unit_size=UnitSize.PIXELS)))
ProductScreen = Screen(name="ProductScreen", description="Product details screen", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={addToCartButton, buyNowButton, productImage, productTitle, productDescription, mainMenu}, is_main_page=True, layout=ScreenLayout)
ProductModule = Module(name="ProductModule", screens={ProductScreen})
gui_model = GUIModel(name="ProductApp", package="com.example.productapp", versionCode="1", versionName="1.0", description="A web application for viewing and purchasing products.", screenCompatibility=True, modules={ProductModule})
article = Article(title=Article_title, description=Article_description)
