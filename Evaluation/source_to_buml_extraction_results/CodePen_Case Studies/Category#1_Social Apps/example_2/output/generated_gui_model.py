from besser.BUML.notations.sourceCode_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *
# GUI model definition

# Styling definitions
ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)

# Colors
BackgroundColor = Color(background_color=EmailTemplate_backgroundColor, text_color=EmailTemplate_textColor, border_color="")
ButtonColor = Color(background_color=Button_backgroundColor, text_color=Button_textColor, border_color="")
LineColor = Color(background_color="", text_color="", border_color=Line_color)

# Sizes
ButtonSize = Size(width="240px", height="40px", padding="12px 24px", margin="25px 0 5px 0", font_size="17px", icon_size="", unit_size=UnitSize.PIXELS)
ImageSize = Size(width="340px", height="auto", padding="0", margin="0", font_size="", icon_size="", unit_size=UnitSize.PIXELS)

# Positions
ButtonPosition = Position(type=PositionType.Relative, top="", left="", right="", bottom="", alignment="", z_index=0)
ImagePosition = Position(type=PositionType.Relative, top="0px", left="", right="", bottom="", alignment="", z_index=0)

# Styling
ButtonStyling = Styling(size=ButtonSize, position=ButtonPosition, color=ButtonColor)
ImageStyling = Styling(size=ImageSize, position=ImagePosition, color=BackgroundColor)
LineStyling = Styling(size=Size(width="100%", height="1px", padding="0", margin="30px 0 0 0", font_size="", icon_size="", unit_size=UnitSize.PIXELS), position=Position(type=PositionType.Relative), color=LineColor)

# ViewComponent definition
viewComponent: ViewComponent = ViewComponent(name="EmailTemplateView", description="Responsive HTML email template")

# Elements for Email Template Screen

# Logo
logoImage: Image = Image(name="LogoImage", description="Logo", styling=ImageStyling)

# Hero Image
heroImage: Image = Image(name="HeroImage", description="Hero Image", styling=ImageStyling)

# SupHeader
supHeader: ViewComponent = ViewComponent(name="SupHeader", description="Introducing", styling=Styling(size=Size(width="87.5%", height="", padding="27px 0 0 0", margin="0", font_size="14px", icon_size="", unit_size=UnitSize.PIXELS), position=Position(type=PositionType.Relative), color=BackgroundColor))

# Header
header: ViewComponent = ViewComponent(name="Header", description="Responsive HTML email templates", styling=Styling(size=Size(width="87.5%", height="", padding="5px 0 0 0", margin="0", font_size="24px", icon_size="", unit_size=UnitSize.PIXELS), position=Position(type=PositionType.Relative), color=BackgroundColor))

# Paragraph
paragraph: ViewComponent = ViewComponent(name="Paragraph", description="More than 50% of total email opens occurred on a mobile device � a mobile-friendly design is a must for email campaigns.", styling=Styling(size=Size(width="87.5%", height="", padding="15px 0 0 0", margin="0", font_size="17px", icon_size="", unit_size=UnitSize.PIXELS), position=Position(type=PositionType.Relative), color=BackgroundColor))

# Button
viewButton: Button = Button(name="ViewButton", description="View on GitHub", label="View on GitHub", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, styling=ButtonStyling)

# Line
line: ViewComponent = ViewComponent(name="Line", description="Line separator", styling=LineStyling)

# Footer
footer: ViewComponent = ViewComponent(name="Footer", description="This email template was sent to you because we want to make the world a better place. You could change your subscription settings anytime.", styling=Styling(size=Size(width="87.5%", height="", padding="10px 0 20px 0", margin="0", font_size="13px", icon_size="", unit_size=UnitSize.PIXELS), position=Position(type=PositionType.Relative), color=Color(background_color="", text_color=Footer_textColor, border_color="")))

# Email Template Screen definition
EmailTemplateScreen: Screen = Screen(name="EmailTemplateScreen", description="Responsive HTML email template screen",
                                     x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", is_main_page=True,
                                     view_elements={logoImage, heroImage, supHeader, header, paragraph, viewButton, line, footer}, layout=ScreenLayout)

# Module definition
EmailModule: Module = Module(name="EmailModule", screens={EmailTemplateScreen})

# Application definition
gui_model: GUIModel = GUIModel(name="EmailTemplateApp", package="com.example.emailtemplate", versionCode="1",
                               versionName="1.0", description="Responsive HTML email template application.",
                               screenCompatibility=True, modules={EmailModule})

# Class and Attributes
# This page is related to the EmailTemplate class.
# Attributes: backgroundColor, textColor, width, height
