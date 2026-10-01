from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#38A169", text_color="#FFFFFF", border_color="#2F855A")
buttonPosition = Position(type=PositionType.Relative, top="", left="", right="", bottom="", alignment="", z_index=0)
buttonSize = Size(width="", height="40", padding="8px", margin="24", font_size="14", icon_size="", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
FormColor = Color(background_color="#FFFFFF", text_color="#4A5568", border_color="#E2E8F0")
formPosition = Position(type=PositionType.Relative, top="", left="", right="", bottom="", alignment="", z_index=0)
formSize = Size(width="100%", height="auto", padding="16px", margin="32px", font_size="", icon_size="", unit_size=UnitSize.PIXELS)
formStyling = Styling(size=formSize, position=formPosition, color=FormColor)
InputFieldColor = Color(background_color="#EDF2F7", text_color="#4A5568", border_color="#CBD5E0")
inputFieldPosition = Position(type=PositionType.Relative, top="", left="", right="", bottom="", alignment="", z_index=0)
inputFieldSize = Size(width="100%", height="40", padding="8px", margin="8px", font_size="14", icon_size="", unit_size=UnitSize.PIXELS)
inputFieldStyling = Styling(size=inputFieldSize, position=inputFieldPosition, color=InputFieldColor)
viewComponent = ViewComponent(name="TravelAgencyView", description="Travel agency page with sections and a form")
parallax = Image(name="ParallaxImage", description="Background image for parallax effect", styling=None)
parallax.backgroundImage = Parallax_backgroundImage
section1 = ViewComponent(name="Section1", description="First section of the website", styling=None)
section1.title = Section_title
section1.content = Section_content
section2 = ViewComponent(name="Section2", description="Second section of the website", styling=None)
section2.title = Section_title
section2.content = Section_content
section3 = ViewComponent(name="Section3", description="Third section of the website", styling=None)
section3.title = Section_title
section3.content = Section_content
button1 = Button(name="Button1", description="Call to action button in section 1", label="Call to Action", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, styling=buttonStyling)
button2 = Button(name="Button2", description="Call to action button in section 2", label="Call to Action", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, styling=buttonStyling)
button3 = Button(name="Button3", description="Call to action button in section 3", label="Call to Action", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, styling=buttonStyling)
form = Form(name="ContactForm", description="Form for user contact information", inputFields=set(), styling=formStyling)
nameField = InputField(name="NameField", description="Input field for name", type=InputField_inputType, validationRules="", styling=inputFieldStyling)
nameField.label = InputField_label
nameField.placeholder = InputField_placeholder
emailField = InputField(name="EmailField", description="Input field for email", type=InputField_inputType, validationRules="", styling=inputFieldStyling)
emailField.label = InputField_label
emailField.placeholder = InputField_placeholder
form.inputFields.update({nameField, emailField})
TravelAgencyScreen = Screen(name="TravelAgencyScreen", description="Screen for the travel agency page", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={parallax, section1, section2, section3, button1, button2, button3, form}, is_main_page=True, layout=ScreenLayout)
TravelAgencyModule = Module(name="TravelAgencyModule", screens={TravelAgencyScreen})
gui_model = GUIModel(name="TravelAgencyApp", package="com.example.travelagency", versionCode="1", versionName="1.0", description="A web application for a travel agency.", screenCompatibility=True, modules={TravelAgencyModule})
