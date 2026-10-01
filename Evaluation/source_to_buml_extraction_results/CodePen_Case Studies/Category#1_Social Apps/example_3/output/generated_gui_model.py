from besser.BUML.notations.source_code_to_gui.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#0B5073", text_color="#FFFFFF", border_color="#0B5073")
buttonPosition = Position(type=PositionType.Relative, top="", left="", right="", bottom="", alignment="", z_index=0)
buttonSize = Size(width="240px", height="40px", padding="12px 24px", margin="24px", font_size="17px", icon_size="", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
ImageColor = Color(background_color="#FFFFFF", text_color="#000000", border_color="#FFFFFF")
imagePosition = Position(type=PositionType.Relative, top="", left="", right="", bottom="", alignment="", z_index=0)
imageSize = Size(width="530px", height="auto", padding="0", margin="0", font_size="", icon_size="", unit_size=UnitSize.PIXELS)
imageStyling = Styling(size=imageSize, position=imagePosition, color=ImageColor)
viewComponent = ViewComponent(name="EmailTemplateView", description="Display an email template with various components")
header = ViewComponent(name="Header", description=EmailTemplate_header, styling=None)
subheader = ViewComponent(name="Subheader", description=EmailTemplate_subheader, styling=None)
heroImage = Image(name="HeroImage", description=Image_alt, styling=imageStyling)
paragraph = ViewComponent(name="Paragraph", description=EmailTemplate_paragraph, styling=None)
exploreButton = Button(name="ExploreButton", description=Button_text, label="Explore templates", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, targetScreen=None, styling=buttonStyling)
socialIcons = [Image(name="FacebookIcon", description=SocialIcon_platform, styling=None), Image(name="TwitterIcon", description=SocialIcon_platform, styling=None), Image(name="GooglePlusIcon", description=SocialIcon_platform, styling=None), Image(name="InstagramIcon", description=SocialIcon_platform, styling=None)]
footer = ViewComponent(name="Footer", description=EmailTemplate_footer, styling=None)
EmailTemplateScreen = Screen(name="EmailTemplateScreen", description="Responsive email template screen", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={header, subheader, heroImage, paragraph, exploreButton, *socialIcons, footer}, is_main_page=True, layout=ScreenLayout)
EmailTemplateModule = Module(name="EmailTemplateModule", screens={EmailTemplateScreen})
gui_model = GUIModel(name="EmailTemplateApp", package="com.example.emailtemplate", versionCode="1", versionName="1.0", description="A responsive email template application.", screenCompatibility=True, modules={EmailTemplateModule})
