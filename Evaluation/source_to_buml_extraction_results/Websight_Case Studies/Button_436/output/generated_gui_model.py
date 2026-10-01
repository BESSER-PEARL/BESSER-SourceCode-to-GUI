from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#FFFFFF", text_color="#006400", border_color="#228B22")
buttonPosition = Position(type=PositionType.Relative, top="", left="", right="", bottom="", alignment="", z_index=0)
buttonSize = Size(width="", height="40", padding="8px", margin="24", font_size="14", icon_size="", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
viewComponent = ViewComponent(name="GreenEnergyView", description="Display information about green energy solutions")
navMenu = Menu(name="NavigationMenu", description="Main navigation menu", menuItems={MenuItem(label="Home"), MenuItem(label="About"), MenuItem(label="Services"), MenuItem(label="Contact")}, styling=Styling(position=Position(type=PositionType.Absolute, top="0", left="", right="", bottom="", alignment="Center", z_index=1), color=Color(background_color="", text_color="#FFFFFF", border_color="")))
mainHeading = ViewComponent(name="MainHeading", description="Main heading of the page", styling=Styling(size=Size(width="", height="", padding="", margin="", font_size="32", icon_size="", unit_size=UnitSize.PIXELS), position=Position(type=PositionType.Relative, top="", left="", right="", bottom="", alignment="", z_index=0), color=Color(background_color="", text_color="#000000", border_color="")))
subHeading = ViewComponent(name="SubHeading", description="Subheading of the page", styling=Styling(size=Size(width="", height="", padding="", margin="", font_size="20", icon_size="", unit_size=UnitSize.PIXELS), position=Position(type=PositionType.Relative, top="", left="", right="", bottom="", alignment="", z_index=0), color=Color(background_color="", text_color="#000000", border_color="")))
learnMoreButton = Button(name="LearnMoreButton", description="Button to learn more about green energy solutions", label="Learn More", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, styling=Styling(size=Size(width="", height="", padding="8px", margin="16px", font_size="14", icon_size="", unit_size=UnitSize.PIXELS), color=Color(background_color="#FFFFFF", text_color="#006400", border_color="#228B22")))
footer = ViewComponent(name="Footer", description="Footer with contact information", styling=Styling(size=Size(width="", height="", padding="", margin="", font_size="14", icon_size="", unit_size=UnitSize.PIXELS), position=Position(type=PositionType.Relative, top="", left="", right="", bottom="", alignment="", z_index=0), color=Color(background_color="#006400", text_color="#FFFFFF", border_color="")))
GreenEnergyScreen = Screen(name="GreenEnergyScreen", description="Screen displaying green energy solutions", x_dpi=WebPage_title, y_dpi=WebPage_description, screen_size="Medium", view_elements={navMenu, mainHeading, subHeading, learnMoreButton, footer}, is_main_page=True, layout=ScreenLayout)
GreenEnergyModule = Module(name="GreenEnergyModule", screens={GreenEnergyScreen})
gui_model = GUIModel(name="GreenEnergyApp", package="com.example.greenenergy", versionCode=WebPage_phone, versionName=WebPage_email, description=WebPage_description, screenCompatibility=True, modules={GreenEnergyModule})
