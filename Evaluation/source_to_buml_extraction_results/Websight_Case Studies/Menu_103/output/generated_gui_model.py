from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
MenuColor = Color(background_color="#FFFFFF", text_color="#000000", border_color="#CCCCCC")
MenuPosition = Position(type=PositionType.Relative)
MenuSize = Size(width="100%", height="auto", padding="10px", font_size="16px", unit_size=UnitSize.PIXELS)
MenuStyling = Styling(size=MenuSize, position=MenuPosition, color=MenuColor)
SidebarColor = Color(background_color="#FFFFFF", text_color="#000000", border_color="#CCCCCC")
SidebarPosition = Position(type=PositionType.Relative)
SidebarSize = Size(width="100%", height="auto", padding="10px", font_size="16px", unit_size=UnitSize.PIXELS)
SidebarStyling = Styling(size=SidebarSize, position=SidebarPosition, color=SidebarColor)
viewComponent: ViewComponent = ViewComponent(name="FashionPageView", description="Display fashion categories and trends")
navigationMenu: Menu = Menu(name="NavigationMenu", description="Main navigation menu", menuItems={MenuItem(label="Home"), MenuItem(label="Products"), MenuItem(label="About"), MenuItem(label="Contact")}, styling=MenuStyling)
leftSidebar: ViewComponent = ViewComponent(name="LeftSidebar", description="Product categories", styling=SidebarStyling)
centerSection: ViewComponent = ViewComponent(name="CenterSection", description="Latest fashion trends", styling=SidebarStyling)
rightSidebar: ViewComponent = ViewComponent(name="RightSidebar", description="Filters and recommendations", styling=SidebarStyling)
FashionScreen: Screen = Screen(name="FashionScreen", description="Fashion page with categories and trends", x_dpi=Property(name="x_dpi", type=StringType), y_dpi=Property(name="y_dpi", type=StringType), screen_size=Property(name="Medium", type=StringType), view_elements={navigationMenu, leftSidebar, centerSection, rightSidebar}, is_main_page=True, layout=ScreenLayout)
FashionModule: Module = Module(name="FashionModule", screens={FashionScreen})
gui_model: GUIModel = GUIModel(name="FashionApp", package="com.example.fashionapp", versionCode=Property(name="versionCode", type=StringType), versionName=Property(name="versionName", type=StringType), description="A web application for exploring fashion trends and categories.", screenCompatibility=True, modules={FashionModule})
