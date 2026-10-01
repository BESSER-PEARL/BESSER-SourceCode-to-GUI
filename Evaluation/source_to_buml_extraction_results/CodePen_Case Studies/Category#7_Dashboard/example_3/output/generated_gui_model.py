from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *
from enum import Enum


class LayoutType(Enum):
    Flex = "flex"
    Grid = "grid"


class PositionType(Enum):
    Sticky = "sticky"
    Relative = "relative"


class UnitSize(Enum):
    PIXELS = "px"
    PERCENT = "%"


class JustificationType(Enum):
    Center = "center"


class Color:

    def __init__(self, background_color, text_color, border_color):
        self.background_color = background_color
        self.text_color = text_color
        self.border_color = border_color


class Position:

    def __init__(self, type, top=None, left=None, right=None, z_index=0):
        self.type = type
        self.top = top
        self.left = left
        self.right = right
        self.z_index = z_index


class Size:

    def __init__(self, width, height, padding="0", margin="0", font_size="16px", unit_size=UnitSize.PIXELS):
        self.width = width
        self.height = height
        self.padding = padding
        self.margin = margin
        self.font_size = font_size
        self.unit_size = unit_size


class Styling:

    def __init__(self, size, position, color):
        self.size = size
        self.position = position
        self.color = color


class Layout:

    def __init__(self, type, orientation="vertical", gap="15px", alignment=JustificationType.Center):
        self.type = type
        self.orientation = orientation
        self.gap = gap
        self.alignment = alignment


class ViewComponent:

    def __init__(self, name, description, styling=None):
        self.name = name
        self.description = description
        self.styling = styling


class MenuItem:

    def __init__(self, label):
        self.label = label


class Menu(ViewComponent):

    def __init__(self, name, description, menuItems, styling=None):
        super().__init__(name, description, styling)
        self.menuItems = menuItems


class DataList(ViewComponent):

    def __init__(self, name, description, list_sources, styling=None):
        super().__init__(name, description, styling)
        self.list_sources = list_sources


class Screen(ViewComponent):

    def __init__(self, name, description, view_elements, layout, is_main_page=True):
        super().__init__(name, description)
        self.view_elements = view_elements
        self.layout = layout
        self.is_main_page = is_main_page


class Module:

    def __init__(self, name, screens):
        self.name = name
        self.screens = screens


class GUIModel:

    def __init__(self, name, package, versionCode, versionName, description, screenCompatibility, modules):
        self.name = name
        self.package = package
        self.versionCode = versionCode
        self.versionName = versionName
        self.description = description
        self.screenCompatibility = screenCompatibility
        self.modules = modules


navbar_color = Color("#343a40", "#ffffff", "#343a40", text_color="", background_color="", border_color="")
navbar_position = Position(PositionType.Sticky, top="0", left="0", right="0", z_index=10)
navbar_size = Size("100%", "56px", font_size="16px")
navbar_styling = Styling(navbar_size, navbar_position, navbar_color)
sidebar_color = Color("#f8f9fa", "#343a40", "#f8f9fa", text_color="", background_color="", border_color="")
sidebar_position = Position(PositionType.Relative, top="0", left="0")
sidebar_size = Size("250px", "100vh", font_size="16px")
sidebar_styling = Styling(sidebar_size, sidebar_position, sidebar_color)
card_size = Size("100%", "auto", padding="20px", margin="10px")
screen_layout = Layout(LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
navbar = Menu("Navbar", "Top navigation bar", [MenuItem("Company name", label=""), MenuItem("Search", label=""), MenuItem("Sign out", label="")], styling=navbar_styling, name="", menuItems="", description="")
sidebar = Menu("Sidebar", "Side navigation menu", [MenuItem("Dashboard", label=""), MenuItem("Orders", label=""), MenuItem("Products", label=""), MenuItem("Customers", label=""), MenuItem("Reports", label=""), MenuItem("Integrations", label=""), MenuItem("Saved Reports", label="")], styling=sidebar_styling, name="", menuItems="", description="")
card1 = ViewComponent("AllProjectsCard", "Card showing all projects", styling=Styling(card_size, None, None), name="", description="")
card2 = ViewComponent("TeamMembersCard", "Card showing team members", styling=Styling(card_size, None, None), name="", description="")
card3 = ViewComponent("TotalBudgetCard", "Card showing total budget", styling=Styling(card_size, None, None), name="", description="")
card4 = ViewComponent("NewCustomersCard", "Card showing new customers", styling=Styling(card_size, None, None), name="", description="")
project_table = DataList("ProjectTable", "Table of ongoing projects", set(), styling=Styling(card_size, None, None), name="", description="", list_sources="")
chart1 = ViewComponent("HouseholdExpenditureChart", "Radar chart for household expenditure", styling=Styling(card_size, None, None), name="", description="")
chart2 = ViewComponent("MonthlyRevenueChart", "Bar chart for monthly revenue", styling=Styling(card_size, None, None), name="", description="")
chart3 = ViewComponent("ExportsOfGoodsChart", "Doughnut chart for exports of goods", styling=Styling(card_size, None, None), name="", description="")
dashboard_screen = Screen("DashboardScreen", "Main dashboard screen with navigation and statistics", {navbar, sidebar, card1, card2, card3, card4, project_table, chart1, chart2, chart3}, layout=screen_layout, view_elements="", y_dpi="", x_dpi="", name="", description="", screen_size="")
dashboard_module = Module("DashboardModule", {dashboard_screen}, name="", screens="")
gui_model = GUIModel("DashboardApp", "com.example.dashboardapp", "1", "1.0", "A web application for managing and viewing dashboard statistics.", True, {dashboard_module}, name="", description="", versionCode="", versionName="", package="", modules="")
