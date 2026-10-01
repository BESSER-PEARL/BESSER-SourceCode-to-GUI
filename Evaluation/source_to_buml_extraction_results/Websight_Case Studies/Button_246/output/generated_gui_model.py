from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="horizontal", alignment=JustificationType.Center)
TextColor = Color(text_color="#FFFFFF", background_color="", border_color="")
TextPosition = Position(type=PositionType.Relative)
TextSize = Size(font_size="32px", unit_size=UnitSize.PIXELS)
TextStyling = Styling(size=TextSize, position=TextPosition, color=TextColor)
ButtonColor = Color(background_color="#38A169", text_color="#FFFFFF", border_color="#2F855A")
ButtonPosition = Position(type=PositionType.Relative)
ButtonSize = Size(width="auto", height="40px", padding="8px", margin="10px", font_size="16px", unit_size=UnitSize.PIXELS)
ButtonStyling = Styling(size=ButtonSize, position=ButtonPosition, color=ButtonColor)
ImagePosition = Position(type=PositionType.Relative)
ImageSize = Size(width="100%", height="100%", unit_size=UnitSize.PERCENT)
ImageStyling = Styling(size=ImageSize, position=ImagePosition)
viewComponent: ViewComponent = ViewComponent(name="WelcomeView", description="Welcome page for the technology company")
welcomeText: ViewComponent = ViewComponent(name="WelcomeText", description=WebPage_description, styling=TextStyling)
learnMoreButton: Button = Button(name="LearnMoreButton", description=WebPage_title, label=Button_buttonText, buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, styling=ButtonStyling)
technologyImage: Image = Image(name="TechnologyImage", styling=ImageStyling, description="")
WelcomeScreen: Screen = Screen(name="WelcomeScreen", description=WebPage_description, x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Large", view_elements={welcomeText, learnMoreButton, technologyImage}, is_main_page=True, layout=ScreenLayout)
MyModule: Module = Module(name="TechnologyCompanyModule", screens={WelcomeScreen})
gui_model: GUIModel = GUIModel(name="TechnologyCompanyApp", package="com.example.technologycompany", versionCode="1", versionName="1.0", description="A web application for a technology company.", screenCompatibility=True, modules={MyModule})
