from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#EF4444", text_color="#FFFFFF", border_color="#DC2626")
buttonPosition = Position(type=PositionType.Relative, z_index=0)
buttonSize = Size(width="", height="40", padding="8px", margin="24", font_size="14", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
inputFieldColor = Color(background_color="#FFFFFF", text_color="#000000", border_color="#CCCCCC")
inputFieldPosition = Position(type=PositionType.Relative, z_index=0)
inputFieldSize = Size(width="100%", height="auto", padding="8px", margin="8px", font_size="14", unit_size=UnitSize.PIXELS)
inputFieldStyling = Styling(size=inputFieldSize, position=inputFieldPosition, color=inputFieldColor)
viewComponent: ViewComponent = ViewComponent(name="WebPageView", description="Display the automotive company webpage")
headerImage: Image = Image(name="HeaderImage", description="")
navMenu: Menu = Menu(name="NavigationMenu", description="Main navigation menu", menuItems={MenuItem(label="Home"), MenuItem(label="About"), MenuItem(label="Vehicles"), MenuItem(label="Contact")})
featuredVehiclesButton: Button = Button(name="FeaturedVehiclesButton", description="View featured vehicles", label="View Vehicles", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, styling=buttonStyling)
serviceAppointmentForm: Form = Form(
    name="ServiceAppointmentForm",
    description="Form for scheduling a service appointment",
    inputFields={
        InputField(name="NameField", description="Name input field", type="Text", validationRules="", styling=inputFieldStyling),
        InputField(name="EmailField", description="Email input field", type="Email", validationRules="", styling=inputFieldStyling),
        InputField(name="PhoneField", description="Phone input field", type="Tel", validationRules="", styling=inputFieldStyling),
        InputField(name="MessageField", description="Message input field", type="Text", validationRules="", styling=inputFieldStyling),
    },
)
submitButton: Button = Button(name="SubmitButton", description="Submit the service appointment form", label="Submit", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Submit, styling=buttonStyling)
WebPageScreen: Screen = Screen(name="WebPageScreen", description="Automotive company webpage", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={headerImage, navMenu, featuredVehiclesButton, serviceAppointmentForm, submitButton}, is_main_page=True, layout=ScreenLayout)
WebPageModule: Module = Module(name="WebPageModule", screens={WebPageScreen})
gui_model: GUIModel = GUIModel(name="AutomotiveCompanyApp", package="com.example.automotivecompany", versionCode="1", versionName="1.0", description="Web application for an automotive company.", screenCompatibility=True, modules={WebPageModule})
