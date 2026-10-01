from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *
from gui_framework import Layout, LayoutType, JustificationType, Color, Position, PositionType, Size, UnitSize, Styling, ViewComponent, MenuItem, Menu, InputField, InputFieldType, Image, Screen, Module, GUIModel

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#007BFF", text_color="#FFFFFF", border_color="#0056b3")
buttonPosition = Position(type=PositionType.Relative, z_index=10)
buttonSize = Size(height="40px", padding="8px", margin="24px", font_size="14px", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
viewComponent = ViewComponent(name="ChumhumView", description="Display Chumhum elements")
headerMenuItems = [MenuItem(label="Publishing"), MenuItem(label="Gallery"), MenuItem(label="Foto"), MenuItem(label="Email"), MenuItem(label="Videos"), MenuItem(label="Buy"), MenuItem(label="FAQ")]
headerMenu = Menu(name="HeaderMenu", description="Main navigation menu", menuItems=set(headerMenuItems))
searchInputField = InputField(name="Main_search", description="Search input", type=InputFieldType.Text, styling=Styling(size=Size(width="610px", height="25px", unit_size=UnitSize.PIXELS)))
logoImage = Image(name="Main_logo", description="")
footerMenuItems = [MenuItem(label="Chumhum agency"), MenuItem(label="Chumhum apps"), MenuItem(label="Chumhum work group"), MenuItem(label="Chumhum Photos")]
footerMenu = Menu(name="FooterMenu", description="Footer navigation menu", menuItems=set(footerMenuItems))
footerCopyright = ViewComponent(name="Footer_copyright", description="Copyright information")
MainScreen = Screen(name="ChumhumMainScreen", description="Main screen for Chumhum", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={headerMenu, searchInputField, logoImage, footerMenu, footerCopyright}, is_main_page=True, layout=ScreenLayout)
ChumhumModule = Module(name="ChumhumModule", screens={MainScreen})
gui_model = GUIModel(name="ChumhumApp", package="com.example.chumhum", versionCode="1", versionName="1.0", description="Chumhum web application", screenCompatibility=True, modules={ChumhumModule})
