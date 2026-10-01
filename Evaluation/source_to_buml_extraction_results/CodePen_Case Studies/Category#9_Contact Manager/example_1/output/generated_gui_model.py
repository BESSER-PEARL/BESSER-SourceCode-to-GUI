from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
inputFieldStyling = Styling(size=Size(width="100%", height="40px", padding="8px", margin="10px", font_size="14px", unit_size=UnitSize.PIXELS), position=Position(type=PositionType.Relative, z_index=0), color=Color(background_color="#FFFFFF", text_color="#000000", border_color="#CCCCCC"))
buttonStyling = Styling(size=Size(width="100%", height="40px", padding="8px", margin="10px", font_size="14px", unit_size=UnitSize.PIXELS), position=Position(type=PositionType.Relative, z_index=0), color=Color(background_color="#007BFF", text_color="#FFFFFF", border_color="#0056b3"))
errorStyling = Styling(size=Size(width="100%", height="auto", padding="8px", margin="5px", font_size="12px", unit_size=UnitSize.PIXELS), position=Position(type=PositionType.Relative, z_index=0), color=Color(background_color="#FFDDDD", text_color="#FF0000", border_color="#FFAAAA"))
successStyling = Styling(size=Size(width="100%", height="auto", padding="8px", margin="5px", font_size="12px", unit_size=UnitSize.PIXELS), position=Position(type=PositionType.Relative, z_index=0), color=Color(background_color="#DDFFDD", text_color="#008000", border_color="#AAFFAA"))
viewComponent = ViewComponent(name="ContactPageView", description="Contact form with validation and success message")
nameInput = InputField(name="NameInput", description="Full Name", type=InputFieldType.Text, validationRules="required", styling=inputFieldStyling)
emailInput = InputField(name="EmailInput", description="Email Address", type=InputFieldType.Email, validationRules="required|email", styling=inputFieldStyling)
subjectInput = InputField(name="SubjectInput", description="Subject", type=InputFieldType.Text, validationRules="required", styling=inputFieldStyling)
messageInput = InputField(name="MessageInput", description="Message", type=InputFieldType.Text, validationRules="required", styling=inputFieldStyling)
contactForm = Form(name="ContactForm", description="Form to contact us", inputFields={nameInput, emailInput, subjectInput, messageInput}, styling=None)
successMessage = ViewComponent(name="SuccessMessage", description="Form submitted successfully!", styling=successStyling)
submitButton = Button(name="SubmitButton", description="Send Message", label="Send Message", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.SubmitForm, styling=buttonStyling)
ContactPageScreen = Screen(name="ContactPageScreen", description="Contact us page with form and success message", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={contactForm, successMessage, submitButton}, is_main_page=True, layout=ScreenLayout)
ContactModule = Module(name="ContactModule", screens={ContactPageScreen})
gui_model = GUIModel(name="ContactApp", package="com.example.contactapp", versionCode="1", versionName="1.0", description="A web application for contacting us.", screenCompatibility=True, modules={ContactModule})
