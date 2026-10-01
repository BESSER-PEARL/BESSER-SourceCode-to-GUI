from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ImageColor = Color(background_color="", text_color="", border_color="")
ImagePosition = Position(type=PositionType.Relative, top="", left="", right="", bottom="", alignment="center", z_index=0)
ImageSize = Size(width="100%", height="400px", padding="", margin="", font_size="", icon_size="", unit_size=UnitSize.PIXELS)
ImageStyling = Styling(size=ImageSize, position=ImagePosition, color=ImageColor)
ButtonColor = Color(background_color="#EC4899", text_color="#FFFFFF", border_color="#BE185D")
ButtonPosition = Position(type=PositionType.Relative, top="", left="", right="", bottom="", alignment="center", z_index=0)
ButtonSize = Size(width="", height="40px", padding="8px", margin="24px", font_size="14px", icon_size="", unit_size=UnitSize.PIXELS)
ButtonStyling = Styling(size=ButtonSize, position=ButtonPosition, color=ButtonColor)
viewComponent: ViewComponent = ViewComponent(name="FloristPageView", description="Display florist welcome page with image and button")
flowerImage: Image = Image(name="FlowerImage", description="Flower arrangement", styling=ImageStyling)
flowerImage.attributes = {Image_src, Image_alt}
quoteButton: Button = Button(name="GetQuoteButton", description="Get a quote for flower arrangements", label="Get a Quote", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add, styling=ButtonStyling)
quoteButton.attributes = {Button_label}
FloristScreen: Screen = Screen(name="FloristScreen", description="Welcome to our Florist page with beautiful flower arrangements", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={flowerImage, quoteButton}, is_main_page=True, layout=ScreenLayout)
FloristModule: Module = Module(name="FloristModule", screens={FloristScreen})
gui_model: GUIModel = GUIModel(name="FloristApp", package="com.example.floristapp", versionCode="1", versionName="1.0", description="A web application for a florist shop.", screenCompatibility=True, modules={FloristModule})
webPage: WebPage = WebPage()
webPage.attributes = {WebPage_title, WebPage_description, WebPage_subtitle}
