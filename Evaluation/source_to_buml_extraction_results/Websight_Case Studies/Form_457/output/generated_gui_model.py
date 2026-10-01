from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
HeaderColor = Color(background_color="#6B7280", text_color="#FFFFFF", border_color="")
HeaderPosition = Position(type=PositionType.Relative, alignment=JustificationType.Center)
HeaderSize = Size(width="100%", height="auto", padding="16px", font_size="24", unit_size=UnitSize.PIXELS)
HeaderStyling = Styling(size=HeaderSize, position=HeaderPosition, color=HeaderColor)
ButtonColor = Color(background_color="#6B7280", text_color="#FFFFFF", border_color="")
ButtonPosition = Position(type=PositionType.Inline)
ButtonSize = Size(width="auto", height="auto", padding="8px", margin="4px", font_size="16", unit_size=UnitSize.PIXELS)
ButtonStyling = Styling(size=ButtonSize, position=ButtonPosition, color=ButtonColor)
ImagePosition = Position(type=PositionType.Relative)
ImageSize = Size(width="100%", height="auto", unit_size=UnitSize.PIXELS)
ImageStyling = Styling(size=ImageSize, position=ImagePosition, color=None)
InputFieldPosition = Position(type=PositionType.Relative)
InputFieldSize = Size(width="auto", height="auto", padding="8px", margin="4px", font_size="16", unit_size=UnitSize.PIXELS)
InputFieldStyling = Styling(size=InputFieldSize, position=InputFieldPosition, color=None)
viewComponent: ViewComponent = ViewComponent(name="TravelAgencyView", description="Travel agency homepage with navigation and sections")
header: ViewComponent = ViewComponent(name="Header", description="Header with navigation", styling=HeaderStyling)
menuItems = {MenuItem(label="Home"), MenuItem(label="Destinations"), MenuItem(label="Flights"), MenuItem(label="Hotels"), MenuItem(label="Contact")}
navigationMenu: Menu = Menu(name="NavigationMenu", description="Main navigation menu", menuItems=menuItems, styling=ButtonStyling)
mainImage: Image = Image(name="MainImage", description="Travel banner image", styling=ImageStyling)
destinationsSection: ViewComponent = ViewComponent(name="DestinationsSection", description="Destinations section with images", styling=None)
beachImage: Image = Image(name="BeachImage", description="Beach destination image", styling=ImageStyling)
mountainImage: Image = Image(name="MountainImage", description="Mountain destination image", styling=ImageStyling)
cityImage: Image = Image(name="CityImage", description="City destination image", styling=ImageStyling)
searchInput: InputField = InputField(name="SearchInput", description="Search input field", type="Text", validationRules="", styling=InputFieldStyling)
searchButton: Button = Button(name="SearchButton", description="Search button", label="Search", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Search, styling=ButtonStyling)
searchForm: Form = Form(name="SearchForm", description="Search flights and hotels", inputFields={searchInput}, styling=None)
emailInput: InputField = InputField(name="EmailInput", description="Email input field", type="Email", validationRules="", styling=InputFieldStyling)
signUpButton: Button = Button(name="SignUpButton", description="Sign up button", label="Sign Up", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.SubmitForm, styling=ButtonStyling)
newsletterForm: Form = Form(name="NewsletterForm", description="Newsletter sign-up form", inputFields={emailInput}, styling=None)
footer: ViewComponent = ViewComponent(name="Footer", description="Footer with copyright", styling=HeaderStyling)
TravelAgencyScreen: Screen = Screen(
    name="TravelAgencyScreen",
    description="Main screen for the travel agency",
    x_dpi=Property(name="x_dpi", type=IntegerType, multiplicity=Multiplicity(1, 1)),
    y_dpi=Property(name="y_dpi", type=IntegerType, multiplicity=Multiplicity(1, 1)),
    screen_size=Property(name="screen_size", type=StringType, multiplicity=Multiplicity(1, 1)),
    view_elements={header, navigationMenu, mainImage, destinationsSection, beachImage, mountainImage, cityImage, searchForm, searchButton, newsletterForm, signUpButton, footer},
    is_main_page=True,
    layout=ScreenLayout,
)
TravelAgencyModule: Module = Module(name="TravelAgencyModule", screens={TravelAgencyScreen})
gui_model: GUIModel = GUIModel(name="TravelAgencyApp", package="com.example.travelagency", versionCode=Property(name="versionCode", type=StringType, multiplicity=Multiplicity(1, 1)), versionName=Property(name="versionName", type=StringType, multiplicity=Multiplicity(1, 1)), description="A travel agency web application.", screenCompatibility=True, modules={TravelAgencyModule})
