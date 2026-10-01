from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *
from besser.BUML.metamodel.structural import Property
from structural_model import header, mainContent

headerColor = Color(background_color="#FFFFFF", text_color="#000000", border_color="")
headerPosition = Position(type=PositionType.Relative, top="", left="", right="", bottom="", alignment="center", z_index=0)
headerSize = Size(width="100%", height="auto", padding="12px", margin="", font_size="40px", icon_size="", unit_size=UnitSize.PIXELS)
headerStyling = Styling(size=headerSize, position=headerPosition, color=headerColor)
buttonColor = Color(background_color="#EF4444", text_color="#FFFFFF", border_color="")
buttonPosition = Position(type=PositionType.Relative, top="", left="", right="", bottom="", alignment="", z_index=0)
buttonSize = Size(width="", height="40px", padding="8px", margin="8px", font_size="16px", icon_size="", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=buttonColor)
mainContentColor = Color(background_color="#F3F4F6", text_color="#000000", border_color="")
mainContentPosition = Position(type=PositionType.Relative, top="", left="", right="", bottom="", alignment="", z_index=0)
mainContentSize = Size(width="100%", height="auto", padding="12px", margin="", font_size="24px", icon_size="", unit_size=UnitSize.PIXELS)
mainContentStyling = Styling(size=mainContentSize, position=mainContentPosition, color=mainContentColor)
headerComponent = ViewComponent(name=header.ends["Header"].name, description="Header section with title", styling=headerStyling)
signUpButton = Button(name="SignUpButton", description="Sign up for a consultation", label="Sign Up for a Consultation", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add, styling=buttonStyling)
mainContentComponent = ViewComponent(name=mainContent.ends["MainContent"].name, description="Main content section with about us", styling=mainContentStyling)
financialServicesScreen = Screen(name="FinancialServicesScreen", description="Financial Services Page", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Large", view_elements={headerComponent, signUpButton, mainContentComponent}, is_main_page=True)
financialServicesModule = Module(name="FinancialServicesModule", screens={financialServicesScreen})
gui_model = GUIModel(name="FinancialServicesApp", package="com.example.financialservices", versionCode="1", versionName="1.0", description="A web application for financial services.", screenCompatibility=True, modules={financialServicesModule})
