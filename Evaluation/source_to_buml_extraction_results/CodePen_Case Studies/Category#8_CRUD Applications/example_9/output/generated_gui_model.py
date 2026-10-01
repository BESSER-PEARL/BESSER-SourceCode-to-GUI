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
    TextButton = "text"


class ButtonActionType(Enum):
    Navigate = "navigate"
    Add = "add"
    Edit = "edit"
    Delete = "delete"


class JustificationType(Enum):
    Center = "center"


class UnitSize(Enum):
    PIXELS = "px"


class Layout:

    def __init__(self, type, orientation, gap, alignment):
        self.type = type
        self.orientation = orientation
        self.gap = gap
        self.alignment = alignment


class Size:

    def __init__(self, width, height, padding, margin, font_size, unit_size):
        self.width = width
        self.height = height
        self.padding = padding
        self.margin = margin
        self.font_size = font_size
        self.unit_size = unit_size


class Color:

    def __init__(self, background_color, text_color, border_color):
        self.background_color = background_color
        self.text_color = text_color
        self.border_color = border_color


class Position:

    def __init__(self, type, z_index):
        self.type = type
        self.z_index = z_index


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

    def __init__(self, name, description, label, buttonType, actionType, targetScreen, styling):
        super().__init__(name, description)
        self.label = label
        self.buttonType = buttonType
        self.actionType = actionType
        self.targetScreen = targetScreen
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


class Screen(ViewComponent):

    def __init__(self, name, description, x_dpi, y_dpi, screen_size, view_elements, layout, is_main_page):
        super().__init__(name, description)
        self.x_dpi = x_dpi
        self.y_dpi = y_dpi
        self.screen_size = screen_size
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


ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#007BFF", text_color="#FFFFFF", border_color="#0056b3")
buttonPosition = Position(type=PositionType.Relative, z_index=10)
buttonSize = Size(width="150px", height="40px", padding="8px", margin="24px", font_size="14px", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
viewComponent = ViewComponent(name="ProductView", description="Display product details and actions")
backButton = Button(name="BackButton", description="Back to product list", label="Back to product list", buttonType=ButtonType.TextButton, actionType=ButtonActionType.Navigate, targetScreen=None, styling=buttonStyling)
addButton = Button(name="AddProductButton", description="Add a new product", label="Add product", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Add, targetScreen=None, styling=buttonStyling)
editButton = Button(name="EditProductButton", description="Edit product", label="Edit", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Edit, targetScreen=None, styling=buttonStyling)
deleteButton = Button(name="DeleteProductButton", description="Delete product", label="Delete", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Delete, targetScreen=None, styling=buttonStyling)
productDataSource = DataSourceElement(name="ProductDataSource", dataSourceClass="Product", fields=["Product_name", "Product_description", "Product_price"])
productList = DataList(name="ProductList", description="List of products", list_sources={productDataSource}, styling=None)
ProductScreen = Screen(name="ProductScreen", description="Product details and actions", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={backButton, addButton, editButton, deleteButton, productList}, layout=ScreenLayout, is_main_page=True)
ProductModule = Module(name="ProductModule", screens={ProductScreen})
gui_model = GUIModel(name="ProductManagementApp", package="com.example.productmanagement", versionCode="1", versionName="1.0", description="A web application for managing products.", screenCompatibility=True, modules={ProductModule})
