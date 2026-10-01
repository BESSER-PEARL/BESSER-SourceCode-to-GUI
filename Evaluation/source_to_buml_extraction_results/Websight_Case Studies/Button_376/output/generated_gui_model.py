from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

headerColor = Color(background_color="#FFFFFF", text_color="#000000", border_color="")
headerPosition = Position(type=PositionType.Relative, alignment="center", z_index=0)
headerSize = Size(width="100%", height="auto", padding="16px", font_size="16px", unit_size=UnitSize.PIXELS)
headerStyling = Styling(size=headerSize, position=headerPosition, color=headerColor)
navColor = Color(background_color="", text_color="#4CAF50", border_color="")
navPosition = Position(type=PositionType.Relative, alignment="center", z_index=0)
navSize = Size(width="auto", height="auto", padding="8px", font_size="14px", unit_size=UnitSize.PIXELS)
navStyling = Styling(size=navSize, position=navPosition, color=navColor)
mainColor = Color(background_color="#F7FAFC", text_color="#000000", border_color="")
mainPosition = Position(type=PositionType.Relative, alignment="center", z_index=0)
mainSize = Size(width="100%", height="auto", padding="16px", font_size="16px", unit_size=UnitSize.PIXELS)
mainStyling = Styling(size=mainSize, position=mainPosition, color=mainColor)
buttonColor = Color(background_color="#4CAF50", text_color="#FFFFFF", border_color="")
buttonPosition = Position(type=PositionType.Relative, alignment="center", z_index=0)
buttonSize = Size(width="auto", height="40px", padding="8px", font_size="14px", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=buttonColor)
logoImage = Image(name="LogoImage", description="Logo of the organization", styling=None)
logoImage.src = "logo.png"
logoImage.alt = "Organization Logo"
homeMenuItem = MenuItem(label="Home")
aboutMenuItem = MenuItem(label="About")
contactMenuItem = MenuItem(label="Contact")
navMenu = Menu(name="NavigationMenu", description="Main navigation menu", menuItems={homeMenuItem, aboutMenuItem, contactMenuItem}, styling=navStyling)
header = ViewContainer(name="Header", description="Header of the page", layout=None, styling=headerStyling, view_elements={logoImage, navMenu})
welcomeText = Paragraph(name="WelcomeText", description="Welcome message", styling=None)
welcomeText.text = "Welcome to our non-profit organization!"
donateButton = Button(name="DonateButton", description="Donate now button", label="Donate Now", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add, styling=buttonStyling)
impactImage = Image(name="ImpactImage", description="Image showing impact", styling=None)
impactImage.src = "impact.png"
impactImage.alt = "Impact Image"
impactText = Paragraph(name="ImpactText", description="Text about impact", styling=None)
impactText.text = "Our impact is significant and growing."
storyImage = Image(name="StoryImage", description="Image showing story", styling=None)
storyImage.src = "story.png"
storyImage.alt = "Story Image"
storyText = Paragraph(name="StoryText", description="Text about stories", styling=None)
storyText.text = "Read our inspiring stories."
impactSection = ViewContainer(name="ImpactSection", description="Section about impact", layout=None, styling=None, view_elements={impactImage, impactText})
storySection = ViewContainer(name="StorySection", description="Section about stories", layout=None, styling=None, view_elements={storyImage, storyText})
mainContent = ViewContainer(name="MainContent", description="Main content of the page", layout=None, styling=mainStyling, view_elements={welcomeText, donateButton, impactSection, storySection})
homeScreen = Screen(name="HomeScreen", description="Home page of the non-profit organization", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", is_main_page=True, layout=None, view_elements={header, mainContent})
mainModule = Module(name="MainModule", screens={homeScreen})
gui_model = GUIModel(name="NonProfitApp", package="com.example.nonprofitapp", versionCode="1", versionName="1.0", description="A web application for a non-profit organization", screenCompatibility=True, modules={mainModule})
