from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", alignment=JustificationType.Center)
TitleColor = Color(text_color="#4A5568", border_color="", background_color="")
TitlePosition = Position(type=PositionType.Relative, alignment="center")
TitleSize = Size(font_size="40", unit_size=UnitSize.PIXELS)
TitleStyling = Styling(size=TitleSize, position=TitlePosition, color=TitleColor)
DescriptionColor = Color(text_color="#718096", border_color="", background_color="")
DescriptionPosition = Position(type=PositionType.Relative, alignment="center")
DescriptionSize = Size(font_size="18", unit_size=UnitSize.PIXELS)
DescriptionStyling = Styling(size=DescriptionSize, position=DescriptionPosition, color=DescriptionColor)
ButtonColor = Color(background_color="#38A169", text_color="#FFFFFF", border_color="")
ButtonPosition = Position(type=PositionType.Relative, alignment="center")
ButtonSize = Size(width="auto", height="40", padding="8px", margin="8px", font_size="16", unit_size=UnitSize.PIXELS)
ButtonStyling = Styling(size=ButtonSize, position=ButtonPosition, color=ButtonColor)
TitleComponent = ViewComponent(name=FashionRetailerPage_title.name, description="Main title of the page", styling=TitleStyling)
DescriptionComponent = ViewComponent(name=FashionRetailerPage_description.name, description="Page description", styling=DescriptionStyling)
ShopButton = Button(name="ShopNowButton", description="Button to navigate to shop", label="Shop Now", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, styling=ButtonStyling)
FashionRetailerScreen = Screen(name="FashionRetailerScreen", description="Welcome screen for the fashion retailer", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={TitleComponent, DescriptionComponent, ShopButton}, is_main_page=True, layout=ScreenLayout)
FashionRetailerModule = Module(name="FashionRetailerModule", screens={FashionRetailerScreen})
gui_model = GUIModel(name="FashionRetailerApp", package="com.example.fashionretailer", versionCode="1", versionName="1.0", description="A premier fashion retailer application.", screenCompatibility=True, modules={FashionRetailerModule})
