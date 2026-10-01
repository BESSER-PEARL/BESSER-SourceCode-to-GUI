from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#6B7280", text_color="#FFFFFF", border_color="#4B5563")
buttonPosition = Position(type=PositionType.Relative, z_index=10)
buttonSize = Size(width="auto", height="40px", padding="8px", margin="0", font_size="16px", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
viewComponent = ViewComponent(name="ArchitectureFirmView", description="Architecture Firm Web Page")
homeMenuItem = MenuItem(label="Home")
aboutMenuItem = MenuItem(label="About")
contactMenuItem = MenuItem(label="Contact")
navMenu = Menu(name="NavBar", description="Navigation Bar", menuItems={homeMenuItem, aboutMenuItem, contactMenuItem})
headerTitle = Header(name="Header", description="Main Header", title=Header_title, subtitle=Header_subtitle)
learnMoreButton = Button(name="LearnMoreButton", description="Learn More about the firm", label="Learn More", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, styling=buttonStyling)
servicesSection = Section(name="ServicesSection", description="Our Services", title=Section_title)
architectureImage = Image(name="ArchitectureImage", description="")
footer = Footer(name="Footer", description="Footer", copyright=Footer_copyright)
ArchitectureFirmScreen = Screen(name="ArchitectureFirmScreen", description="Architecture Firm Web Page", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={navMenu, headerTitle, learnMoreButton, servicesSection, architectureImage, footer}, is_main_page=True, layout=ScreenLayout)
ArchitectureModule = Module(name="ArchitectureModule", screens={ArchitectureFirmScreen})
gui_model = GUIModel(name="ArchitectureFirmApp", package="com.example.architecturefirm", versionCode="1", versionName="1.0", description="Web application for an architecture firm.", screenCompatibility=True, modules={ArchitectureModule})
