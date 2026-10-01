from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#4C51BF", text_color="#FFFFFF", border_color="#3B49DF")
buttonPosition = Position(type=PositionType.Relative, z_index=10)
buttonSize = Size(width="auto", height="40px", padding="8px", margin="24px", font_size="14px", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
viewComponent = ViewComponent(name="RestaurantView", description="Display restaurant information and reservation form")
menuLink1 = MenuItem(label="Menu")
menuLink2 = MenuItem(label="Reservation")
navBar = Menu(name="NavBar", description="Navigation bar with links", menuItems={menuLink1, menuLink2})
nameField = InputField(name="NameField", description="Input for name", type=InputFieldType.Text, styling=None)
emailField = InputField(name="EmailField", description="Input for email", type=InputFieldType.Email, styling=None)
reservationForm = Form(name="ReservationForm", description="Form for making reservations", inputFields={nameField, emailField}, styling=None)
submitButton = Button(name="SubmitButton", description="Submit reservation", label="Submit", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Submit, styling=buttonStyling)
hoursOfOperation = DataSourceElement(name="HoursOfOperation", dataSourceClass=HoursOfOperation, fields={HoursOfOperation_weekdayHours, HoursOfOperation_weekendHours})
contactInformation = DataSourceElement(name="ContactInformation", dataSourceClass=ContactInformation, fields={ContactInformation_address, ContactInformation_phone, ContactInformation_email})
footer = ViewContainer(name="Footer", description="Footer with hours and contact info", layout=None, view_elements={hoursOfOperation, contactInformation})
RestaurantScreen = Screen(name="RestaurantScreen", description="Restaurant landing page with reservation form", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={navBar, reservationForm, submitButton, footer}, is_main_page=True, layout=ScreenLayout)
RestaurantModule = Module(name="RestaurantModule", screens={RestaurantScreen})
gui_model = GUIModel(name="RestaurantApp", package="com.example.restaurantapp", versionCode="1", versionName="1.0", description="A web application for restaurant reservations.", screenCompatibility=True, modules={RestaurantModule})
