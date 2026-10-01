from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColorPrimary = Color(background_color="#007BFF", text_color="#FFFFFF", border_color="#0056b3")
ButtonColorDefault = Color(background_color="#FFFFFF", text_color="#000000", border_color="#CCCCCC")
buttonPosition = Position(type=PositionType.Relative, z_index=10)
buttonSize = Size(height="40", padding="8px", margin="24", font_size="14", unit_size=UnitSize.PIXELS)
buttonStylingPrimary = Styling(size=buttonSize, position=buttonPosition, color=ButtonColorPrimary)
buttonStylingDefault = Styling(size=buttonSize, position=buttonPosition, color=ButtonColorDefault)
viewComponent = ViewComponent(name="NorchVuejsApp", description="Testing your search index")
searchInputField = InputField(name="SearchBox", description="Input field for search queries", type=InputFieldType.Text, validationRules="", styling=Styling(size=Size(width="100%", height="40", padding="8px", unit_size=UnitSize.PIXELS)))
searchButton = Button(name="SearchButton", description="Button to initiate search", label="Search", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Search, styling=buttonStylingPrimary)
jsonButton = Button(name="JsonButton", description="Button to view JSON", label="JSON", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.View, styling=buttonStylingDefault)
resultsDataSource = DataSourceElement(name="ResultsDataSource", dataSourceClass=Results, fields=[Results_categories, Results_searchresults])
resultsList = DataList(name="ResultsList", description="List of search results", list_sources={resultsDataSource}, styling=Styling(size=Size(width="100%", height="auto", padding="10px", unit_size=UnitSize.PIXELS)))
NorchVuejsScreen = Screen(name="NorchVuejsScreen", description="Screen for Norch Vuejs app", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={searchInputField, searchButton, jsonButton, resultsList}, is_main_page=True, layout=ScreenLayout)
NorchModule = Module(name="NorchModule", screens={NorchVuejsScreen})
gui_model = GUIModel(name="NorchVuejsApp", package="com.example.norchvuejsapp", versionCode="1", versionName="1.0", description="A Vue.js application for testing search index", screenCompatibility=True, modules={NorchModule})
