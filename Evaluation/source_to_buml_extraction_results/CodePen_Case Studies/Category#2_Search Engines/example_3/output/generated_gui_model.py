from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#FFFFFF", text_color="#000000", border_color="#CCCCCC")
buttonPosition = Position(type=PositionType.Relative, z_index=0)
buttonSize = Size(width="", height="40", padding="8px", margin="24", font_size="14", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
inputFieldColor = Color(background_color="transparent", text_color="#000000", border_color="#CCCCCC")
inputFieldPosition = Position(type=PositionType.Relative, z_index=0)
inputFieldSize = Size(width="100%", height="40", padding="8px", margin="24", font_size="14", unit_size=UnitSize.PIXELS)
inputFieldStyling = Styling(size=inputFieldSize, position=inputFieldPosition, color=inputFieldColor)
dropdownColor = Color(background_color="transparent", text_color="#000000", border_color="#CCCCCC")
dropdownStyling = Styling(size=inputFieldSize, position=inputFieldPosition, color=dropdownColor)
viewComponent = ViewComponent(name="ImageGalleryView", description="Display a gallery of images with search functionality")
searchButton = Button(name="SearchButton", description="Search for images", label="Search", buttonType=ButtonType.IconButton, actionType=ButtonActionType.Search, styling=buttonStyling)
searchInputField = InputField(name="SearchInput", description="Enter search query", type=ImageGallery_q, styling=inputFieldStyling)
imageTypeDropdown = InputField(name="ImageTypeDropdown", description="Select image type", type=ImageGallery_image_type, styling=dropdownStyling)
imageDataSource = DataSourceElement(name="ImageDataSource", dataSourceClass=Image, fields={Image_largeImageURL, Image_tags})
imageList = DataList(name="ImageList", description="List of images", list_sources={imageDataSource}, styling=inputFieldStyling)
ImageGalleryScreen = Screen(name="ImageGalleryScreen", description="Explore a collection of images", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", is_main_page=True, view_elements={searchButton, searchInputField, imageTypeDropdown, imageList}, layout=ScreenLayout)
ImageGalleryModule = Module(name="ImageGalleryModule", screens={ImageGalleryScreen})
gui_model = GUIModel(name="ImageGalleryApp", package="com.example.imagegallery", versionCode="1", versionName="1.0", description="A web application for exploring images.", screenCompatibility=True, modules={ImageGalleryModule})
