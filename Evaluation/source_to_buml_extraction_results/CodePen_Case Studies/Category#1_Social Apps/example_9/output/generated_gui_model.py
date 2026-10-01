from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="20px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#FFFFFF", text_color="rgba(0,0,0,.6)", border_color="rgba(0,0,0,.1)")
buttonPosition = Position(type=PositionType.Relative, z_index=0)
buttonSize = Size(width="200px", height="40px", padding="8px", margin="20px 0", font_size="14px", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
twitterButton = Button(name="TwitterButton", description="Twitter link", label="Twitter", buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate, styling=buttonStyling)
facebookButton = Button(name="FacebookButton", description="Facebook link", label="Facebook", buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate, styling=buttonStyling)
googlePlusButton = Button(name="GooglePlusButton", description="Google Plus link", label="Google +", buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate, styling=buttonStyling)
pinterestButton = Button(name="PinterestButton", description="Pinterest link", label="Pinterest", buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate, styling=buttonStyling)
dribbbleButton = Button(name="DribbbleButton", description="Dribbble link", label="Dribbble", buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate, styling=buttonStyling)
instagramButton = Button(name="InstagramButton", description="Instagram link", label="Instagram", buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate, styling=buttonStyling)
SocialSectionScreen = Screen(name="SocialSection", description="Screen with social media links", x_dpi="160", y_dpi="160", screen_size="Medium", view_elements={twitterButton, facebookButton, googlePlusButton, pinterestButton, dribbbleButton, instagramButton}, is_main_page=True, layout=ScreenLayout)
SocialModule = Module(name="SocialModule", screens={SocialSectionScreen})
gui_model = GUIModel(name="SocialMediaApp", package="com.example.socialmedia", versionCode="1", versionName="1.0", description="An application with social media links", screenCompatibility=True, modules={SocialModule})
