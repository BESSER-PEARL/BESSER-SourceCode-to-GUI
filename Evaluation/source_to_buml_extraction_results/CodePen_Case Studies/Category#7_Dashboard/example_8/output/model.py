####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
User = Class(name="User")
Section = Class(name="Section")
Action = Class(name="Action")
Button = Class(name="Button")
Menu = Class(name="Menu")
List = Class(name="List")
Item = Class(name="Item")
AppData = Class(name="AppData")
Sidenav = Class(name="Sidenav")
Toolbar = Class(name="Toolbar")
Content = Class(name="Content")

# User class attributes and methods
User_icon: Property = Property(name="icon", type=StringType)
User_name: Property = Property(name="name", type=StringType)
User_email: Property = Property(name="email", type=StringType)
User.attributes={User_icon, User_email, User_name}

# Section class attributes and methods
Section_name: Property = Property(name="name", type=StringType)
Section_expand: Property = Property(name="expand", type=BooleanType)
Section.attributes={Section_expand, Section_name}

# Action class attributes and methods
Action_name: Property = Property(name="name", type=StringType)
Action_link: Property = Property(name="link", type=StringType)
Action_error: Property = Property(name="error", type=BooleanType)
Action_completed: Property = Property(name="completed", type=BooleanType)
Action_message: Property = Property(name="message", type=StringType)
Action_icon: Property = Property(name="icon", type=StringType)
Action.attributes={Action_message, Action_link, Action_error, Action_icon, Action_completed, Action_name}

# Button class attributes and methods
Button_name: Property = Property(name="name", type=StringType)
Button_icon: Property = Property(name="icon", type=StringType)
Button_link: Property = Property(name="link", type=StringType)
Button.attributes={Button_name, Button_link, Button_icon}

# Menu class attributes and methods
Menu_name: Property = Property(name="name", type=StringType)
Menu_icon: Property = Property(name="icon", type=StringType)
Menu_width: Property = Property(name="width", type=IntegerType)
Menu.attributes={Menu_icon, Menu_name, Menu_width}

# List class attributes and methods
List_name: Property = Property(name="name", type=StringType)
List.attributes={List_name}

# Item class attributes and methods
Item_name: Property = Property(name="name", type=StringType)
Item_description: Property = Property(name="description", type=StringType)
Item_link: Property = Property(name="link", type=StringType)
Item.attributes={Item_name, Item_description, Item_link}

# AppData class attributes and methods
AppData_title: Property = Property(name="title", type=StringType)
AppData.attributes={AppData_title}

# Sidenav class attributes and methods

# Toolbar class attributes and methods

# Content class attributes and methods

# Relationships
user: BinaryAssociation = BinaryAssociation(
    name="user",
    ends={
        Property(name="AppData", type=AppData, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="User", type=User, multiplicity=Multiplicity(1, 1))
    }
)
sidenav: BinaryAssociation = BinaryAssociation(
    name="sidenav",
    ends={
        Property(name="AppData", type=AppData, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Sidenav", type=Sidenav, multiplicity=Multiplicity(1, 1))
    }
)
toolbar: BinaryAssociation = BinaryAssociation(
    name="toolbar",
    ends={
        Property(name="AppData", type=AppData, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Toolbar", type=Toolbar, multiplicity=Multiplicity(1, 1))
    }
)
content: BinaryAssociation = BinaryAssociation(
    name="content",
    ends={
        Property(name="AppData", type=AppData, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Content", type=Content, multiplicity=Multiplicity(1, 1))
    }
)
sections: BinaryAssociation = BinaryAssociation(
    name="sections",
    ends={
        Property(name="Sidenav", type=Sidenav, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Section", type=Section, multiplicity=Multiplicity(1, 1))
    }
)
buttons: BinaryAssociation = BinaryAssociation(
    name="buttons",
    ends={
        Property(name="Button", type=Button, multiplicity=Multiplicity(1, 1)),
        Property(name="Toolbar", type=Toolbar, multiplicity=Multiplicity(1, 1), is_navigable=False)
    }
)
menus: BinaryAssociation = BinaryAssociation(
    name="menus",
    ends={
        Property(name="Toolbar", type=Toolbar, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Menu", type=Menu, multiplicity=Multiplicity(1, 1))
    }
)
menuActions: BinaryAssociation = BinaryAssociation(
    name="menuActions",
    ends={
        Property(name="Menu", type=Menu, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Action", type=Action, multiplicity=Multiplicity(1, 1))
    }
)
lists: BinaryAssociation = BinaryAssociation(
    name="lists",
    ends={
        Property(name="Content", type=Content, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="List", type=List, multiplicity=Multiplicity(1, 1))
    }
)
items: BinaryAssociation = BinaryAssociation(
    name="items",
    ends={
        Property(name="List", type=List, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Item", type=Item, multiplicity=Multiplicity(1, 1))
    }
)
listMenus: BinaryAssociation = BinaryAssociation(
    name="listMenus",
    ends={
        Property(name="List", type=List, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Menu", type=Menu, multiplicity=Multiplicity(1, 1))
    }
)
actions: BinaryAssociation = BinaryAssociation(
    name="actions",
    ends={
        Property(name="Section", type=Section, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="Action", type=Action, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={User, Section, Action, Button, Menu, List, Item, AppData, Sidenav, Toolbar, Content},
    associations={user, sidenav, toolbar, content, sections, buttons, menus, menuActions, lists, items, listMenus, actions},
    generalizations={}
)
