from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#54bfff", text_color="#636363", border_color="#0056b3")
buttonPosition = Position(type=PositionType.Relative, z_index=10)
buttonSize = Size(width="8em", height="2em", padding="8px", margin="0.5em", font_size="14px", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
viewComponent = ViewComponent(name="AcronymLookupView", description="A tool for looking up acronyms")
acronymOnlyCheckbox = InputField(name="AcronymOnlyCheckbox", description="Search by Acronym only", type=InputFieldType.Checkbox, styling=None)
nameOnlyCheckbox = InputField(name="NameOnlyCheckbox", description="Search by name/term only", type=InputFieldType.Checkbox, styling=None)
searchInputField = InputField(name="SearchInput", description="Search input field", type=InputFieldType.Search, styling=Styling(size=Size(width="20em", height="2em", padding="0.5em", margin="0.3em", font_size="1.05em", unit_size=UnitSize.EM)))
searchButton = Button(name="SearchButton", description="Search button", label="Search", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Search, styling=buttonStyling)
clearButton = Button(name="ClearButton", description="Clear button", label="Clear", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Cancel, styling=buttonStyling)
footerContactEmail = InputField(name="FooterContactEmail", description="Contact email", type=InputFieldType.Email, styling=None)
footerPoweredBy = InputField(name="FooterPoweredBy", description="Powered by", type=InputFieldType.Text, styling=None)
footerServiceDeskEmail = InputField(name="FooterServiceDeskEmail", description="Service desk email", type=InputFieldType.Email, styling=None)
AcronymLookupScreen = Screen(name="AcronymLookupScreen", description="Screen for acronym lookup tool", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={acronymOnlyCheckbox, nameOnlyCheckbox, searchInputField, searchButton, clearButton, footerContactEmail, footerPoweredBy, footerServiceDeskEmail}, is_main_page=True, layout=ScreenLayout)
AcronymLookupModule = Module(name="AcronymLookupModule", screens={AcronymLookupScreen})
gui_model = GUIModel(name="AcronymLookupApp", package="com.example.acronymlookup", versionCode="1", versionName="1.0", description="A tool for looking up acronyms", screenCompatibility=True, modules={AcronymLookupModule})
