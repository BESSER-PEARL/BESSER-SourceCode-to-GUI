from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Grid, orientation="vertical", gap="4px", alignment=JustificationType.Center)
ContainerColor = Color(background_color="#FBD38D", text_color="#000000", border_color="#FFFFFF")
ContainerPosition = Position(type=PositionType.Relative)
ContainerSize = Size(width="100%", height="auto", padding="32px", margin="0", unit_size=UnitSize.PIXELS)
ContainerStyling = Styling(size=ContainerSize, position=ContainerPosition, color=ContainerColor)
CardColor = Color(background_color="#FFFFFF", text_color="#000000", border_color="#E2E8F0")
CardPosition = Position(type=PositionType.Relative)
CardSize = Size(width="100%", height="auto", padding="16px", margin="0", unit_size=UnitSize.PIXELS)
CardStyling = Styling(size=CardSize, position=CardPosition, color=CardColor)
ButtonColor = Color(background_color="#38A169", text_color="#FFFFFF", border_color="#2F855A")
ButtonPosition = Position(type=PositionType.Relative)
ButtonSize = Size(width="auto", height="40px", padding="8px", margin="0", font_size="14px", unit_size=UnitSize.PIXELS)
ButtonStyling = Styling(size=ButtonSize, position=ButtonPosition, color=ButtonColor)
viewComponent: ViewComponent = ViewComponent(name="RealEstateView", description="Display a list of properties with details")
propertyCard: ViewComponent = ViewComponent(name="PropertyCard", description="Display property details", styling=CardStyling)
propertyImage: Image = Image(name="PropertyImage", description="")
viewDetailsButton: Button = Button(name="ViewDetailsButton", description="View property details", label="View Details", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.View, styling=ButtonStyling)
RealEstatePageScreen: Screen = Screen(name="RealEstatePage", description="Welcome to Our Real Estate Agency", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={propertyCard, viewDetailsButton}, is_main_page=True, layout=ScreenLayout)
RealEstateModule: Module = Module(name="RealEstateModule", screens={RealEstatePageScreen})
gui_model: GUIModel = GUIModel(name="RealEstateApp", package="com.example.realestate", versionCode="1", versionName="1.0", description="A web application for browsing real estate properties.", screenCompatibility=True, modules={RealEstateModule})
