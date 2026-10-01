from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *
from besser.BUML.metamodel.structural import Class, Property, Method, Parameter, BinaryAssociation, Generalization, DomainModel, Enumeration, EnumerationLiteral, Multiplicity, StringType, IntegerType, FloatType, BooleanType, TimeType, DateType, DateTimeType, TimeDeltaType, AnyType, Constraint, AssociationClass, Metadata
from structural_model import Menu, Menu_item, Menu_price

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ImagePosition = Position(type=PositionType.Relative, alignment="center")
ImageSize = Size(width="50%", height="auto", margin="8px", unit_size=UnitSize.PERCENT)
ImageColor = Color(border_color="", text_color="", background_color="")
ImageStyling = Styling(size=ImageSize, position=ImagePosition, color=ImageColor)
NavPosition = Position(type=PositionType.Relative, alignment="center")
NavSize = Size(width="auto", height="auto", margin="8px", unit_size=UnitSize.PIXELS)
NavColor = Color(text_color="#FFFFFF", border_color="", background_color="")
NavStyling = Styling(size=NavSize, position=NavPosition, color=NavColor)
TablePosition = Position(type=PositionType.Relative)
TableSize = Size(width="100%", height="auto", unit_size=UnitSize.PERCENT)
TableColor = Color(background_color="#FFFFFF", border_color="", text_color="")
TableStyling = Styling(size=TableSize, position=TablePosition, color=TableColor)
LogoImage = Image(name="LogoImage", description="Logo of the page", styling=ImageStyling)
NavMenu = Menu(name="NavMenu", description="Navigation menu", menuItems={MenuItem(label="Home"), MenuItem(label="Menu"), MenuItem(label="About Us"), MenuItem(label="Contact")}, styling=NavStyling)
MenuTable = DataList(name="MenuTable", description="List of menu items", list_sources=set(), styling=TableStyling)
MenuScreen = Screen(name="MenuScreen", description="Screen displaying the menu", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={LogoImage, NavMenu, MenuTable}, is_main_page=True, layout=ScreenLayout)
MenuModule = Module(name="MenuModule", screens={MenuScreen})
gui_model = GUIModel(name="MenuApp", package="com.example.menuapp", versionCode="1", versionName="1.0", description="A web application for displaying a menu.", screenCompatibility=True, modules={MenuModule})
