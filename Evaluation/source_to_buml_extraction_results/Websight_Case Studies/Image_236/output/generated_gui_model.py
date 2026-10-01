from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *
# GUI model definition

# Styling definitions

# Screen layout
ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)

# Header styling
HeaderColor = Color(background_color="#FFFFFF", text_color="#343A40", border_color="#E5E7EB")
HeaderPosition = Position(type=PositionType.Relative, top="0", left="0", right="0", bottom="", alignment="center", z_index=10)
HeaderSize = Size(width="100%", height="auto", padding="10px", margin="0", font_size="16", icon_size="", unit_size=UnitSize.PIXELS)
HeaderStyling = Styling(size=HeaderSize, position=HeaderPosition, color=HeaderColor)

# Button styling
ButtonColor = Color(background_color="#FFFFFF", text_color="#1F2937", border_color="#D1D5DB")
ButtonPosition = Position(type=PositionType.Inline, alignment="center", z_index=0)
ButtonSize = Size(width="auto", height="40", padding="8px", margin="6", font_size="14", icon_size="", unit_size=UnitSize.PIXELS)
ButtonStyling = Styling(size=ButtonSize, position=ButtonPosition, color=ButtonColor)

# Main content styling
MainContentColor = Color(background_color="#F3F4F6", text_color="#1F2937", border_color="#E5E7EB")
MainContentPosition = Position(type=PositionType.Relative, top="0", left="0", right="0", bottom="", alignment="center", z_index=0)
MainContentSize = Size(width="100%", height="auto", padding="20px", margin="0", font_size="18", icon_size="", unit_size=UnitSize.PIXELS)
MainContentStyling = Styling(size=MainContentSize, position=MainContentPosition, color=MainContentColor)

# Image styling
ImagePosition = Position(type=PositionType.Relative, top="", left="", right="", bottom="", alignment="center", z_index=0)
ImageSize = Size(width="100%", height="auto", padding="0", margin="0", font_size="", icon_size="", unit_size=UnitSize.PIXELS)
ImageStyling = Styling(size=ImageSize, position=ImagePosition, color=None)

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="FoodTruckView", description="Display food truck information and menu")

# Header elements
headerLogo: Image = Image(name=WebPage_headerLogo.name, styling=ImageStyling)
headerMenuButton: Button = Button(name=WebPage_headerMenu.name, description="Navigate to Menu", label="Menu", buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate, styling=ButtonStyling)
headerOrderNowButton: Button = Button(name=WebPage_headerOrderNow.name, description="Navigate to Order Now", label="Order Now", buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate, styling=ButtonStyling)
headerBookATruckButton: Button = Button(name=WebPage_headerBookATruck.name, description="Navigate to Book a Truck", label="Book a Truck", buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate, styling=ButtonStyling)

# Main content elements
mainTitle: ViewComponent = ViewComponent(name=WebPage_mainTitle.name, description="Welcome to Our Food Truck", styling=MainContentStyling)
mainDescription: ViewComponent = ViewComponent(name=WebPage_mainDescription.name, description="We offer a wide variety of delicious food items made from the freshest ingredients.", styling=MainContentStyling)

# Food item elements
foodItemImage: Image = Image(name=WebPage_foodItemImage.name, styling=ImageStyling)
foodItemName: ViewComponent = ViewComponent(name=WebPage_foodItemName.name, description="Burger", styling=MainContentStyling)
foodItemDescription: ViewComponent = ViewComponent(name=WebPage_foodItemDescription.name, description="A juicy, delicious burger made with the finest beef.", styling=MainContentStyling)
foodItemPrice: ViewComponent = ViewComponent(name=WebPage_foodItemPrice.name, description="$10", styling=MainContentStyling)

# Footer elements
footerCopyright: ViewComponent = ViewComponent(name=WebPage_footerCopyright.name, description="� 2022 Food Truck Business. All rights reserved.", styling=MainContentStyling)

# Screen definition
FoodTruckScreen: Screen = Screen(name="FoodTruckScreen", description="Food truck main page",
                                 x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium",
                                 view_elements={headerLogo, headerMenuButton, headerOrderNowButton, headerBookATruckButton,
                                                mainTitle, mainDescription, foodItemImage, foodItemName, foodItemDescription,
                                                foodItemPrice, footerCopyright},
                                 is_main_page=True, layout=ScreenLayout)

# Module definition
FoodTruckModule: Module = Module(name="FoodTruckModule", screens={FoodTruckScreen})

# Application definition
gui_model: GUIModel = GUIModel(name="FoodTruckApp", package="com.example.foodtruck", versionCode="1",
                               versionName="1.0", description="A web application for a food truck business.",
                               screenCompatibility=True, modules={FoodTruckModule})

# Class and attributes
# This page is related to the "WebPage" class in the structural model.
# Attributes: headerLogo, headerMenu, headerOrderNow, headerBookATruck, mainTitle, mainDescription, foodItemName, foodItemDescription, foodItemPrice, foodItemImage, footerCopyright
