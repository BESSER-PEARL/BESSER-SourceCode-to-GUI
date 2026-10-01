from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

headerColor = Color(background_color="", text_color="#FFFFFF", border_color="")
headerPosition = Position(type=PositionType.Absolute, top="0", left="0", right="0", bottom="", alignment="", z_index=0)
headerSize = Size(width="100%", height="100vh", padding="", margin="", font_size="", icon_size="", unit_size=UnitSize.PERCENT)
headerStyling = Styling(size=headerSize, position=headerPosition, color=headerColor)
navColor = Color(background_color="", text_color="#FFFFFF", border_color="")
navPosition = Position(type=PositionType.Absolute, top="0", left="", right="0", bottom="", alignment="", z_index=1)
navSize = Size(width="100%", height="", padding="16px", margin="", font_size="", icon_size="", unit_size=UnitSize.PIXELS)
navStyling = Styling(size=navSize, position=navPosition, color=navColor)
buttonColor = Color(background_color="#FFFFFF", text_color="#6B46C1", border_color="")
buttonPosition = Position(type=PositionType.Relative, top="", left="", right="", bottom="", alignment="", z_index=0)
buttonSize = Size(width="", height="", padding="8px 16px", margin="", font_size="", icon_size="", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=buttonColor)
headerComponent = ViewComponent(name=header.ends["Header"].name, description="Main header with background image", styling=headerStyling)
navComponent = ViewComponent(name=navigation.ends["Navigation"].name, description="Navigation bar", styling=navStyling)
buttonComponent = Button(name="BookNowButton", description="Button to book travel", label="Book Now", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, styling=buttonStyling)
mainScreen = Screen(name="TravelAgencyHome", description="Home screen for the travel agency", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Large", view_elements={headerComponent, navComponent, buttonComponent}, is_main_page=True)
travelModule = Module(name="TravelModule", screens={mainScreen})
gui_model = GUIModel(name="TravelAgencyApp", package="com.example.travelagency", versionCode="1", versionName="1.0", description="Travel agency application", screenCompatibility=True, modules={travelModule})
