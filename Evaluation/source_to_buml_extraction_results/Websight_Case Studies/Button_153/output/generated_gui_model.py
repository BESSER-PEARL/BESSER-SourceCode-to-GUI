from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="horizontal", gap="0", alignment=JustificationType.Center)
TextColor = Color(background_color="", text_color="#FFFFFF", border_color="")
TextPosition = Position(type=PositionType.Relative, top="", left="", right="", bottom="", alignment="", z_index=0)
TextSize = Size(width="", height="", padding="0", margin="0", font_size="16", icon_size="", unit_size=UnitSize.PIXELS)
TextStyling = Styling(size=TextSize, position=TextPosition, color=TextColor)
ButtonColor = Color(background_color="#6B46C1", text_color="#FFFFFF", border_color="#553C9A")
ButtonPosition = Position(type=PositionType.Relative, top="", left="", right="", bottom="", alignment="", z_index=0)
ButtonSize = Size(width="", height="40", padding="8px", margin="0", font_size="14", icon_size="", unit_size=UnitSize.PIXELS)
ButtonStyling = Styling(size=ButtonSize, position=ButtonPosition, color=ButtonColor)
ImagePosition = Position(type=PositionType.Relative, top="", left="", right="", bottom="", alignment="", z_index=0)
ImageSize = Size(width="40", height="40", padding="0", margin="0", font_size="", icon_size="", unit_size=UnitSize.PIXELS)
ImageStyling = Styling(size=ImageSize, position=ImagePosition, color=TextColor)
welcomeText = ViewComponent(name="WelcomeText", description=WebPage_description, styling=TextStyling)
servicesText = ViewComponent(name="ServicesText", description=Service_description, styling=TextStyling)
learnMoreButton = Button(name="LearnMoreButton", description="Learn more about the company", label="Learn More", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, styling=ButtonStyling)
technologyImage = Image(name="TechnologyImage", styling=ImageStyling, description="")
innovationImage = Image(name="InnovationImage", styling=ImageStyling, description="")
HomeScreen = Screen(name="HomeScreen", description=WebPage_description, x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={welcomeText, servicesText, learnMoreButton, technologyImage, innovationImage}, is_main_page=True, layout=ScreenLayout)
TechModule = Module(name="TechModule", screens={HomeScreen})
gui_model = GUIModel(name="TechCompanyApp", package="com.example.techcompany", versionCode="1", versionName="1.0", description=WebPage_description, screenCompatibility=True, modules={TechModule})
