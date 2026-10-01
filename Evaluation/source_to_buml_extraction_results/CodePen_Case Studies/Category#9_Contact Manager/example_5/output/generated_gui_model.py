from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#007BFF", text_color="#FFFFFF", border_color="#0056b3")
buttonPosition = Position(type=PositionType.Relative, alignment="center", z_index=10)
buttonSize = Size(width="auto", height="40px", padding="8px", margin="5px", font_size="14px", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
inputFieldColor = Color(background_color="#FFFFFF", text_color="#000000", border_color="#CCCCCC")
inputFieldPosition = Position(type=PositionType.Relative, alignment="left", z_index=0)
inputFieldSize = Size(width="100%", height="auto", padding="10px", margin="10px", font_size="14px", unit_size=UnitSize.PIXELS)
inputFieldStyling = Styling(size=inputFieldSize, position=inputFieldPosition, color=inputFieldColor)
viewComponent = ViewComponent(name="ContactManagerView", description="Manage contacts with add, save, and load functionalities")
contactForm = Form(name="ContactForm", description="Form to add a new contact", inputFields={InputField(name="NameInput", description="Input for contact name", type="Text", validationRules="required", styling=inputFieldStyling), InputField(name="EmailInput", description="Input for contact email", type="Email", validationRules="required", styling=inputFieldStyling)})
newContactButton = Button(name="NewContactButton", description="Add a new contact", label="New Contact", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add, styling=buttonStyling)
emptyButton = Button(name="EmptyButton", description="Empty the contact list", label="Empty", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Delete, styling=buttonStyling)
saveButton = Button(name="SaveButton", description="Save the contact list", label="Save", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Save, styling=buttonStyling)
loadButton = Button(name="LoadButton", description="Load the contact list", label="Load", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.ShowList, styling=buttonStyling)
contactList = DataList(name="ContactList", description="List of contacts", list_sources=set(), styling=inputFieldStyling)
ContactManagerScreen = Screen(name="ContactManagerScreen", description="Screen to manage contacts", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={contactForm, newContactButton, emptyButton, saveButton, loadButton, contactList}, is_main_page=True, layout=ScreenLayout)
ContactManagerModule = Module(name="ContactManagerModule", screens={ContactManagerScreen})
gui_model = GUIModel(name="ContactManagerApp", package="com.example.contactmanager", versionCode="1", versionName="1.0", description="A web application for managing contacts.", screenCompatibility=True, modules={ContactManagerModule})
