from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#007BFF", text_color="#FFFFFF", border_color="#0056b3")
buttonPosition = Position(type=PositionType.Relative, alignment="", z_index=10)
buttonSize = Size(width="", height="40", padding="8px", margin="24", font_size="14", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
viewComponent = ViewComponent(name="ConstructionCompanyView", description="Welcome page for the construction company")
menuItems = {MenuItem(label="Home"), MenuItem(label="Services"), MenuItem(label="Projects"), MenuItem(label="About Us"), MenuItem(label="Contact")}
navigationMenu = Menu(name="MainMenu", description="Main navigation menu", menuItems=menuItems)
heroTitle = InputField(name=HeroSection_title.name, description="Main title", type="Text", styling=None)
heroDescription = InputField(name=HeroSection_description.name, description="Description", type="Text", styling=None)
heroImage = Image(name=Image_src.name, description="")
serviceComponent = ViewComponent(name=Service_name.name, description="Service 1")
testimonialComponent = ViewComponent(name=Testimonial_content.name, description="Testimonial 1")
teamMemberComponent = ViewComponent(name=TeamMember_name.name, description="Team Member 1")
contactForm = Form(name="ContactForm", description="Contact us form", inputFields={InputField(name=ContactForm_name.name, description="Name field", type="Text"), InputField(name=ContactForm_email.name, description="Email field", type="Email"), InputField(name=ContactForm_message.name, description="Message field", type="Text")})
submitButton = Button(name="SubmitButton", description="Submit the form", label="Submit", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Submit, styling=buttonStyling)
footerLink = Button(name="FooterLink", description="Safety Certifications", label="Safety Certifications", buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate, styling=None)
ConstructionScreen = Screen(name="ConstructionScreen", description="Main page of the construction company", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Large", view_elements={navigationMenu, heroTitle, heroDescription, heroImage, serviceComponent, testimonialComponent, teamMemberComponent, contactForm, submitButton, footerLink}, is_main_page=True, layout=ScreenLayout)
ConstructionModule = Module(name="ConstructionModule", screens={ConstructionScreen})
gui_model = GUIModel(name="ConstructionApp", package="com.example.constructionapp", versionCode="1", versionName="1.0", description="A web application for a construction company.", screenCompatibility=True, modules={ConstructionModule})
