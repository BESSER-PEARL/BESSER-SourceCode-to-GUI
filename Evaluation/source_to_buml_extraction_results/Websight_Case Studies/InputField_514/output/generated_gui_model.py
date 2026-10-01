from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ImageColor = Color(background_color="", text_color="", border_color="")
ImagePosition = Position(type=PositionType.Relative, top="", left="", right="", bottom="", alignment="center", z_index=0)
ImageSize = Size(width="100%", height="96", padding="", margin="", font_size="", icon_size="", unit_size=UnitSize.PERCENT)
ImageStyling = Styling(size=ImageSize, position=ImagePosition, color=ImageColor)
NavColor = Color(background_color="#FFFFFF", text_color="#343A40", border_color="#CED4DA")
NavPosition = Position(type=PositionType.Relative, top="", left="", right="", bottom="", alignment="", z_index=0)
NavSize = Size(width="100%", height="auto", padding="6px", margin="", font_size="", icon_size="", unit_size=UnitSize.PERCENT)
NavStyling = Styling(size=NavSize, position=NavPosition, color=NavColor)
SearchBarColor = Color(background_color="#FFFFFF", text_color="#343A40", border_color="#CED4DA")
SearchBarPosition = Position(type=PositionType.Relative, top="", left="", right="", bottom="", alignment="", z_index=0)
SearchBarSize = Size(width="100%", height="auto", padding="4px", margin="", font_size="", icon_size="", unit_size=UnitSize.PERCENT)
SearchBarStyling = Styling(size=SearchBarSize, position=SearchBarPosition, color=SearchBarColor)
realEstateImage = Image(name="RealEstateImage", description="Real Estate Image", styling=ImageStyling)
navigationMenu = Menu(name="NavigationMenu", description="Main navigation menu", styling=NavStyling, menuItems="")
searchBar = InputField(name="SearchBar", description="Search for properties", type="Text", validationRules="", styling=SearchBarStyling)
RealEstateScreen = Screen(name="RealEstatePage", description="Welcome to Our Real Estate Agency", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Large", view_elements={realEstateImage, navigationMenu, searchBar}, is_main_page=True, layout=ScreenLayout)
RealEstateModule = Module(name="RealEstateModule", screens={RealEstateScreen})
gui_model = GUIModel(name="RealEstateApp", package="com.example.realestate", versionCode="1", versionName="1.0", description="A web application for real estate listings.", screenCompatibility=True, modules={RealEstateModule})
