from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *
from enum import Enum


class LayoutType(Enum):
    FLEX = "flex"
    GRID = "grid"


class PositionType(Enum):
    RELATIVE = "relative"
    ABSOLUTE = "absolute"


class UnitSize(Enum):
    PIXELS = "px"
    PERCENT = "%"


class JustificationType(Enum):
    CENTER = "center"
    LEFT = "left"


class Layout:

    def __init__(self, type, orientation, gap, alignment):
        self.type = type
        self.orientation = orientation
        self.gap = gap
        self.alignment = alignment


class Color:

    def __init__(self, background_color, text_color, border_color):
        self.background_color = background_color
        self.text_color = text_color
        self.border_color = border_color


class Position:

    def __init__(self, type, z_index):
        self.type = type
        self.z_index = z_index


class Size:

    def __init__(self, height, padding, margin, font_size, unit_size):
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


screen_layout = Layout(type=LayoutType.FLEX, orientation="vertical", gap="15px", alignment=JustificationType.CENTER)
button_color = Color(background_color="#007BFF", text_color="#FFFFFF", border_color="#0056b3")
button_position = Position(type=PositionType.RELATIVE, z_index=10)
button_size = Size(height="40px", padding="8px", margin="24px", font_size="14px", unit_size=UnitSize.PIXELS)
button_styling = Styling(size=button_size, position=button_position, color=button_color)


class ViewComponent:

    def __init__(self, name, description):
        self.name = name
        self.description = description


view_component = ViewComponent(name="UserDashboardView", description="Display user dashboard with navigation and stats")


class MenuItem:

    def __init__(self, label):
        self.label = label


analytics_menu_item = MenuItem(label="Analytics")
projects_menu_item = MenuItem(label="Projects")
teams_menu_item = MenuItem(label="Teams")
users_menu_item = MenuItem(label="Users")
time_menu_item = MenuItem(label="Time")


class Menu:

    def __init__(self, name, description, menu_items):
        self.name = name
        self.description = description
        self.menu_items = menu_items


main_menu = Menu(name="MainMenu", description="Main navigation menu", menuItems="")


class InputField:

    def __init__(self, name, description, type, styling, label):
        self.name = name
        self.description = description
        self.type = type
        self.styling = styling
        self.label = label


header_greeting = InputField(name="HeaderGreeting", description="Greeting message", type="Text", styling=None)
search_input = InputField(name="SearchInput", description="Search input field", type="Search", styling=None)
weekly_sprint_section = ViewComponent(name="WeeklySprintSection", description="Weekly sprint stats")
weekly_tasks_section = ViewComponent(name="WeeklyTasksSection", description="Weekly tasks stats")
weekly_prs_section = ViewComponent(name="WeeklyPRsSection", description="Weekly PRs stats")
weekly_commits_section = ViewComponent(name="WeeklyCommitsSection", description="Weekly commits stats")
weekly_issues_section = ViewComponent(name="WeeklyIssuesSection", description="Weekly issues stats")


class Screen:

    def __init__(self, name, description, x_dpi, y_dpi, screen_size, view_elements, is_main_page, layout):
        self.name = name
        self.description = description
        self.x_dpi = x_dpi
        self.y_dpi = y_dpi
        self.screen_size = screen_size
        self.view_elements = view_elements
        self.is_main_page = is_main_page
        self.layout = layout


user_dashboard_screen = Screen(name="UserDashboardScreen", description="User dashboard with navigation and stats", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={main_menu, header_greeting, search_input, weekly_sprint_section, weekly_tasks_section, weekly_prs_section, weekly_commits_section, weekly_issues_section}, is_main_page=True, layout=screen_layout)


class Module:

    def __init__(self, name, screens):
        self.name = name
        self.screens = screens


user_dashboard_module = Module(name="UserDashboardModule", screens={user_dashboard_screen})


class GUIModel:

    def __init__(self, name, package, version_code, version_name, description, screen_compatibility, modules):
        self.name = name
        self.package = package
        self.version_code = version_code
        self.version_name = version_name
        self.description = description
        self.screen_compatibility = screen_compatibility
        self.modules = modules


gui_model = GUIModel(name="UserDashboardApp", package="com.example.userdashboard", description="A user dashboard application with navigation and stats.", modules={user_dashboard_module}, versionCode="", versionName="")
