from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", alignment=JustificationType.Center)
HeaderColor = Color(background_color="#1F2937", text_color="#FFFFFF", border_color="")
HeaderPosition = Position(type=PositionType.Fixed, top="0", left="0", right="0", alignment="center")
HeaderSize = Size(width="100%", height="auto", padding="16px", unit_size=UnitSize.PIXELS)
HeaderStyling = Styling(size=HeaderSize, position=HeaderPosition, color=HeaderColor)
MainColor = Color(background_color="#1F2937", text_color="#FFFFFF", border_color="")
MainPosition = Position(type=PositionType.Relative, top="0", left="0", right="0", alignment="center")
MainSize = Size(width="100%", height="auto", padding="16px", unit_size=UnitSize.PIXELS)
MainStyling = Styling(size=MainSize, position=MainPosition, color=MainColor)
FooterColor = Color(background_color="#374151", text_color="#FFFFFF", border_color="")
FooterPosition = Position(type=PositionType.Fixed, bottom="0", left="0", right="0", alignment="center")
FooterSize = Size(width="100%", height="auto", padding="16px", unit_size=UnitSize.PIXELS)
FooterStyling = Styling(size=FooterSize, position=FooterPosition, color=FooterColor)
HeaderComponent = ViewComponent(name=WebPage_header.name, description="Navigation and social media links", styling=HeaderStyling)
MainComponent = ViewComponent(name=WebPage_main.name, description="Main content area", styling=MainStyling)
FooterComponent = ViewComponent(name=WebPage_footer.name, description="Footer with copyright", styling=FooterStyling)
LearnMoreButton = Button(name="LearnMoreButton", description="Button to learn more about the startup", label="Learn More", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, styling=Styling(size=Size(width="auto", height="auto", padding="8px", unit_size=UnitSize.PIXELS), color=Color(background_color="#10B981", text_color="#FFFFFF", border_color="")))
WebPageScreen = Screen(name="WebPageScreen", description="A web page with header, main content, and footer", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Large", view_elements={HeaderComponent, MainComponent, FooterComponent, LearnMoreButton}, is_main_page=True, layout=ScreenLayout)
WebPageModule = Module(name="WebPageModule", screens={WebPageScreen})
gui_model = GUIModel(name="WebPageApp", package="com.example.webpageapp", versionCode="1", versionName="1.0", description="A web application with a header, main content, and footer.", screenCompatibility=True, modules={WebPageModule})
