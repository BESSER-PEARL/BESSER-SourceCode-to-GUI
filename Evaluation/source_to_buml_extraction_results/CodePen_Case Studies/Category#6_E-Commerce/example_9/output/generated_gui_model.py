from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#007BFF", text_color="#FFFFFF", border_color="#0056b3")
buttonPosition = Position(type=PositionType.Relative, z_index=10)
buttonSize = Size(height="40px", padding="8px", margin="24px", font_size="14px", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
MenuColor = Color(background_color="#FFFFFF", text_color="#343A40", border_color="#CED4DA")
MenuPosition = Position(type=PositionType.Relative, top="200px", left="20px", z_index=0)
menuSize = Size(width="100%", padding="10px", unit_size=UnitSize.PIXELS)
MenuStyling = Styling(size=menuSize, position=MenuPosition, color=MenuColor)
ImagePosition = Position(type=PositionType.Relative, z_index=0)
imageSize = Size(width="100%", height="auto", unit_size=UnitSize.PIXELS)
ImageStyling = Styling(size=imageSize, position=ImagePosition)
viewComponent = ViewComponent(name="ECommerceView", description="E-Commerce Website Interface")
searchBox = InputField(name="SearchBox", description="Search input field", type="Text", styling=buttonStyling)
cartMenuItem = MenuItem(label="Cart")
signUpMenuItem = MenuItem(label="Sign Up")
loginMenuItem = MenuItem(label="Login")
menuBar = Menu(name="MenuBar", description="Navigation menu", menuItems={cartMenuItem, signUpMenuItem, loginMenuItem}, styling=MenuStyling)
categories = ["On Sale", "Mobiles", "Computers", "Books", "Fitness", "Baby Care", "Magazines", "Auto Accessories", "Movies & Music", "Video & Games", "Home & Kitchen", "Furniture", "Grocery"]
sideMenuItems = {MenuItem(label=category) for category in categories}
sideMenu = Menu(name="SideMenu", description="Category menu", menuItems=sideMenuItems, styling=MenuStyling)
sliderImage1 = Image(name="SliderImage1", styling=ImageStyling, description="")
sliderImage2 = Image(name="SliderImage2", styling=ImageStyling, description="")
slider = ViewContainer(name="Slider", description="Image slider", view_elements={sliderImage1, sliderImage2}, layout=ScreenLayout)
ECommerceScreen = Screen(name="ECommerceScreen", description="Main screen of the E-Commerce website", x_dpi="160", y_dpi="160", screen_size="Large", view_elements={searchBox, menuBar, sideMenu, slider}, is_main_page=True, layout=ScreenLayout)
ECommerceModule = Module(name="ECommerceModule", screens={ECommerceScreen})
gui_model = GUIModel(name="ECommerceApp", package="com.example.ecommerce", versionCode="1", versionName="1.0", description="An E-Commerce web application interface.", screenCompatibility=True, modules={ECommerceModule})
