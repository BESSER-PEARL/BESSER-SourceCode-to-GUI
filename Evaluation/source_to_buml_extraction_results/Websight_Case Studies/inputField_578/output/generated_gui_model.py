from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#F59E0B", text_color="#FFFFFF", border_color="#D97706")
buttonPosition = Position(type=PositionType.Absolute, top="", left="", right="", bottom="", alignment="center", z_index=10)
buttonSize = Size(width="", height="40", padding="8px", margin="24", font_size="14", icon_size="", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
footerButtonColor = Color(background_color="#F59E0B", text_color="#FFFFFF", border_color="#D97706")
footerButtonPosition = Position(type=PositionType.Relative, top="", left="", right="", bottom="", alignment="", z_index=0)
footerButtonSize = Size(width="", height="40", padding="8px", margin="24", font_size="14", icon_size="", unit_size=UnitSize.PIXELS)
footerButtonStyling = Styling(size=footerButtonSize, position=footerButtonPosition, color=footerButtonColor)
imagePosition = Position(type=PositionType.Relative, top="", left="", right="", bottom="", alignment="", z_index=0)
imageSize = Size(width="100%", height="auto", padding="0", margin="0", font_size="", icon_size="", unit_size=UnitSize.PIXELS)
imageStyling = Styling(size=imageSize, position=imagePosition, color=None)
textPosition = Position(type=PositionType.Relative, top="", left="", right="", bottom="", alignment="", z_index=0)
textSize = Size(width="", height="", padding="0", margin="0", font_size="16", icon_size="", unit_size=UnitSize.PIXELS)
textStyling = Styling(size=textSize, position=textPosition, color=None)
viewComponent: ViewComponent = ViewComponent(name="NonProfitPage", description="Non-profit organization page with mission and volunteer information")
backgroundImage: Image = Image(name="BackgroundImage", styling=imageStyling, description="")
backgroundImage.src = Image_src
donateButton: Button = Button(name="DonateButton", description="Donate Now", label="Donate Now", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, styling=buttonStyling)
missionSection: ViewComponent = ViewComponent(name="MissionSection", description="Our Mission", styling=textStyling)
missionSection.title = Section_title
missionSection.content = Section_content
volunteerSection: ViewComponent = ViewComponent(name="VolunteerSection", description="How to Volunteer", styling=textStyling)
volunteerSection.title = Section_title
volunteerSection.content = Section_content
footer: ViewComponent = ViewComponent(name="Footer", description="Footer with social media and newsletter", styling=textStyling)
footer.socialMediaLinks = Footer_socialMediaLinks
footer.newsletterEmail = Footer_newsletterEmail
signUpButton: Button = Button(name="SignUpButton", description="Sign up for newsletter", label="Sign Up", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, styling=footerButtonStyling)
opportunitiesButton: Button = Button(name="OpportunitiesButton", description="Check out volunteer opportunities", label="Opportunities", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, styling=footerButtonStyling)
NonProfitScreen: Screen = Screen(name="NonProfitScreen", description="Non-profit organization page", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={backgroundImage, donateButton, missionSection, volunteerSection, footer, signUpButton, opportunitiesButton}, is_main_page=True, layout=ScreenLayout)
NonProfitModule: Module = Module(name="NonProfitModule", screens={NonProfitScreen})
gui_model: GUIModel = GUIModel(name="NonProfitApp", package="com.example.nonprofit", versionCode="1", versionName="1.0", description="A web application for a non-profit organization.", screenCompatibility=True, modules={NonProfitModule})
