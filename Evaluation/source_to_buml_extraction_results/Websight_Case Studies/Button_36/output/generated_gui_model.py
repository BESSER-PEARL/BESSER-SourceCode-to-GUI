from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#007BFF", text_color="#FFFFFF", border_color="#0056b3")
buttonPosition = Position(type=PositionType.Relative, alignment="center", z_index=10)
buttonSize = Size(width="", height="40", padding="8px", margin="24", font_size="14", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
ImagePosition = Position(type=PositionType.Relative, alignment="center")
ImageSize = Size(width="100%", height="64", unit_size=UnitSize.PIXELS)
ImageStyling = Styling(size=ImageSize, position=ImagePosition)
headerImage = Image(name=RealEstatePage_headerImage.name, styling=ImageStyling, description="")
welcomeText = ViewComponent(name=RealEstatePage_title.name, description="Welcome to Our Real Estate Agency")
descriptionText = ViewComponent(name=RealEstatePage_description.name, description="We are a trusted real estate agency with a reputation for excellence. We specialize in finding the perfect home for you. Whether you're looking for a luxury home, a cozy starter home, or a vacation home, we've got you covered.")
featuredListingsButton = Button(name="FeaturedListingsButton", description="View featured listings", label="View Listings", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, styling=buttonStyling)
testimonialsButton = Button(name="TestimonialsButton", description="Read testimonials", label="Read Testimonials", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, styling=buttonStyling)
aboutUsButton = Button(name="AboutUsButton", description="Learn more about us", label="Learn More", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, styling=buttonStyling)
contactUsButton = Button(name="ContactUsButton", description="Contact us", label="Contact Us", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, styling=buttonStyling)
RealEstateScreen = Screen(name="RealEstatePage", description="Real Estate Agency Home Page", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={headerImage, welcomeText, descriptionText, featuredListingsButton, testimonialsButton, aboutUsButton, contactUsButton}, is_main_page=True, layout=ScreenLayout)
RealEstateModule = Module(name="RealEstateModule", screens={RealEstateScreen})
gui_model = GUIModel(name="RealEstateApp", package="com.example.realestate", versionCode="1", versionName="1.0", description="A web application for a real estate agency.", screenCompatibility=True, modules={RealEstateModule})
