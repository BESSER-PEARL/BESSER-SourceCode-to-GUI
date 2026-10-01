from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *

ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ListColor = Color(background_color="#FFFFFF", text_color="#343A40", border_color="#CED4DA")
ListPosition = Position(type=PositionType.Relative, top="200px", left="20px")
listSize = Size(width="100%", height="auto", padding="10px")
ListStyling = Styling(size=listSize, position=ListPosition, color=ListColor)
PaginationColor = Color(background_color="#FFFFFF", text_color="#343A40", border_color="#CED4DA")
PaginationPosition = Position(type=PositionType.Relative)
paginationSize = Size(width="100%", height="auto", padding="10px")
PaginationStyling = Styling(size=paginationSize, position=PaginationPosition, color=PaginationColor)
viewComponent = ViewComponent(name="ContentsListView", description="Display a list of contents with pagination")
datasource_contents = DataSourceElement(name="ContentsDataSource", dataSourceClass=Contents, fields=[Contents_contentName, Contents_category, Contents_registered, Contents_user])
contentsList = DataList(name="ContentsList", description="A list of contents", list_sources={datasource_contents}, styling=ListStyling)
pagination = DataList(name="Pagination", description="Pagination controls", list_sources={}, styling=PaginationStyling)
ContentsScreen = Screen(name="ContentsScreen", description="Explore a collection of contents", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={contentsList, pagination}, layout=ScreenLayout, is_main_page=True)
MyModule = Module(name="ContentsModule", screens={ContentsScreen})
gui_model = GUIModel(name="ContentsApp", package="com.example.contentsapp", versionCode="1", versionName="1.0", description="A web application for managing contents.", screenCompatibility=True, modules={MyModule})
