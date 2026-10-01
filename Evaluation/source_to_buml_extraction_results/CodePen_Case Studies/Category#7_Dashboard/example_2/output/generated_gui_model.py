from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *
from besser.BUML.metamodel.gui import Screen, ViewContainer, ViewComponent, Menu, MenuItem, Form, InputField, Button, DataList, Image, Layout, Position, Size, Color, Styling, ButtonType, ButtonActionType, InputFieldType, CollectionSourceType, LayoutType, PositionType, JustificationType, UnitSize
from besser.BUML.metamodel.structural import Property

main_screen = Screen(name="MainScreen", is_main_page=True, screen_size="Large", x_dpi="96", y_dpi="96", layout=Layout(orientation="vertical", padding="10px", margin="10px", gap="5px", alignment=JustificationType.Center, wrap=True), view_elements=set(), description="")
page_header = ViewContainer(name="PageHeader", description="Header of the page with logo and menu toggle", layout=Layout(orientation="horizontal", padding="5px", margin="5px", gap="10px", alignment=JustificationType.SpaceBetween, wrap=False), styling=Styling(size=Size(width="100%", height="auto"), position=Position(type=PositionType.Static), color=Color(background_color="#242e42", text_color="#dde9f8", border_color="#1d2636")), view_elements="")
admin_menu = Menu(
    name="AdminMenu",
    description="Admin menu with navigation items",
    menuItems={MenuItem(label="Pages"), MenuItem(label="Users"), MenuItem(label="Trends"), MenuItem(label="Collection"), MenuItem(label="Comments"), MenuItem(label="Appearance"), MenuItem(label="Settings"), MenuItem(label="Options"), MenuItem(label="Charts")},
    styling=Styling(size=Size(width="auto", height="auto"), position=Position(type=PositionType.Static), color=Color(background_color="#FFFFFF", text_color="#000000", border_color="#CCCCCC")),
)
page_content = ViewContainer(name="PageContent", description="Main content area with search and grid", layout=Layout(orientation="vertical", padding="10px", margin="10px", gap="10px", alignment=JustificationType.Center, wrap=True), styling=Styling(size=Size(width="100%", height="auto"), position=Position(type=PositionType.Static), color=Color(background_color="#f0f1f6", text_color="#171616", border_color="#fff")), view_elements="")
search_form = Form(name="SearchForm", description="Form for searching pages", inputFields={InputField(name="SearchInput", description="Search input field", type=InputFieldType.Search, validationRules="", styling=Styling(size=Size(width="100%", height="50px"), position=Position(type=PositionType.Static), color=Color(background_color="#fff", text_color="#000", border_color="#ccc")))})
page_header.view_elements.add(admin_menu)
page_content.view_elements.add(search_form)
main_screen.view_elements.add(page_header)
main_screen.view_elements.add(page_content)
related_class = "PageContent"
attributes = [PageContent_search, PageContent_grid, PageContent_footerMadeBy, PageContent_footerLogo, PageContent_greeting, PageContent_notifications]
