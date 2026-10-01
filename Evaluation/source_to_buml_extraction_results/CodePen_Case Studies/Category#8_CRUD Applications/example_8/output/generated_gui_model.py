from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *
from enum import Enum


class LayoutType(Enum):
    Flex = "flex"


class PositionType(Enum):
    Relative = "relative"


class ButtonType(Enum):
    RaisedButton = "raised"


class ButtonActionType(Enum):
    Add = "add"
    Delete = "delete"


class UnitSize(Enum):
    PIXELS = "px"


class JustificationType(Enum):
    Center = "center"


class Layout:

    def __init__(self, type, orientation, gap, alignment):
        self.type = type
        self.orientation = orientation
        self.gap = gap
        self.alignment = alignment


class Size:

    def __init__(self, height=None, padding=None, margin=None, font_size=None, unit_size=None, width=None):
        self.height = height
        self.padding = padding
        self.margin = margin
        self.font_size = font_size
        self.unit_size = unit_size
        self.width = width


class Position:

    def __init__(self, type, z_index=None, top=None, left=None):
        self.type = type
        self.z_index = z_index
        self.top = top
        self.left = left


class Color:

    def __init__(self, background_color, text_color, border_color):
        self.background_color = background_color
        self.text_color = text_color
        self.border_color = border_color


class Styling:

    def __init__(self, size, position, color):
        self.size = size
        self.position = position
        self.color = color


class ViewComponent:

    def __init__(self, name, description):
        self.name = name
        self.description = description


class Button(ViewComponent):

    def __init__(self, name, description, label, buttonType, actionType, styling):
        super().__init__(name, description)
        self.label = label
        self.buttonType = buttonType
        self.actionType = actionType
        self.styling = styling


class DataSourceElement:

    def __init__(self, name, dataSourceClass, fields):
        self.name = name
        self.dataSourceClass = dataSourceClass
        self.fields = fields


class DataList(ViewComponent):

    def __init__(self, name, description, list_sources, styling):
        super().__init__(name, description)
        self.list_sources = list_sources
        self.styling = styling


class Screen:

    def __init__(self, name, description, x_dpi, y_dpi, screen_size, is_main_page, view_elements, layout):
        self.name = name
        self.description = description
        self.x_dpi = x_dpi
        self.y_dpi = y_dpi
        self.screen_size = screen_size
        self.is_main_page = is_main_page
        self.view_elements = view_elements
        self.layout = layout


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


ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#007BFF", text_color="#FFFFFF", border_color="#0056b3")
buttonPosition = Position(type=PositionType.Relative, z_index=10)
buttonSize = Size(height="40px", padding="8px", margin="24px", font_size="14px", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
TableColor = Color(background_color="#FFFFFF", text_color="#343A40", border_color="#CED4DA")
TablePosition = Position(type=PositionType.Relative, top="200px", left="20px")
tableSize = Size(width="100%", padding="10px")
TableStyling = Styling(size=tableSize, position=TablePosition, color=TableColor)
viewComponent = ViewComponent(name="EmployeeManagementView", description="Manage employees with actions")
addEmployeeButton = Button(name="AddEmployeeButton", description="Add a new employee", label="Add New Employee", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add, styling=buttonStyling)
deleteEmployeeButton = Button(name="DeleteEmployeeButton", description="Delete selected employees", label="Delete", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Delete, styling=buttonStyling)
datasource_employee = DataSourceElement(name="EmployeeDataSource", dataSourceClass="Employee", fields=["name", "email", "address", "phone"])
employeeList = DataList(name="EmployeeList", description="List of employees", list_sources={datasource_employee}, styling=TableStyling)
EmployeeManagementScreen = Screen(name="EmployeeManagementScreen", description="Screen to manage employees", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", is_main_page=True, view_elements={addEmployeeButton, deleteEmployeeButton, employeeList}, layout=ScreenLayout)
EmployeeModule = Module(name="EmployeeModule", screens={EmployeeManagementScreen})
gui_model = GUIModel(name="EmployeeManagementApp", package="com.example.employeemanagement", versionCode="1", versionName="1.0", description="Application for managing employees.", screenCompatibility=True, modules={EmployeeModule})
