from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
MenuColor = Color(background_color="#FFFFFF", text_color="#343A40", border_color="#CED4DA")
MenuPosition = Position(type=PositionType.Relative)
MenuSize = Size(width="100%", height="auto", padding="10px", unit_size=UnitSize.PIXELS)
MenuStyling = Styling(size=MenuSize, position=MenuPosition, color=MenuColor)
ButtonColor = Color(background_color="#EF4444", text_color="#FFFFFF", border_color="#DC2626")
ButtonPosition = Position(type=PositionType.Relative)
ButtonSize = Size(width="", height="40px", padding="8px", margin="24px", font_size="14px", unit_size=UnitSize.PIXELS)
ButtonStyling = Styling(size=ButtonSize, position=ButtonPosition, color=ButtonColor)
ImagePosition = Position(type=PositionType.Relative)
ImageSize = Size(width="300px", height="200px", unit_size=UnitSize.PIXELS)
ImageStyling = Styling(size=ImageSize, position=ImagePosition, color=None)
viewComponent: ViewComponent = ViewComponent(name="ArchitecturePage", description="Display architecture projects and information")
menuItems = {MenuItem(label="Home"), MenuItem(label="About"), MenuItem(label="Projects"), MenuItem(label="Contact")}
menu: Menu = Menu(name="MainMenu", description="Main navigation menu", menuItems=menuItems, styling=MenuStyling)
sidebar: ViewComponent = ViewComponent(name="Sidebar", description="About Us section", styling=None)
mainContent: ViewComponent = ViewComponent(name="MainContent", description="Our Past Projects", styling=None)
image1: Image = Image(name="ArchitectureImage", styling=ImageStyling, description="")
image2: Image = Image(name="InteriorImage", styling=ImageStyling, description="")
image3: Image = Image(name="ExteriorImage", styling=ImageStyling, description="")
image4: Image = Image(name="UrbanImage", styling=ImageStyling, description="")
formFields = {InputField(name="EmailField", description="Enter your email", type="Email", validationRules="", styling=None)}
contactForm: Form = Form(name="ContactForm", description="Contact form and newsletter sign-up", inputFields=formFields, styling=None)
footer: ViewComponent = ViewComponent(name="Footer", description="Footer with contact form", styling=None)
ArchitectureScreen: Screen = Screen(name="ArchitectureScreen", description="Architecture firm page with projects and contact form", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={menu, sidebar, mainContent, image1, image2, image3, image4, contactForm, footer}, is_main_page=True, layout=ScreenLayout)
ArchitectureModule: Module = Module(name="ArchitectureModule", screens={ArchitectureScreen})
gui_model: GUIModel = GUIModel(name="ArchitectureApp", package="com.example.architectureapp", versionCode="1", versionName="1.0", description="Web application for an architecture firm", screenCompatibility=True, modules={ArchitectureModule})
