from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#96858F", text_color="#FFFFFF", border_color="transparent")
buttonPosition = Position(type=PositionType.Relative, z_index=10)
buttonSize = Size(height="40px", padding="12px", font_size="0.9em", unit_size=UnitSize.EM)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
inputFieldSize = Size(width="200px", height="30px", padding="5px", unit_size=UnitSize.PIXELS)
inputFieldStyling = Styling(size=inputFieldSize)
viewComponent = ViewComponent(name="ContactManagerView", description="Manage contacts with add and search functionality")
contactForm = Form(name="ContactForm", description="Form to add a new contact", inputFields={InputField(name="NameInput", description="Input for contact name", type="Text", styling=inputFieldStyling), InputField(name="EmailInput", description="Input for contact email", type="Email", styling=inputFieldStyling)}, styling=None)
addContactButton = Button(name="AddContactButton", description="Button to add a new contact", label="Add new Contact", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add, styling=buttonStyling)
emptyButton = Button(name="EmptyButton", description="Button to empty the contact list", label="Empty", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Delete, styling=buttonStyling)
saveButton = Button(name="SaveButton", description="Button to save the contact list", label="Save", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Save, styling=buttonStyling)
loadButton = Button(name="LoadButton", description="Button to load the contact list", label="Load", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.ShowList, styling=buttonStyling)
searchInputField = InputField(name="SearchInput", description="Input field for searching contacts by name", type="Search", styling=inputFieldStyling)
contactsDataList = DataList(name="ContactsList", description="List of contacts", list_sources=set(), styling=None)
ContactManagerScreen = Screen(name="ContactManagerScreen", description="Screen for managing contacts", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={contactForm, addContactButton, searchInputField, contactsDataList, emptyButton, saveButton, loadButton}, is_main_page=True, layout=ScreenLayout)
ContactManagerModule = Module(name="ContactManagerModule", screens={ContactManagerScreen})
gui_model = GUIModel(name="ContactManagerApp", package="com.example.contactmanager", versionCode="1", versionName="1.0", description="A web application for managing contacts.", screenCompatibility=True, modules={ContactManagerModule})
