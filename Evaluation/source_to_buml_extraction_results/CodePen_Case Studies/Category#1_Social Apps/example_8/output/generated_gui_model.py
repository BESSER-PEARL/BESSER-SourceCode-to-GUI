from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
RadioButtonColor = Color(background_color="#1d1d42", text_color="#ffffff", border_color="rgba(255, 255, 255, 0.1)")
RadioButtonPosition = Position(type=PositionType.Relative)
RadioButtonSize = Size(width="250px", height="40px", padding="20px 60px", margin="15px 0", font_size="18px", unit_size=UnitSize.PIXELS)
RadioButtonStyling = Styling(size=RadioButtonSize, position=RadioButtonPosition, color=RadioButtonColor)
viewComponent = ViewComponent(name="SocialMediaRadioView", description="Select your preferred social media platform")
instagramRadioItem = Button(name="InstagramRadioButton", description="Select Instagram", label="INSTAGRAM", buttonType=ButtonType.ToggleButtons, actionType=ButtonActionType.Select, styling=RadioButtonStyling)
twitterRadioItem = Button(name="TwitterRadioButton", description="Select Twitter", label="TWITTER", buttonType=ButtonType.ToggleButtons, actionType=ButtonActionType.Select, styling=RadioButtonStyling)
linkedinRadioItem = Button(name="LinkedInRadioButton", description="Select LinkedIn", label="LINKEDIN", buttonType=ButtonType.ToggleButtons, actionType=ButtonActionType.Select, styling=RadioButtonStyling)
RadioSectionScreen = Screen(name="SocialMediaSelectionScreen", description="Choose your frequently used social media platform", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={instagramRadioItem, twitterRadioItem, linkedinRadioItem}, layout=ScreenLayout, is_main_page=True)
MyModule = Module(name="SocialMediaModule", screens={RadioSectionScreen})
gui_model = GUIModel(name="SocialMediaApp", package="com.example.socialmedia", versionCode="1", versionName="1.0", description="An application to select your preferred social media platform.", screenCompatibility=True, modules={MyModule})
