from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#007BFF", text_color="#FFFFFF", border_color="#0056b3")
buttonPosition = Position(type=PositionType.Relative, alignment="center", z_index=10)
buttonSize = Size(width="auto", height="40px", padding="8px", margin="24px", font_size="14px", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
inputFieldColor = Color(background_color="#FFFFFF", text_color="#000000", border_color="#CCCCCC")
inputFieldPosition = Position(type=PositionType.Relative, alignment="center", z_index=0)
inputFieldSize = Size(width="100%", height="auto", padding="10px", margin="5px", font_size="14px", unit_size=UnitSize.PIXELS)
inputFieldStyling = Styling(size=inputFieldSize, position=inputFieldPosition, color=inputFieldColor)
viewComponent = ViewComponent(name="VolunteerListView", description="Display a list of volunteers with actions")
searchInputField = InputField(name="SearchVolunteers", description="Search volunteers", type="Search", validationRules="", styling=inputFieldStyling)
emailButton = Button(name="EmailAllButton", description="Email all selected volunteers", label="Email All Volunteers", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Send, styling=buttonStyling)
viewListButton = Button(name="ViewListButton", description="View list of email addresses", label="View List of Email Addresses", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.ShowList, styling=buttonStyling)
datasource_volunteer = DataSourceElement(name="VolunteerDataSource", dataSourceClass=Volunteer, fields=[Volunteer_id, Volunteer_name, Volunteer_phone, Volunteer_email, Volunteer_status, Volunteer_unix])
volunteerList = DataList(name="VolunteerList", description="A list of volunteers", list_sources={datasource_volunteer}, styling=Styling(size=Size(width="100%", height="auto"), position=Position(type=PositionType.Relative)))
VolunteerScreen = Screen(name="VolunteerScreen", description="Manage volunteers", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", is_main_page=True, view_elements={searchInputField, emailButton, viewListButton, volunteerList}, layout=ScreenLayout)
VolunteerModule = Module(name="VolunteerModule", screens={VolunteerScreen})
gui_model = GUIModel(name="VolunteerManagementApp", package="com.example.volunteermanagement", versionCode="1", versionName="1.0", description="A web application for managing volunteers.", screenCompatibility=True, modules={VolunteerModule})
