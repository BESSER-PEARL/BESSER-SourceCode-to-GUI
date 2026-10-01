from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="horizontal", gap="10px", alignment=JustificationType.Left)
MenuColor = Color(background_color="#FFFFFF", text_color="#000000", border_color="#CCCCCC")
MenuPosition = Position(type=PositionType.Relative)
MenuSize = Size(width="25%", height="100%", padding="16px", font_size="16", unit_size=UnitSize.PERCENT)
MenuStyling = Styling(size=MenuSize, position=MenuPosition, color=MenuColor)
ProductDisplayColor = Color(background_color="#F7FAFC", text_color="#000000", border_color="#CCCCCC")
ProductDisplayPosition = Position(type=PositionType.Relative)
ProductDisplaySize = Size(width="75%", height="100%", padding="16px", font_size="16", unit_size=UnitSize.PERCENT)
ProductDisplayStyling = Styling(size=ProductDisplaySize, position=ProductDisplayPosition, color=ProductDisplayColor)
ProductCardColor = Color(background_color="#FFFFFF", text_color="#000000", border_color="#CCCCCC")
ProductCardPosition = Position(type=PositionType.Relative)
ProductCardSize = Size(width="33%", height="auto", padding="8px", margin="8px", font_size="14", unit_size=UnitSize.PERCENT)
ProductCardStyling = Styling(size=ProductCardSize, position=ProductCardPosition, color=ProductCardColor)
menu: Menu = Menu(name="MainMenu", description="Main navigation menu", menuItems={MenuItem(label="Home"), MenuItem(label="About"), MenuItem(label="Contact")}, styling=MenuStyling)
productDisplay: ViewContainer = ViewContainer(name="ProductDisplay", description="Display area for products", styling=ProductDisplayStyling, view_elements="")
productCard: ViewComponent = ViewComponent(name="ProductCard", description="Card displaying a product", styling=ProductCardStyling)
WebPageScreen: Screen = Screen(name="FashionBrandPage", description="Welcome to our fashion brand page", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Large", is_main_page=True, view_elements={menu, productDisplay, productCard}, layout=ScreenLayout)
FashionModule: Module = Module(name="FashionModule", screens={WebPageScreen})
gui_model: GUIModel = GUIModel(name="FashionApp", package="com.example.fashionapp", versionCode="1", versionName="1.0", description="A web application for a fashion brand.", screenCompatibility=True, modules={FashionModule})
