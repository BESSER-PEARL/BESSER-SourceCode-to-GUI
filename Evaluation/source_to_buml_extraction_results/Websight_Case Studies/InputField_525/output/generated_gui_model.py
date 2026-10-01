from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

headerStyling = Styling(size=Size(width="100%", height="50px", unit_size=UnitSize.PIXELS), position=Position(type=PositionType.Relative), color=Color(background_color="#FFFFFF", border_color="", text_color=""))
searchInputStyling = Styling(size=Size(width="auto", height="auto", unit_size=UnitSize.PIXELS), position=Position(type=PositionType.Relative), color=Color(border_color="", background_color="", text_color=""))
searchButtonStyling = Styling(size=Size(width="auto", height="auto", unit_size=UnitSize.PIXELS), position=Position(type=PositionType.Relative), color=Color(background_color="#EC4899", text_color="#FFFFFF", border_color=""))
sectionStyling = Styling(size=Size(width="100%", height="auto", unit_size=UnitSize.PIXELS), position=Position(type=PositionType.Relative), color=Color(border_color="", background_color="", text_color=""))
buttonStyling = Styling(size=Size(width="auto", height="auto", unit_size=UnitSize.PIXELS), position=Position(type=PositionType.Relative), color=Color(background_color="#EC4899", text_color="#FFFFFF", border_color=""))
logoImage = Image(name=WebPage_logo.name, styling=headerStyling, description="")
searchInput = InputField(name=WebPage_searchInput.name, description="Search for properties, communities, agents...", type="Text", styling=searchInputStyling)
searchButton = Button(name="SearchButton", description="Search button", label="Search", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Search, styling=searchButtonStyling)
propertiesSection = ViewComponent(name=WebPage_propertiesDescription.name, description="Properties section", styling=sectionStyling)
communitiesSection = ViewComponent(name=WebPage_communitiesDescription.name, description="Communities section", styling=sectionStyling)
agentsSection = ViewComponent(name=WebPage_agentsDescription.name, description="Agents section", styling=sectionStyling)
contactSection = ViewComponent(name=WebPage_contactDescription.name, description="Contact section", styling=sectionStyling)
viewPropertiesButton = Button(name="ViewPropertiesButton", description="View properties", label="View Properties", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, styling=buttonStyling)
viewCommunitiesButton = Button(name="ViewCommunitiesButton", description="View communities", label="View Communities", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, styling=buttonStyling)
meetAgentsButton = Button(name="MeetAgentsButton", description="Meet our agents", label="Meet Our Agents", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, styling=buttonStyling)
contactUsButton = Button(name="ContactUsButton", description="Contact us", label="Contact Us", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, styling=buttonStyling)
homeScreen = Screen(name="HomeScreen", description="Main page of the real estate application", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={logoImage, searchInput, searchButton, propertiesSection, communitiesSection, agentsSection, contactSection, viewPropertiesButton, viewCommunitiesButton, meetAgentsButton, contactUsButton}, is_main_page=True, layout=Layout(type=LayoutType.Flex, orientation="vertical", alignment=JustificationType.Center))
realEstateModule = Module(name="RealEstateModule", screens={homeScreen})
gui_model = GUIModel(name="RealEstateApp", package="com.example.realestate", versionCode="1", versionName="1.0", description="A web application for real estate management.", screenCompatibility=True, modules={realEstateModule})
