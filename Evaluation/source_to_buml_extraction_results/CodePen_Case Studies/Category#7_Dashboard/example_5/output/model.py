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
Navbar = Class(name="Navbar")
DropdownMenu = Class(name="DropdownMenu")
Aside = Class(name="Aside")
NotificationPanel = Class(name="NotificationPanel")
SearchPanel = Class(name="SearchPanel")
UserMenu = Class(name="UserMenu")
Footer = Class(name="Footer")

# Navbar class attributes and methods
Navbar_brand: Property = Property(name="brand", type=StringType)
Navbar_activity: Property = Property(name="activity", type=StringType)
Navbar_notifications: Property = Property(name="notifications", type=IntegerType)
Navbar_user: Property = Property(name="user", type=StringType)
Navbar.attributes={Navbar_brand, Navbar_activity, Navbar_notifications, Navbar_user}

# DropdownMenu class attributes and methods
DropdownMenu_title: Property = Property(name="title", type=StringType)
DropdownMenu.attributes={DropdownMenu_title}

# Aside class attributes and methods
Aside_projects: Property = Property(name="projects", type=StringType)
Aside_navItems: Property = Property(name="navItems", type=StringType)
Aside.attributes={Aside_projects, Aside_navItems}

# NotificationPanel class attributes and methods
NotificationPanel_notificationCount: Property = Property(name="notificationCount", type=IntegerType)
NotificationPanel.attributes={NotificationPanel_notificationCount}

# SearchPanel class attributes and methods
SearchPanel_query: Property = Property(name="query", type=StringType)
SearchPanel.attributes={SearchPanel_query}

# UserMenu class attributes and methods
UserMenu_username: Property = Property(name="username", type=StringType)
UserMenu.attributes={UserMenu_username}

# Footer class attributes and methods
Footer_chatStatus: Property = Property(name="chatStatus", type=StringType)
Footer_contactStatus: Property = Property(name="contactStatus", type=StringType)
Footer.attributes={Footer_chatStatus, Footer_contactStatus}

# Relationships
navDropdown: BinaryAssociation = BinaryAssociation(
    name="navDropdown",
    ends={
        Property(name="Navbar", type=Navbar, multiplicity=Multiplicity(1, 1)),
        Property(name="DropdownMenu", type=DropdownMenu, multiplicity=Multiplicity(1, 1))
    }
)
navNotification: BinaryAssociation = BinaryAssociation(
    name="navNotification",
    ends={
        Property(name="Navbar", type=Navbar, multiplicity=Multiplicity(1, 1)),
        Property(name="NotificationPanel", type=NotificationPanel, multiplicity=Multiplicity(1, 1))
    }
)
navSearch: BinaryAssociation = BinaryAssociation(
    name="navSearch",
    ends={
        Property(name="Navbar", type=Navbar, multiplicity=Multiplicity(1, 1)),
        Property(name="SearchPanel", type=SearchPanel, multiplicity=Multiplicity(1, 1))
    }
)
navUserMenu: BinaryAssociation = BinaryAssociation(
    name="navUserMenu",
    ends={
        Property(name="Navbar", type=Navbar, multiplicity=Multiplicity(1, 1)),
        Property(name="UserMenu", type=UserMenu, multiplicity=Multiplicity(1, 1))
    }
)
asideFooter: BinaryAssociation = BinaryAssociation(
    name="asideFooter",
    ends={
        Property(name="Aside", type=Aside, multiplicity=Multiplicity(1, 1)),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={Navbar, DropdownMenu, Aside, NotificationPanel, SearchPanel, UserMenu, Footer},
    associations={navDropdown, navNotification, navSearch, navUserMenu, asideFooter},
    generalizations={}
)
