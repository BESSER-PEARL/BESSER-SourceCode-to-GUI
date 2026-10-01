from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#E9D5FF", text_color="#7C3AED", border_color="#7C3AED")
buttonPosition = Position(type=PositionType.Relative)
buttonSize = Size(width="100%", height="40px", padding="8px", margin="24px", font_size="14px", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
viewComponent = ViewComponent(name="ProjectView", description="Display project details with actions")
callToActionButton = Button(name="CallToActionButton", description="Perform an action", label="Call to Action", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, styling=buttonStyling)
projectImage = Image(name="ProjectImage", description="")
datasource_webpage = DataSourceElement(name="WebPageDataSource", dataSourceClass=WebPage, fields=[WebPage_projectTitle, WebPage_projectDescription, WebPage_projectImage, WebPage_projectTeam, WebPage_location, WebPage_servicesProvided])
WebPageScreen = Screen(name="WebPageScreen", description="Display project details", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", is_main_page=True, view_elements={callToActionButton, projectImage}, layout=ScreenLayout)
MyModule = Module(name="WebPageModule", screens={WebPageScreen})
gui_model = GUIModel(name="WebPageApp", package="com.example.webpageapp", versionCode="1", versionName="1.0", description="A web application for displaying project details.", screenCompatibility=True, modules={MyModule})
