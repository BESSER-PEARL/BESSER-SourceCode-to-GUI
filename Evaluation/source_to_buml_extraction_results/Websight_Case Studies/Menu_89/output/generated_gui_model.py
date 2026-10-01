from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="horizontal", gap="0", alignment=JustificationType.Left)
MenuColor = Color(background_color="#E5E7EB", text_color="#000000", border_color="#E5E7EB")
MenuPosition = Position(type=PositionType.Relative)
MenuSize = Size(width="25%", height="100%", padding="16px", font_size="16", unit_size=UnitSize.PERCENT)
MenuStyling = Styling(size=MenuSize, position=MenuPosition, color=MenuColor)
ContentPosition = Position(type=PositionType.Relative)
ContentSize = Size(width="75%", height="100%", padding="16px", font_size="16", unit_size=UnitSize.PERCENT)
ContentStyling = Styling(size=ContentSize, position=ContentPosition, color=None)
ButtonColor = Color(background_color="#10B981", text_color="#FFFFFF", border_color="#10B981")
ButtonPosition = Position(type=PositionType.Relative)
ButtonSize = Size(height="40", padding="8px", margin="8px", font_size="14", unit_size=UnitSize.PIXELS)
ButtonStyling = Styling(size=ButtonSize, position=ButtonPosition, color=ButtonColor)
TransparentButtonColor = Color(background_color="transparent", text_color="#10B981", border_color="#10B981")
TransparentButtonStyling = Styling(size=ButtonSize, position=ButtonPosition, color=TransparentButtonColor)
viewComponent: ViewComponent = ViewComponent(name="FoodMenuView", description="Display a menu with categories and filter options")
menuItems = {MenuItem(label=Menu_pizza.name), MenuItem(label=Menu_burger.name), MenuItem(label=Menu_sushi.name)}
menuCategories = {MenuItem(label=Categories_vegetarian.name), MenuItem(label=Categories_nonVegetarian.name)}
menuFilters = {MenuItem(label=FilterOptions_price.name), MenuItem(label=FilterOptions_rating.name)}
menu: Menu = Menu(name="MainMenu", description="Main menu with categories and filters", menuItems=menuItems.union(menuCategories).union(menuFilters), styling=MenuStyling)
popularDishImage: Image = Image(name="PopularDishImage", description=PopularDish_description.name, styling=ContentStyling)
orderButton: Button = Button(name="OrderNowButton", description="Order the popular dish", label="Order Now", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add, styling=ButtonStyling)
addToCartButton: Button = Button(name="AddToCartButton", description="Add the popular dish to cart", label="Add to Cart", buttonType=ButtonType.TextButton, actionType=ButtonActionType.Add, styling=TransparentButtonStyling)
FoodMenuScreen: Screen = Screen(name="FoodMenuScreen", description="Screen displaying the food menu and popular dish", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Large", is_main_page=True, view_elements={menu, popularDishImage, orderButton, addToCartButton}, layout=ScreenLayout)
FoodMenuModule: Module = Module(name="FoodMenuModule", screens={FoodMenuScreen})
gui_model: GUIModel = GUIModel(name="FoodOrderingApp", package="com.example.foodordering", versionCode="1", versionName="1.0", description="A web application for ordering food online.", screenCompatibility=True, modules={FoodMenuModule})
