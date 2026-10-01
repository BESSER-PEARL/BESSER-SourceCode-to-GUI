from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *
from enum import Enum


class LayoutType(Enum):
    Flex = "flex"
    Grid = "grid"


class PositionType(Enum):
    Relative = "relative"
    Absolute = "absolute"


class UnitSize(Enum):
    PIXELS = "px"
    PERCENT = "%"


class ButtonType(Enum):
    RaisedButton = "raised"


class ButtonActionType(Enum):
    SubmitForm = "submit"


class JustificationType(Enum):
    Center = "center"


class Color:

    def __init__(self, background_color, text_color, border_color):
        self.background_color = background_color
        self.text_color = text_color
        self.border_color = border_color


class Position:

    def __init__(self, type, z_index=0):
        self.type = type
        self.z_index = z_index


class Size:

    def __init__(self, width=None, height=None, padding=None, font_size=None, unit_size=UnitSize.PIXELS):
        self.width = width
        self.height = height
        self.padding = padding
        self.font_size = font_size
        self.unit_size = unit_size


class Styling:

    def __init__(self, size=None, position=None, color=None):
        self.size = size
        self.position = position
        self.color = color


class Layout:

    def __init__(self, type, orientation, gap, alignment):
        self.type = type
        self.orientation = orientation
        self.gap = gap
        self.alignment = alignment


ScreenLayout = Layout(type=LayoutType.Flex, orientation="vertical", gap="15px", alignment=JustificationType.Center)
ButtonColor = Color(background_color="#CA4D5D", text_color="#FFFFFF", border_color="#744F96")
buttonPosition = Position(type=PositionType.Relative, z_index=10)
buttonSize = Size(height="40px", padding="8px", font_size="1.2em", unit_size=UnitSize.PIXELS)
buttonStyling = Styling(size=buttonSize, position=buttonPosition, color=ButtonColor)
inputFieldColor = Color(background_color="#FFFFFF", text_color="#000000", border_color="#E25B5E")
inputFieldPosition = Position(type=PositionType.Relative)
inputFieldSize = Size(width="100%", height="30px", padding="5px", font_size="16px", unit_size=UnitSize.PIXELS)
inputFieldStyling = Styling(size=inputFieldSize, position=inputFieldPosition, color=inputFieldColor)


class InputField:

    def __init__(self, name, description, type, styling, property):
        self.name = name
        self.description = description
        self.type = type
        self.styling = styling
        self.property = property


firstnameField = InputField(name="FirstNameField", description="Input for first name", type="Text", styling=inputFieldStyling)
surnameField = InputField(name="SurnameField", description="Input for surname", type="Text", styling=inputFieldStyling)
ageField = InputField(name="AgeField", description="Input for age", type="Number", styling=inputFieldStyling)
numberField = InputField(name="NumberField", description="Input for number", type="Number", styling=inputFieldStyling)
emailField = InputField(name="EmailField", description="Input for email", type="Email", styling=inputFieldStyling)
addressField = InputField(name="AddressField", description="Input for address", type="Text", styling=inputFieldStyling)


class Form:

    def __init__(self, name, description, inputFields, styling=None):
        self.name = name
        self.description = description
        self.inputFields = inputFields
        self.styling = styling


contactForm = Form(name="ContactForm", description="Form to create a new contact", inputFields={firstnameField, surnameField, ageField, numberField, emailField, addressField})


class Button:

    def __init__(self, name, description, label, buttonType, actionType, styling):
        self.name = name
        self.description = description
        self.label = label
        self.buttonType = buttonType
        self.actionType = actionType
        self.styling = styling


submitButton = Button(name="SubmitButton", description="Submit the form", label="Create Contact", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.SubmitForm, styling=buttonStyling)


class DataSourceElement:

    def __init__(self, name, dataSourceClass, fields):
        self.name = name
        self.dataSourceClass = dataSourceClass
        self.fields = fields


datasource_contacts = DataSourceElement(name="ContactsDataSource", dataSourceClass="Contacts", fields=["Form_firstname", "Form_surname", "Form_age", "Form_phoneNumber", "Form_email", "Form_address"])


class DataList:

    def __init__(self, name, description, list_sources, styling=None):
        self.name = name
        self.description = description
        self.list_sources = list_sources
        self.styling = styling


contactsList = DataList(name="ContactsList", description="List of contacts", list_sources={datasource_contacts})


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


ContactManagerScreen = Screen(name="ContactManagerScreen", description="Screen for managing contacts", x_dpi="x_dpi", y_dpi="y_dpi", screen_size="Medium", view_elements={contactForm, submitButton, contactsList}, is_main_page=True, layout=ScreenLayout)


class Module:

    def __init__(self, name, screens):
        self.name = name
        self.screens = screens


ContactManagerModule = Module(name="ContactManagerModule", screens={ContactManagerScreen})


class GUIModel:

    def __init__(self, name, package, versionCode, versionName, description, screenCompatibility, modules):
        self.name = name
        self.package = package
        self.versionCode = versionCode
        self.versionName = versionName
        self.description = description
        self.screenCompatibility = screenCompatibility
        self.modules = modules


gui_model = GUIModel(name="ContactManagerApp", package="com.example.contactmanager", versionCode="1", versionName="1.0", description="An application for managing contacts", screenCompatibility=True, modules={ContactManagerModule})
