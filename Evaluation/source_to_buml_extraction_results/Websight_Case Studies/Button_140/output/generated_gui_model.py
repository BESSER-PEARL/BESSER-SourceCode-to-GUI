from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#FFFFFF", text_color="#1F2937", border_color="#1F2937")
buttonPosition = Position(type=PositionType.Relative)
buttonSize = Size(width="auto", height="40px", padding="8px", margin="24px", font_size="14px", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
viewComponent: ViewComponent = ViewComponent(name="RealEstateView", description="Display real estate options")
homeMenuItem = MenuItem(label="Home")
aboutMenuItem = MenuItem(label="About")
contactMenuItem = MenuItem(label="Contact")
navigationMenu: Menu = Menu(name="NavigationMenu", description="Main navigation menu", menuItems={homeMenuItem, aboutMenuItem, contactMenuItem})
getStartedButton: Button = Button(name="GetStartedButton", description="Start finding your dream home", label="Get Started", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, styling=buttonStyling)
houseImage: Image = Image(name="HouseImage", description="")
apartmentImage: Image = Image(name="ApartmentImage", description="")
section1: ViewContainer = ViewContainer(name="Section1", description="Introduction section", view_elements={getStartedButton, houseImage})
section2: ViewContainer = ViewContainer(name="Section2", description="Details section", view_elements={getStartedButton, apartmentImage})
RealEstateScreen: Screen = Screen(name="RealEstateScreen", description="Explore real estate options", x_dpi=Property(name="x_dpi", type=IntegerType), y_dpi=Property(name="y_dpi", type=IntegerType), screen_size=Property(name="screen_size", type=StringType), view_elements={navigationMenu, section1, section2}, is_main_page=True, layout=ScreenLayout)
RealEstateModule: Module = Module(name="RealEstateModule", screens={RealEstateScreen})
gui_model: GUIModel = GUIModel(name="RealEstateApp", package="com.example.realestate", versionCode=Property(name="versionCode", type=StringType), versionName=Property(name="versionName", type=StringType), description="A web application for exploring real estate options.", screenCompatibility=True, modules={RealEstateModule})
