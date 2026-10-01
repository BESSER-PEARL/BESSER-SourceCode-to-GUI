from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="0", alignment=JustificationType.Center)
HeaderColor = Color(background_color="#6B46C1", text_color="#FFFFFF", border_color="")
HeaderPosition = Position(type=PositionType.Relative, alignment="center")
HeaderSize = Size(width="100%", height="auto", padding="16px", font_size="24", unit_size=UnitSize.PIXELS)
HeaderStyling = Styling(size=HeaderSize, position=HeaderPosition, color=HeaderColor)
NavColor = Color(background_color="#D6BCFA", text_color="#FFFFFF", border_color="")
NavPosition = Position(type=PositionType.Relative, alignment="center")
NavSize = Size(width="100%", height="auto", padding="16px", unit_size=UnitSize.PIXELS)
NavStyling = Styling(size=NavSize, position=NavPosition, color=NavColor)
AsideColor = Color(background_color="#E9D8FD", text_color="#FFFFFF", border_color="")
AsidePosition = Position(type=PositionType.Relative, alignment="left")
AsideSize = Size(width="25%", height="auto", padding="16px", unit_size=UnitSize.PIXELS)
AsideStyling = Styling(size=AsideSize, position=AsidePosition, color=AsideColor)
MainPosition = Position(type=PositionType.Relative, alignment="left")
MainSize = Size(width="75%", height="auto", padding="16px", unit_size=UnitSize.PIXELS)
MainStyling = Styling(size=MainSize, position=MainPosition)
header: ViewComponent = ViewComponent(name="Header", description="Law Firm Header", styling=HeaderStyling)
navMenuItems = {MenuItem(label="Home"), MenuItem(label="About"), MenuItem(label="Services"), MenuItem(label="Contact")}
navigation: Menu = Menu(name="Navigation", description="Main Navigation", menuItems=navMenuItems, styling=NavStyling)
aside: ViewComponent = ViewComponent(name="Aside", description="Contact Information and Services", styling=AsideStyling)
main: ViewComponent = ViewComponent(name="Main", description="About Us Section", styling=MainStyling)
LawFirmPageScreen: Screen = Screen(name="LawFirmPage", description="Law Firm Information Page", x_dpi=Property(name="x_dpi", type=IntegerType), y_dpi=Property(name="y_dpi", type=IntegerType), screen_size=Property(name="screen_size", type=StringType), view_elements={header, navigation, aside, main}, is_main_page=True, layout=ScreenLayout)
LawFirmModule: Module = Module(name="LawFirmModule", screens={LawFirmPageScreen})
gui_model: GUIModel = GUIModel(name="LawFirmApp", package="com.example.lawfirm", versionCode=Property(name="versionCode", type=StringType), versionName=Property(name="versionName", type=StringType), description="A web application for a law firm.", screenCompatibility=True, modules={LawFirmModule})
