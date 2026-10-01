from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *
# Define styling and layout properties
navButtonStyling = Styling(
    size=Size(width="100px", height="40px", padding="5px", margin="5px", font_size="14px", icon_size="20px", unit_size=UnitSize.PIXELS),
    position=Position(type=PositionType.Relative, top="10px", left="10px", alignment="left", z_index=1),
    color=Color(background_color="#FFFFFF", text_color="#727272", border_color="#727272")
)

heartButtonStyling = Styling(
    size=Size(width="40px", height="40px", padding="5px", margin="5px", icon_size="20px", unit_size=UnitSize.PIXELS),
    position=Position(type=PositionType.Relative, top="10px", left="120px", alignment="left", z_index=1),
    color=Color(background_color="#FFFFFF", text_color="#727272", border_color="#727272")
)

photoImageStyling = Styling(
    size=Size(width="236px", height="236px", padding="10px", margin="10px", unit_size=UnitSize.PIXELS),
    position=Position(type=PositionType.Relative, top="60px", left="10px", alignment="center", z_index=0)
)

descriptionTitleStyling = Styling(
    size=Size(padding="5px", margin="5px", font_size="24px", unit_size=UnitSize.PIXELS),
    position=Position(type=PositionType.Relative, top="310px", left="10px", alignment="left", z_index=0),
    color=Color(text_color="#000000")
)

descriptionSubtitleStyling = Styling(
    size=Size(padding="5px", margin="5px", font_size="18px", unit_size=UnitSize.PIXELS),
    position=Position(type=PositionType.Relative, top="340px", left="10px", alignment="left", z_index=0),
    color=Color(text_color="#000000")
)

descriptionPriceStyling = Styling(
    size=Size(padding="5px", margin="5px", font_size="32px", unit_size=UnitSize.PIXELS),
    position=Position(type=PositionType.Relative, top="370px", left="10px", alignment="left", z_index=0),
    color=Color(text_color="#000000")
)

descriptionTextStyling = Styling(
    size=Size(padding="5px", margin="5px", font_size="16px", unit_size=UnitSize.PIXELS),
    position=Position(type=PositionType.Relative, top="410px", left="10px", alignment="left", z_index=0),
    color=Color(text_color="#000000")
)

addToCartButtonStyling = Styling(
    size=Size(width="120px", height="40px", padding="5px", margin="5px", font_size="16px", unit_size=UnitSize.PIXELS),
    position=Position(type=PositionType.Relative, top="460px", left="10px", alignment="left", z_index=0),
    color=Color(background_color="#ffcc00", text_color="#3d3d3d", border_color="#000000")
)

wishlistButtonStyling = Styling(
    size=Size(width="120px", height="40px", padding="5px", margin="5px", font_size="16px", unit_size=UnitSize.PIXELS),
    position=Position(type=PositionType.Relative, top="460px", left="140px", alignment="left", z_index=0),
    color=Color(background_color="#ffcc00", text_color="#3d3d3d", border_color="#000000")
)

# Define view components
navButton = Button(
    name="BackToAllPlantsButton",
    description="Navigate back to all plants",
    label="Back to all Plants",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Navigate,
    styling=navButtonStyling
)

heartButton = Button(
    name="HeartButton",
    description="Heart icon",
    label="",
    buttonType=ButtonType.IconButton,
    actionType=ButtonActionType.None,
    styling=heartButtonStyling
)

photoImage = Image(
    name="PlantPhoto",
    description="Image of the plant",
    styling=photoImageStyling
)

descriptionTitle = ViewComponent(
    name="DescriptionTitle",
    description="Title of the plant",
    styling=descriptionTitleStyling,
    property=Description_title
)

descriptionSubtitle = ViewComponent(
    name="DescriptionSubtitle",
    description="Subtitle of the plant",
    styling=descriptionSubtitleStyling,
    property=Description_subtitle
)

descriptionPrice = ViewComponent(
    name="DescriptionPrice",
    description="Price of the plant",
    styling=descriptionPriceStyling,
    property=Description_price
)

descriptionText = ViewComponent(
    name="DescriptionText",
    description="Description of the plant",
    styling=descriptionTextStyling,
    property=Description_description
)

addToCartButton = Button(
    name="AddToCartButton",
    description="Add the plant to cart",
    label="Add to Cart",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Add,
    styling=addToCartButtonStyling
)

wishlistButton = Button(
    name="WishlistButton",
    description="Add the plant to wishlist",
    label="Wishlist",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Add,
    styling=wishlistButtonStyling
)

# Define screen
PlantDetailScreen = Screen(
    name="PlantDetailScreen",
    description="Screen displaying details of a plant",
    x_dpi="x_dpi",
    y_dpi="y_dpi",
    screen_size="Medium",
    view_elements={navButton, heartButton, photoImage, descriptionTitle, descriptionSubtitle, descriptionPrice, descriptionText, addToCartButton, wishlistButton},
    is_main_page=True
)

# Define module
PlantModule = Module(
    name="PlantModule",
    screens={PlantDetailScreen}
)

# Define application
gui_model = GUIModel(
    name="PlantApp",
    package="com.example.plantapp",
    versionCode="1",
    versionName="1.0",
    description="An application for managing plant details",
    screenCompatibility=True,
    modules={PlantModule}
)
