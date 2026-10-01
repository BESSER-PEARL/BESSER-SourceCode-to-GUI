from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *
from besser.BUML.metamodel.structural import Property

headerColor = Color(background_color="#6B46C1", text_color="#FFFFFF", border_color="")
headerPosition = Position(type=PositionType.Relative, top="", left="", right="", bottom="", alignment="", z_index=0)
headerSize = Size(width="100%", height="auto", padding="16px", margin="", font_size="24px", icon_size="", unit_size=UnitSize.PIXELS)
headerStyling = Styling(size=headerSize, position=headerPosition, color=headerColor)
navItemColor = Color(background_color="", text_color="#FFFFFF", border_color="")
navItemPosition = Position(type=PositionType.Inline, top="", left="", right="", bottom="", alignment="", z_index=0)
navItemSize = Size(width="", height="", padding="", margin="", font_size="16px", icon_size="", unit_size=UnitSize.PIXELS)
navItemStyling = Styling(size=navItemSize, position=navItemPosition, color=navItemColor)
mainContentColor = Color(background_color="#F7FAFC", text_color="#2D3748", border_color="")
mainContentPosition = Position(type=PositionType.Relative, top="", left="", right="", bottom="", alignment="", z_index=0)
mainContentSize = Size(width="100%", height="auto", padding="16px", margin="", font_size="18px", icon_size="", unit_size=UnitSize.PIXELS)
mainContentStyling = Styling(size=mainContentSize, position=mainContentPosition, color=mainContentColor)
footerColor = Color(background_color="#6B46C1", text_color="#FFFFFF", border_color="")
footerPosition = Position(type=PositionType.Relative, top="", left="", right="", bottom="", alignment="", z_index=0)
footerSize = Size(width="100%", height="auto", padding="16px", margin="", font_size="16px", icon_size="", unit_size=UnitSize.PIXELS)
footerStyling = Styling(size=footerSize, position=footerPosition, color=footerColor)
headerComponent = ViewComponent(name=Property(name="Header", type=Header), description="Header of the E-commerce Store", styling=headerStyling)
navComponent = Menu(name=Property(name="Navigation", type=Navigation), description="Navigation menu", menuItems={MenuItem(label="Home"), MenuItem(label="Products"), MenuItem(label="About Us"), MenuItem(label="Contact")}, styling=navItemStyling)
mainContentComponent = ViewComponent(name=Property(name="MainContent", type=MainContent), description="Main content area", styling=mainContentStyling)
footerComponent = ViewComponent(name=Property(name="Footer", type=Footer), description="Footer of the E-commerce Store", styling=footerStyling)
ecommerceScreen = Screen(name="ECommerceStoreScreen", description="E-commerce Store main screen", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Large", view_elements={headerComponent, navComponent, mainContentComponent, footerComponent}, is_main_page=True)
ecommerceModule = Module(name="ECommerceModule", screens={ecommerceScreen})
gui_model = GUIModel(name="ECommerceApp", package="com.example.ecommerce", versionCode="1", versionName="1.0", description="E-commerce Store Application", screenCompatibility=True, modules={ecommerceModule})
