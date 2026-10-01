from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="10px", alignment=JustificationType.Left)
inputFieldColor = Color(background_color="#FFFFFF", text_color="#000000", border_color="#CCCCCC")
inputFieldPosition = Position(type=PositionType.Relative)
inputFieldSize = Size(width="400px", height="30px", padding="5px", margin="5px", font_size="14px", unit_size=UnitSize.PIXELS)
inputFieldStyling = Styling(size=inputFieldSize, position=inputFieldPosition, color=inputFieldColor)
buttonColor = Color(background_color="#949bc4", text_color="#fdfff5", border_color="#0056b3")
buttonPosition = Position(type=PositionType.Relative)
buttonSize = Size(width="100px", height="40px", padding="5px", margin="10px", font_size="14px", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=buttonColor)
viewComponent = ViewComponent(name="PhoneBookView", description="Manage phone book entries")
givenNameField = InputField(name="GivenNameField", description="Input for given name", type=InputFieldType.Text, validationRules="", styling=inputFieldStyling)
familyNameField = InputField(name="FamilyNameField", description="Input for family name", type=InputFieldType.Text, validationRules="", styling=inputFieldStyling)
phoneNumberField = InputField(name="PhoneNumberField", description="Input for phone number", type=InputFieldType.Tel, validationRules="", styling=inputFieldStyling)
addContactButton = Button(name="AddContactButton", description="Button to add contact", label="Add contact", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add, styling=buttonStyling)
phoneBookForm = Form(name="PhoneBookForm", description="Form to add phone book entries", inputFields={givenNameField, familyNameField, phoneNumberField}, styling=None)
PhoneBookScreen = Screen(name="PhoneBookScreen", description="Screen for managing phone book", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={phoneBookForm, addContactButton}, is_main_page=True, layout=ScreenLayout)
PhoneBookModule = Module(name="PhoneBookModule", screens={PhoneBookScreen})
gui_model = GUIModel(name="PhoneBookApp", package="com.example.phonebook", versionCode="1", versionName="1.0", description="An application to manage phone book entries.", screenCompatibility=True, modules={PhoneBookModule})
