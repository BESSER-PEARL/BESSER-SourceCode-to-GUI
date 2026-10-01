from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#38A169", text_color="#FFFFFF", border_color="#2F855A")
buttonPosition = Position(type=PositionType.Relative, top="", left="", right="", bottom="", alignment="", z_index=0)
buttonSize = Size(width="", height="40", padding="8px", margin="24", font_size="14", icon_size="", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
InputFieldColor = Color(background_color="#FFFFFF", text_color="#4A5568", border_color="#CBD5E0")
inputFieldPosition = Position(type=PositionType.Relative, top="", left="", right="", bottom="", alignment="", z_index=0)
inputFieldSize = Size(width="100%", height="auto", padding="10px", margin="", font_size="14", icon_size="", unit_size=UnitSize.PIXELS)
inputFieldStyling = Styling(size=inputFieldSize, position=inputFieldPosition, color=InputFieldColor)
viewComponent = ViewComponent(name="RealEstateHomePage", description="Welcome page for the real estate company")
logoImage = Image(name="LogoImage", description="")
menuItems = {MenuItem(label="Home"), MenuItem(label="About"), MenuItem(label="Contact")}
navigationMenu = Menu(name="NavigationMenu", description="Main navigation menu", menuItems=menuItems)
searchInputField = InputField(name="SearchInput", description="Search for a property", type="Text", validationRules="", styling=inputFieldStyling)
searchButton = Button(name="SearchButton", description="Search properties", label="Search", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Search, styling=buttonStyling)
searchForm = Form(name="SearchForm", description="Form to search properties", inputFields={searchInputField}, styling=None)
RealEstateHomeScreen = Screen(name="RealEstateHomeScreen", description="Main screen for the real estate company", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Large", view_elements={logoImage, navigationMenu, searchForm, searchButton}, is_main_page=True, layout=ScreenLayout)
RealEstateModule = Module(name="RealEstateModule", screens={RealEstateHomeScreen})
gui_model = GUIModel(name="RealEstateApp", package="com.example.realestate", versionCode="1", versionName="1.0", description="A web application for a real estate company.", screenCompatibility=True, modules={RealEstateModule})
webPage = WebPage(attributes={WebPage_logo, WebPage_navLinks, WebPage_title, WebPage_description, WebPage_searchPlaceholder})
searchFormClass = SearchForm(attributes={SearchForm_searchInput})
