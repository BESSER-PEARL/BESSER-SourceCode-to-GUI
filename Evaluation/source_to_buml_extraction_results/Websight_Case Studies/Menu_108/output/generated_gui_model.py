from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
HeaderImageColor = Color(background_color="#FFFFFF", text_color="", border_color="")
HeaderImagePosition = Position(type=PositionType.Relative, top="", left="", right="", bottom="", alignment="", z_index=0)
HeaderImageSize = Size(width="100%", height="auto", padding="", margin="", font_size="", icon_size="", unit_size=UnitSize.PIXELS)
HeaderImageStyling = Styling(size=HeaderImageSize, position=HeaderImagePosition, color=HeaderImageColor)
ButtonColor = Color(background_color="#F472B6", text_color="#FFFFFF", border_color="#EC4899")
ButtonPosition = Position(type=PositionType.Relative, top="", left="", right="", bottom="", alignment="", z_index=0)
ButtonSize = Size(width="", height="40", padding="8px", margin="24", font_size="14", icon_size="", unit_size=UnitSize.PIXELS)
ButtonStyling = Styling(size=ButtonSize, position=ButtonPosition, color=ButtonColor)
viewComponent: ViewComponent = ViewComponent(name="WebPageView", description="Display a webpage with sections and navigation")
headerImage: Image = Image(name="HeaderImage", description="Header image for the webpage", styling=HeaderImageStyling)
navMenu: Menu = Menu(name="NavigationMenu", description="Navigation links for the webpage", menuItems={MenuItem(label="Popular Products"), MenuItem(label="Custom Printing"), MenuItem(label="Design Services")})
popularProductsButton: Button = Button(name="PopularProductsButton", description="Navigate to popular products", label="Shop Now", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, styling=ButtonStyling)
customPrintingButton: Button = Button(name="CustomPrintingButton", description="Navigate to custom printing", label="Get a Quote", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, styling=ButtonStyling)
designServicesButton: Button = Button(name="DesignServicesButton", description="Navigate to design services", label="Learn More", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, styling=ButtonStyling)
WebPageScreen: Screen = Screen(name="WebPageScreen", description="A webpage with header, main sections, and footer", x_dpi=WebPage_header, y_dpi=WebPage_main, screen_size="Medium", view_elements={headerImage, navMenu, popularProductsButton, customPrintingButton, designServicesButton}, is_main_page=True, layout=ScreenLayout)
WebPageModule: Module = Module(name="WebPageModule", screens={WebPageScreen})
gui_model: GUIModel = GUIModel(name="WebPageApp", package="com.example.webpageapp", versionCode="1", versionName="1.0", description="A web application for displaying a webpage with sections and navigation.", screenCompatibility=True, modules={WebPageModule})
