from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="horizontal", gap="0", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#F59E0B", text_color="#FFFFFF", border_color="#D97706")
buttonPosition = Position(type=PositionType.Absolute, top="50%", left="50%", alignment="center", z_index=10)
buttonSize = Size(width="150px", height="50px", padding="10px", font_size="16px", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
TableColor = Color(background_color="#FFFFFF", text_color="#000000", border_color="#E5E7EB")
tablePosition = Position(type=PositionType.Relative, top="20px", left="0", alignment="center", z_index=0)
tableSize = Size(width="100%", height="auto", padding="10px", unit_size=UnitSize.PIXELS)
tableStyling = Styling(size=tableSize, position=tablePosition, color=TableColor)
FooterColor = Color(background_color="#F59E0B", text_color="#FFFFFF", border_color="#D97706")
footerPosition = Position(type=PositionType.Relative, top="0", left="0", alignment="center", z_index=0)
footerSize = Size(width="100%", height="50px", padding="10px", unit_size=UnitSize.PIXELS)
footerStyling = Styling(size=footerSize, position=footerPosition, color=FooterColor)
navMenu: Menu = Menu(name="NavigationMenu", description="Main navigation menu", menuItems={MenuItem(label="Home"), MenuItem(label="About Us"), MenuItem(label="Services"), MenuItem(label="Contact Us")})
heroButton: Button = Button(name="HeroButton", description="Get Started button", label="Get Started", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, styling=buttonStyling)
financialTable: DataList = DataList(name="FinancialTable", description="Table displaying financial data", list_sources={DataSourceElement(name="FinancialDataSource", dataSourceClass=FinancialTable, fields={FinancialTable_income, FinancialTable_expenses})}, styling=tableStyling)
footer: ViewComponent = ViewComponent(name="Footer", description="Footer with links", styling=footerStyling)
WebPageScreen: Screen = Screen(name="WebPage", description="Main web page with navigation, hero section, financial data, and footer", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Large", is_main_page=True, view_elements={navMenu, heroButton, financialTable, footer}, layout=ScreenLayout)
WebModule: Module = Module(name="WebModule", screens={WebPageScreen})
gui_model: GUIModel = GUIModel(name="WebApp", package="com.example.webapp", versionCode="1", versionName="1.0", description="A web application for displaying financial data", screenCompatibility=True, modules={WebModule})
