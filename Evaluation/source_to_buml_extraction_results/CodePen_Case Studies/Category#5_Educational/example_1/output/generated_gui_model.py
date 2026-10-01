from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *
from enum import Enum
from dataclasses import dataclass, field
from typing import Set, Optional


class LayoutType(Enum):
    FLEX = "flex"
    GRID = "grid"


class PositionType(Enum):
    RELATIVE = "relative"
    ABSOLUTE = "absolute"


class ButtonType(Enum):
    RAISED = "raised"
    ICON = "icon"


class ButtonActionType(Enum):
    NAVIGATE = "navigate"


class UnitSize(Enum):
    PIXELS = "px"


class JustificationType(Enum):
    CENTER = "center"


@dataclass
class Size:
    height: str
    padding: str
    margin: str
    font_size: str
    unit_size: UnitSize


@dataclass
class Color:
    background_color: str
    text_color: str
    border_color: str


@dataclass
class Position:
    type: PositionType
    z_index: int


@dataclass
class Styling:
    size: Size
    position: Position
    color: Color


@dataclass
class Layout:
    type: LayoutType
    orientation: str
    gap: str
    alignment: JustificationType


@dataclass
class MenuItem:
    label: str


@dataclass
class Menu:
    name: str
    description: str
    menu_items: Set[MenuItem]


@dataclass
class Button:
    name: str
    description: str
    label: str
    button_type: ButtonType
    action_type: ButtonActionType
    styling: Styling


@dataclass
class DataSourceElement:
    name: str
    data_source_class: str
    fields: Set[str]


@dataclass
class DataList:
    name: str
    description: str
    list_sources: Set[DataSourceElement]


@dataclass
class Screen:
    name: str
    description: str
    x_dpi: str
    y_dpi: str
    screen_size: str
    view_elements: Set
    is_main_page: bool
    layout: Layout


@dataclass
class Module:
    name: str
    screens: Set[Screen]


@dataclass
class GUIModel:
    name: str
    package: str
    version_code: str
    version_name: str
    description: str
    screen_compatibility: bool
    modules: Set[Module]


button_color = Color("#007BFF", "#FFFFFF", "#0056b3", border_color="", background_color="", text_color="")
button_position = Position(PositionType.RELATIVE, 10)
button_size = Size("40", "8px", "24", "14", UnitSize.PIXELS)
button_styling = Styling(button_size, button_position, button_color)
screen_layout = Layout(LayoutType.FLEX, "vertical", "15px", JustificationType.CENTER)
header_menu = Menu("HeaderMenu", "Main navigation menu", {MenuItem("Best Sellers", label=""), MenuItem("Selection", label=""), MenuItem("Contact", label="")}, description="", menuItems="", name="")
hero_button = Button("HeroButton", "Shop Now button", "Shop Now", ButtonType.RAISED, ButtonActionType.NAVIGATE, button_styling, label="", actionType="", name="", description="", buttonType="")
best_sellers_list = DataList("BestSellersList", "List of best-selling items", {DataSourceElement("BestSellersDataSource", "Item", {"Item_name", "Item_description"}, dataSourceClass="", fields="", name="")}, list_sources="", description="", name="")
cta_button = Button("CTAButton", "Shop Now button", "Shop Now", ButtonType.RAISED, ButtonActionType.NAVIGATE, button_styling, label="", actionType="", name="", description="", buttonType="")
chairs_list = DataList("ChairsList", "List of available chairs", {DataSourceElement("ChairsDataSource", "Chair", {"Chair_name", "Chair_price"}, dataSourceClass="", fields="", name="")}, list_sources="", description="", name="")
back_to_top_button = Button("BackToTopButton", "Back to top button", "", ButtonType.ICON, ButtonActionType.NAVIGATE, button_styling, label="", actionType="", name="", description="", buttonType="")
footer_contact_info = DataList("FooterContactInfo", "Contact information", {DataSourceElement("ContactInfoDataSource", "ContactInfo", {"ContactInfo_address", "ContactInfo_hours", "ContactInfo_phone", "ContactInfo_email"}, dataSourceClass="", fields="", name="")}, list_sources="", description="", name="")
web_page_screen = Screen("WebPageScreen", "Main webpage screen", "x_dpi", "y_dpi", "Medium", {header_menu, hero_button, best_sellers_list, cta_button, chairs_list, back_to_top_button, footer_contact_info}, True, screen_layout, screen_size="", name="", x_dpi="", view_elements="", description="", y_dpi="")
web_page_module = Module("WebPageModule", {web_page_screen}, name="", screens="")
gui_model = GUIModel("WebPageApp", "com.example.webpageapp", "1", "1.0", "A web application for displaying a webpage with various sections.", True, {web_page_module}, versionCode="", name="", package="", modules="", description="", versionName="")
