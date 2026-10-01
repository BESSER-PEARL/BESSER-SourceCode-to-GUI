from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

navColor = Color(background_color="#0b121b", text_color="white", border_color="transparent")
navPosition = Position(type=PositionType.Relative)
navSize = Size(width="280px", height="auto", padding="0", font_size="12px", unit_size=UnitSize.PIXELS)
navStyling = Styling(size=navSize, position=navPosition, color=navColor)
headerColor = Color(background_color="#ebecee", text_color="#101620", border_color="transparent")
headerPosition = Position(type=PositionType.Relative)
headerSize = Size(width="100%", height="auto", padding="3rem", font_size="24px", unit_size=UnitSize.PIXELS)
headerStyling = Styling(size=headerSize, position=headerPosition, color=headerColor)
contentColor = Color(background_color="#e5e5e9", text_color="#000000", border_color="transparent")
contentPosition = Position(type=PositionType.Relative)
contentSize = Size(width="100%", height="auto", padding="3rem", font_size="16px", unit_size=UnitSize.PIXELS)
contentStyling = Styling(size=contentSize, position=contentPosition, color=contentColor)
navMenu = Menu(name="NavMenu", description="Navigation menu", menuItems={MenuItem(label="Deals"), MenuItem(label="Activities"), MenuItem(label="Asset Libraries"), MenuItem(label="Funds"), MenuItem(label="Investors"), MenuItem(label="Reports")}, styling=navStyling)
header = ViewComponent(name="Header", description="Page header", styling=headerStyling)
breadcrumbs = ViewComponent(name="Breadcrumbs", description="Breadcrumb navigation", styling=headerStyling)
navTabs = ViewComponent(name="NavTabs", description="Navigation tabs", styling=headerStyling)
contentColumns = ViewComponent(name="ContentColumns", description="Content columns", styling=contentStyling)
mainScreen = Screen(name="MainScreen", description="Main application screen", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Large", view_elements={navMenu, header, breadcrumbs, navTabs, contentColumns}, is_main_page=True)
appModule = Module(name="AppModule", screens={mainScreen})
guiModel = GUIModel(name="AppModel", package="com.example.app", versionCode="1", versionName="1.0", description="An application for managing deals and reports.", screenCompatibility=True, modules={appModule})
navTabs_dealsCount = NavTabs_dealsCount
navTabs_libraryCount = NavTabs_libraryCount
