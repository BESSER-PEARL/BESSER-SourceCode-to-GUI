from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#007BFF", text_color="#FFFFFF", border_color="#0056b3")
buttonPosition = Position(type=PositionType.Relative, z_index=10)
buttonSize = Size(width="150px", height="40px", padding="8px", margin="24px", font_size="14px", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
inputFieldColor = Color(background_color="#FFFFFF", text_color="#000000", border_color="#CCCCCC")
inputFieldPosition = Position(type=PositionType.Relative)
inputFieldSize = Size(width="100%", padding="10px", margin="5px", font_size="14px", unit_size=UnitSize.PIXELS)
inputFieldStyling = Styling(size=inputFieldSize, position=inputFieldPosition, color=inputFieldColor)
viewComponent = ViewComponent(name="ContactManagerView", description="Manage contacts with CRUD operations")
personalInfoForm = Form(
    name="PersonalInfoForm",
    description="Form to input personal information",
    inputFields={
        InputField(name=Contact_name.name, description="Enter full name", type="Text", validationRules="required", styling=inputFieldStyling),
        InputField(name=Contact_age.name, description="Enter age", type="Number", validationRules="required min=0 max=120", styling=inputFieldStyling),
        InputField(name=Contact_email.name, description="Enter email", type="Email", validationRules="required", styling=inputFieldStyling),
        InputField(name=Contact_city.name, description="Enter city", type="Text", styling=inputFieldStyling),
        InputField(name=Contact_zipCode.name, description="Enter zip code", type="Number", validationRules="min=0 max=99999", styling=inputFieldStyling),
        InputField(name=Contact_country.name, description="Enter country", type="Text", styling=inputFieldStyling),
    },
)
addContactButton = Button(name="AddContactButton", description="Add new contact", label="Add new Contact", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add, styling=buttonStyling)
addRandomContactsButton = Button(name="AddRandomContactsButton", description="Add two random contacts", label="Add two random Contacts", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add, styling=buttonStyling)
searchContactButton = Button(name="SearchContactButton", description="Search contact by name", label="Search", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Search, styling=buttonStyling)
printContactsButton = Button(name="PrintContactsButton", description="Print contacts to console", label="Print contacts to console", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.ShowList, styling=buttonStyling)
searchInputField = InputField(name=Search_searchInput.name, description="Search contact by name", type="Text", styling=inputFieldStyling)
matchDisplayField = InputField(name=Search_matchDisplay.name, description="Displays matches", type="Text", validationRules="readonly", styling=inputFieldStyling)
ContactManagerScreen = Screen(name="ContactManagerScreen", description="Screen to manage contacts", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={personalInfoForm, addContactButton, addRandomContactsButton, searchInputField, matchDisplayField, searchContactButton, printContactsButton}, is_main_page=True, layout=ScreenLayout)
ContactManagerModule = Module(name="ContactManagerModule", screens={ContactManagerScreen})
gui_model = GUIModel(name="ContactManagerApp", package="com.example.contactmanager", versionCode="1", versionName="1.0", description="A web application for managing contacts.", screenCompatibility=True, modules={ContactManagerModule})
