from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#007BFF", text_color="#FFFFFF", border_color="#0056b3")
buttonPosition = Position(type=PositionType.Relative, z_index=10)
buttonSize = Size(width="100%", height="40px", padding="8px", margin="24px", font_size="14px", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
viewComponent = ViewComponent(name="ContactManagerView", description="Manage contacts with ease")
listContactsButton = Button(name="ListContactsButton", description="List all contacts", label="List Contacts", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.ShowList, styling=buttonStyling)
addContactButton = Button(name="AddContactButton", description="Add a new contact", label="Add Contact", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add, styling=buttonStyling)
searchStringField = InputField(name="SearchStringField", description="Search contacts", type=InputFieldType.Search, validationRules="", styling=Styling(size=Size(width="100%", unit_size=UnitSize.PIXELS)))
searchForm = Form(name="SearchForm", description="Form for searching contacts", inputFields={searchStringField}, styling=Styling(size=Size(width="100%", unit_size=UnitSize.PIXELS)))
ContactManagerScreen = Screen(name="ContactManagerScreen", description="Screen for managing contacts", x_dpi="160", y_dpi="160", screen_size="Medium", view_elements={listContactsButton, addContactButton, searchForm}, is_main_page=True, layout=ScreenLayout)
ContactManagerModule = Module(name="ContactManagerModule", screens={ContactManagerScreen})
gui_model = GUIModel(name="ContactManagerApp", package="com.example.contactmanager", versionCode="1", versionName="1.0", description="A web application for managing contacts.", screenCompatibility=True, modules={ContactManagerModule})
