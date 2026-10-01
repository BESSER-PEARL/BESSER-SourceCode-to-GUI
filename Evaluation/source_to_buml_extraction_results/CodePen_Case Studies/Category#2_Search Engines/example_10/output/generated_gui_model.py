from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
searchButtonColor = Color(background_color="#FFFFFF", text_color="#000000", border_color="#CCCCCC")
searchButtonPosition = Position(type=PositionType.Relative, alignment="center", z_index=0)
searchButtonSize = Size(width="100px", height="40px", padding="8px", font_size="14px", icon_size="16px", unit_size=UnitSize.PIXELS)
searchButtonStyling = Styling(size=searchButtonSize, position=searchButtonPosition, color=searchButtonColor)
inputFieldColor = Color(background_color="#FFFFFF", text_color="#000000", border_color="#CCCCCC")
inputFieldPosition = Position(type=PositionType.Relative, alignment="center", z_index=0)
inputFieldSize = Size(width="100%", height="40px", padding="8px", font_size="14px", unit_size=UnitSize.PIXELS)
inputFieldStyling = Styling(size=inputFieldSize, position=inputFieldPosition, color=inputFieldColor)
viewComponent = ViewComponent(name="YouTubeVideoSearchView", description="Search YouTube videos")
searchInputField = InputField(name="SearchInputField", description="Enter search query", type="Search", validationRules="", styling=inputFieldStyling)
searchButton = Button(name="SearchButton", description="Search YouTube", label="Search", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Search, styling=searchButtonStyling)
YouTubeVideoSearchScreen = Screen(name="YouTubeVideoSearchScreen", description="Search for YouTube videos", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", is_main_page=True, view_elements={searchInputField, searchButton}, layout=ScreenLayout)
YouTubeModule = Module(name="YouTubeModule", screens={YouTubeVideoSearchScreen})
gui_model = GUIModel(name="YouTubeVideoSearchApp", package="com.example.youtubevideosearch", versionCode="1", versionName="1.0", description="A web application for searching YouTube videos.", screenCompatibility=True, modules={YouTubeModule})
