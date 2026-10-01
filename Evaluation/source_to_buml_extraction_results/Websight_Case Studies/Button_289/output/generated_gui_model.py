from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
TitleColor = Color(background_color="", text_color="#1F2937", border_color="")
TitlePosition = Position(type=PositionType.Relative, alignment="center")
TitleSize = Size(width="", height="", padding="10px", margin="20px", font_size="40px", unit_size=UnitSize.PIXELS)
TitleStyling = Styling(size=TitleSize, position=TitlePosition, color=TitleColor)
SubtitleColor = Color(background_color="", text_color="#1F2937", border_color="")
SubtitlePosition = Position(type=PositionType.Relative, alignment="center")
SubtitleSize = Size(width="", height="", padding="10px", margin="10px", font_size="20px", unit_size=UnitSize.PIXELS)
SubtitleStyling = Styling(size=SubtitleSize, position=SubtitlePosition, color=SubtitleColor)
FilterContainerColor = Color(background_color="#FFFFFF", text_color="#1F2937", border_color="")
FilterContainerPosition = Position(type=PositionType.Relative)
FilterContainerSize = Size(width="100%", height="auto", padding="20px", margin="10px", unit_size=UnitSize.PIXELS)
FilterContainerStyling = Styling(size=FilterContainerSize, position=FilterContainerPosition, color=FilterContainerColor)
ButtonColor = Color(background_color="#6B7280", text_color="#FFFFFF", border_color="")
ButtonPosition = Position(type=PositionType.Relative, alignment="center")
ButtonSize = Size(width="", height="40px", padding="10px", margin="20px", font_size="16px", unit_size=UnitSize.PIXELS)
ButtonStyling = Styling(size=ButtonSize, position=ButtonPosition, color=ButtonColor)
viewComponent: ViewComponent = ViewComponent(name="FoodDeliveryPageView", description="Display the main page of the food delivery service")
title: ViewComponent = ViewComponent(name="Title", description="Main title of the page", styling=TitleStyling)
subtitle: ViewComponent = ViewComponent(name="Subtitle", description="Subtitle of the page", styling=SubtitleStyling)
dietaryPreferencesFilter: ViewComponent = ViewComponent(name="DietaryPreferencesFilter", description="Filter by dietary preferences", styling=FilterContainerStyling)
locationFilter: ViewComponent = ViewComponent(name="LocationFilter", description="Filter by location", styling=FilterContainerStyling)
foodSection: ViewComponent = ViewComponent(name="FoodSection", description="Section displaying food items", styling=FilterContainerStyling)
orderNowButton: Button = Button(name="OrderNowButton", description="Button to place an order", label="Order Now", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, styling=ButtonStyling)
FoodDeliveryPageScreen: Screen = Screen(
    name="FoodDeliveryPage", description="Main page for the food delivery service", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={Property(name="title", type=title), Property(name="subtitle", type=subtitle), Property(name="dietaryPreferencesFilter", type=dietaryPreferencesFilter), Property(name="locationFilter", type=locationFilter), Property(name="foodSection", type=foodSection), Property(name="orderNowButton", type=orderNowButton)}, is_main_page=True, layout=ScreenLayout
)
FoodDeliveryModule: Module = Module(name="FoodDeliveryModule", screens={FoodDeliveryPageScreen})
gui_model: GUIModel = GUIModel(name="FoodDeliveryApp", package="com.example.fooddelivery", versionCode="1", versionName="1.0", description="A web application for food delivery service.", screenCompatibility=True, modules={FoodDeliveryModule})
