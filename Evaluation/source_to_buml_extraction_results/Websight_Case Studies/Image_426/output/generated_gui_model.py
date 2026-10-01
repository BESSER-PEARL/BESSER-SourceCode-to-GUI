from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
BackgroundImageColor = Color(background_color="", text_color="#FFFFFF", border_color="")
BackgroundImagePosition = Position(type=PositionType.Absolute, top="0", left="0", right="0", bottom="0", alignment="center", z_index=0)
BackgroundImageSize = Size(width="100%", height="100%", padding="", margin="", font_size="", icon_size="", unit_size=UnitSize.PERCENT)
BackgroundImageStyling = Styling(size=BackgroundImageSize, position=BackgroundImagePosition, color=BackgroundImageColor)
MenuColor = Color(background_color="#FFFFFF", text_color="#343A40", border_color="#CED4DA")
MenuPosition = Position(type=PositionType.Relative, top="", left="", right="", bottom="", alignment="", z_index=0)
MenuSize = Size(width="50%", height="auto", padding="8px", margin="24", font_size="14", icon_size="", unit_size=UnitSize.PIXELS)
MenuStyling = Styling(size=MenuSize, position=MenuPosition, color=MenuColor)
ContactColor = Color(background_color="#FFFFFF", text_color="#343A40", border_color="#CED4DA")
ContactPosition = Position(type=PositionType.Relative, top="", left="", right="", bottom="", alignment="", z_index=0)
ContactSize = Size(width="100%", height="auto", padding="10px", margin="", font_size="", icon_size="", unit_size=UnitSize.PIXELS)
ContactStyling = Styling(size=ContactSize, position=ContactPosition, color=ContactColor)
backgroundImage: Image = Image(name="CityBackgroundImage", description="Full-screen background image of a city skyline", styling=BackgroundImageStyling)
menuItems = {MenuItem(label="Accounts"), MenuItem(label="Loans"), MenuItem(label="Credit Cards"), MenuItem(label="Investments")}
menu: Menu = Menu(name="MainMenu", description="Main navigation menu", menuItems=menuItems, styling=MenuStyling)
contactDataSource: DataSourceElement = DataSourceElement(name="ContactDataSource", dataSourceClass=Contact, fields={Contact_companyName, Contact_address, Contact_phone, Contact_email})
contactList: DataList = DataList(name="ContactList", description="Contact information", list_sources={contactDataSource}, styling=ContactStyling)
FinancialServicesScreen: Screen = Screen(name="FinancialServicesScreen", description="Financial Services Page with a city skyline background", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Large", is_main_page=True, view_elements={backgroundImage, menu, contactList}, layout=ScreenLayout)
FinancialServicesModule: Module = Module(name="FinancialServicesModule", screens={FinancialServicesScreen})
gui_model: GUIModel = GUIModel(name="FinancialServicesApp", package="com.example.financialservices", versionCode="1", versionName="1.0", description="A professional and sophisticated design for financial services.", screenCompatibility=True, modules={FinancialServicesModule})
