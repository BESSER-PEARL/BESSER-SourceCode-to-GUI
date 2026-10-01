from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

headerColor = Color(background_color="#FFFFFF", text_color="", border_color="")
headerPosition = Position(type=PositionType.Relative, alignment="center", z_index=0)
headerSize = Size(width="100%", height="64px", padding="16px", unit_size=UnitSize.PIXELS)
headerStyling = Styling(size=headerSize, position=headerPosition, color=headerColor)
navColor = Color(background_color="#EC4899", text_color="#FFFFFF", border_color="")
navPosition = Position(type=PositionType.Relative, alignment="center", z_index=0)
navSize = Size(width="100%", height="64px", padding="16px", unit_size=UnitSize.PIXELS)
navStyling = Styling(size=navSize, position=navPosition, color=navColor)
sectionColor = Color(background_color="", text_color="#1F2937", border_color="")
sectionPosition = Position(type=PositionType.Relative, z_index=0)
sectionSize = Size(width="100%", height="auto", padding="16px", margin="32px 0", unit_size=UnitSize.PIXELS)
sectionStyling = Styling(size=sectionSize, position=sectionPosition, color=sectionColor)
logoImage = Image(name=Header_logoSrc.name, description=Header_logoAlt.name, styling=headerStyling)
admissionsImage = Image(name=MainContent_sectionImageSrc.name, description=MainContent_sectionImageAlt.name, styling=sectionStyling)
academicsImage = Image(name=MainContent_sectionImageSrc.name, description=MainContent_sectionImageAlt.name, styling=sectionStyling)
studentLifeImage = Image(name=MainContent_sectionImageSrc.name, description=MainContent_sectionImageAlt.name, styling=sectionStyling)
navMenuItems = {MenuItem(label=Navigation_linkText.name), MenuItem(label=Navigation_linkText.name), MenuItem(label=Navigation_linkText.name)}
navMenu = Menu(name=Navigation_linkHref.name, description=Navigation_linkText.name, menuItems=navMenuItems, styling=navStyling)
mainScreen = Screen(name=WebPage_header.name, description=MainContent_sectionDescription.name, x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={logoImage, navMenu, admissionsImage, academicsImage, studentLifeImage}, is_main_page=True, layout=Layout(type=LayoutType.Flex, orientation="vertical", gap="32px", alignment=JustificationType.Center))
mainModule = Module(name="MainModule", screens={mainScreen})
gui_model = GUIModel(name="InstitutionApp", package="com.example.institutionapp", versionCode="1", versionName="1.0", description="An application showcasing the institution's offerings.", screenCompatibility=True, modules={mainModule})
