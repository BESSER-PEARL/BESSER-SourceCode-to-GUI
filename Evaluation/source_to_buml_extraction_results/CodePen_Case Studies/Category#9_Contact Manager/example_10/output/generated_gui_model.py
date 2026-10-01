from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *
from some_gui_library import Layout, LayoutType, JustificationType, Color, Position, PositionType, Size, UnitSize, Styling, ViewComponent, InputField, InputFieldType, DataSourceElement, DataList, Screen, Module, GUIModel

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
InputFieldColor = Color(background_color="#FFFFFF", text_color="#000000", border_color="#CCCCCC")
inputFieldPosition = Position(type=PositionType.Relative, z_index=0)
inputFieldSize = Size(width="300px", height="40px", padding="8px", margin="15px", font_size="16px", unit_size=UnitSize.PIXELS)
inputFieldStyling = Styling(size=inputFieldSize, position=inputFieldPosition, color=InputFieldColor)
TableColor = Color(background_color="#FFFFFF", text_color="#000000", border_color="#CCCCCC")
tablePosition = Position(type=PositionType.Relative, z_index=0)
tableSize = Size(width="100%", height="auto", padding="12px", margin="10px", font_size="14px", unit_size=UnitSize.PIXELS)
tableStyling = Styling(size=tableSize, position=tablePosition, color=TableColor)
viewComponent = ViewComponent(name="ContactManagerView", description="Manage contacts with search and table display")
searchInputField = InputField(name="SearchField", description="Search contacts by name", type=InputFieldType.Text, validationRules="", styling=inputFieldStyling)
datasource_contact = DataSourceElement(name="ContactDataSource", dataSourceClass="ContactManager", fields=["name", "email", "phone"])
contactTable = DataList(name="ContactTable", description="Table displaying contact information", list_sources={datasource_contact}, styling=tableStyling)
ContactManagerScreen = Screen(name="ContactManagerScreen", description="Screen for managing contacts", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={searchInputField, contactTable}, is_main_page=True, layout=ScreenLayout)
ContactManagerModule = Module(name="ContactManagerModule", screens={ContactManagerScreen})
gui_model = GUIModel(name="ContactManagerApp", package="com.example.contactmanager", versionCode="1", versionName="1.0", description="An application for managing contacts.", screenCompatibility=True, modules={ContactManagerModule})
