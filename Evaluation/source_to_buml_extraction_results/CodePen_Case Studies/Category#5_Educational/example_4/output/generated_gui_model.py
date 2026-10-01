from besser.BUML.notations.source_code_to_buml.output.buml.model import *
from besser.BUML.metamodel.structural import *
from besser.BUML.metamodel.gui import *
from enum import Enum


class LayoutType(Enum):
    Flex = "flex"


class PositionType(Enum):
    Relative = "relative"
    Fixed = "fixed"


class ButtonType(Enum):
    TextButton = "text_button"


class ButtonActionType(Enum):
    Toggle = "toggle"


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


class Position:

    def __init__(self, type, bottom=None, left=None, z_index=None):
        self.type = type
        self.bottom = bottom
        self.left = left
        self.z_index = z_index


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


class Styling:

    def __init__(self, size, position, color):
        self.size = size
        self.position = position
        self.color = color


class ViewComponent:

    def __init__(self, name, description, styling=None):
        self.name = name
        self.description = description
        self.styling = styling


class Button(ViewComponent):

    def __init__(self, name, description, label, buttonType, actionType, styling):
        super().__init__(name, description, styling)
        self.label = label
        self.buttonType = buttonType
        self.actionType = actionType


class Screen:

    def __init__(self, name, description, view_elements, is_main_page, layout):
        self.name = name
        self.description = description
        self.view_elements = view_elements
        self.is_main_page = is_main_page
        self.layout = layout


AccordionButtonColor = Color("#f7d794", "#814329", "#CCCCCC", border_color="", background_color="", text_color="")
AccordionButtonPosition = Position(PositionType.Relative)
AccordionButtonSize = Size("100%", "auto", "15px 20px", "30px 0", "16px", UnitSize.PIXELS)
AccordionButtonStyling = Styling(AccordionButtonSize, AccordionButtonPosition, AccordionButtonColor)
AccordionContentColor = Color("#fff8e1", "#333333", "#DDDDDD", border_color="", background_color="", text_color="")
AccordionContentPosition = Position(PositionType.Relative)
AccordionContentSize = Size("100%", "auto", "0 20px", "0", "14px", UnitSize.PIXELS)
AccordionContentStyling = Styling(AccordionContentSize, AccordionContentPosition, AccordionContentColor)
BadgeColor = Color("#222", "#fff", "#FFFFFF", border_color="", background_color="", text_color="")
BadgePosition = Position(PositionType.Fixed, "20px", "50%", 9999)
BadgeSize = Size("auto", "auto", "8px 14px", "0", "14px", UnitSize.PIXELS)
BadgeStyling = Styling(BadgeSize, BadgePosition, BadgeColor)
accordionItem1 = Button("AccordionItem1", "Accordion item for Quantum Entanglement", "What is Quantum Entanglement?", ButtonType.TextButton, ButtonActionType.Toggle, AccordionButtonStyling, buttonType="", name="", label="", actionType="", description="")
accordionContent1 = ViewComponent("AccordionContent1", "Quantum Entanglement content", AccordionContentStyling, description="", name="")
accordionItem2 = Button("AccordionItem2", "Accordion item for Nonlocality", "What does Nonlocality mean in quantum physics?", ButtonType.TextButton, ButtonActionType.Toggle, AccordionButtonStyling, buttonType="", name="", label="", actionType="", description="")
accordionContent2 = ViewComponent("AccordionContent2", "Nonlocality content", AccordionContentStyling, description="", name="")
badgeSticky = ViewComponent("BadgeSticky", "Designed by Soharab Zia", BadgeStyling, description="", name="")
ScreenLayout = Layout(LayoutType.Flex, "vertical", "15px", JustificationType.Center)
FAQScreen = Screen("FAQPage", "FAQ Page description", {accordionItem1, accordionContent1, accordionItem2, accordionContent2, badgeSticky}, True, ScreenLayout, x_dpi="", name="", screen_size="", description="", view_elements="", y_dpi="")


class Module:

    def __init__(self, name, screens):
        self.name = name
        self.screens = screens


FAQModule = Module("FAQModule", {FAQScreen}, name="", screens="")


class GUIModel:

    def __init__(self, name, package, versionCode, versionName, description, screenCompatibility, modules):
        self.name = name
        self.package = package
        self.versionCode = versionCode
        self.versionName = versionName
        self.description = description
        self.screenCompatibility = screenCompatibility
        self.modules = modules


gui_model = GUIModel("FAQApplication", "com.example.faqapplication", "1", "1.0", "An application for displaying FAQs about Quantum Physics.", True, {FAQModule}, versionName="", modules="", package="", versionCode="", name="", description="")
