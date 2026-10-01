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
Graph = Class(name="Graph")
UserDashboard = Class(name="UserDashboard")
UserDetailsContainer = Class(name="UserDetailsContainer")
Avatar = Class(name="Avatar")
UserSettings = Class(name="UserSettings")
MainMenu = Class(name="MainMenu")
NavContainer = Class(name="NavContainer")
NavItem = Class(name="NavItem")
Subnav = Class(name="Subnav")
MainContent = Class(name="MainContent")
Header = Class(name="Header")
InputContainer = Class(name="InputContainer")
ScrollContainer = Class(name="ScrollContainer")
ContentContainer = Class(name="ContentContainer")
ContentSection = Class(name="ContentSection")
ContentItem = Class(name="ContentItem")
ContentHeader = Class(name="ContentHeader")
ContentBody = Class(name="ContentBody")
ContentBodyItem = Class(name="ContentBodyItem")

# Graph class attributes and methods

# UserDashboard class attributes and methods

# UserDetailsContainer class attributes and methods

# Avatar class attributes and methods

# UserSettings class attributes and methods

# MainMenu class attributes and methods

# NavContainer class attributes and methods

# NavItem class attributes and methods
NavItem_analytics: Property = Property(name="analytics", type=StringType)
NavItem_projects: Property = Property(name="projects", type=StringType)
NavItem_teams: Property = Property(name="teams", type=StringType)
NavItem_users: Property = Property(name="users", type=StringType)
NavItem.attributes={NavItem_projects, NavItem_teams, NavItem_users, NavItem_analytics}

# Subnav class attributes and methods
Subnav_option4: Property = Property(name="option4", type=StringType)
Subnav_option1: Property = Property(name="option1", type=StringType)
Subnav_option2: Property = Property(name="option2", type=StringType)
Subnav_option3: Property = Property(name="option3", type=StringType)
Subnav.attributes={Subnav_option3, Subnav_option2, Subnav_option4, Subnav_option1}

# MainContent class attributes and methods

# Header class attributes and methods
Header_greeting: Property = Property(name="greeting", type=StringType)
Header.attributes={Header_greeting}

# InputContainer class attributes and methods
InputContainer_search: Property = Property(name="search", type=StringType)
InputContainer.attributes={InputContainer_search}

# ScrollContainer class attributes and methods

# ContentContainer class attributes and methods

# ContentSection class attributes and methods
ContentSection_title: Property = Property(name="title", type=StringType)
ContentSection.attributes={ContentSection_title}

# ContentItem class attributes and methods

# ContentHeader class attributes and methods
ContentHeader_title: Property = Property(name="title", type=StringType)
ContentHeader.attributes={ContentHeader_title}

# ContentBody class attributes and methods

# ContentBodyItem class attributes and methods
ContentBodyItem_day: Property = Property(name="day", type=StringType)
ContentBodyItem_stat: Property = Property(name="stat", type=StringType)
ContentBodyItem.attributes={ContentBodyItem_stat, ContentBodyItem_day}

# Relationships
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="UserDashboard", type=UserDashboard, multiplicity=Multiplicity(1, 1)),
        Property(name="UserDetailsContainer", type=UserDetailsContainer, multiplicity=Multiplicity(1, 1))
    }
)
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="UserDetailsContainer", type=UserDetailsContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="Avatar", type=Avatar, multiplicity=Multiplicity(1, 1))
    }
)
association7: BinaryAssociation = BinaryAssociation(
    name="association7",
    ends={
        Property(name="NavItem", type=NavItem, multiplicity=Multiplicity(1, 1)),
        Property(name="Subnav", type=Subnav, multiplicity=Multiplicity(1, 1))
    }
)
association3: BinaryAssociation = BinaryAssociation(
    name="association3",
    ends={
        Property(name="UserDetailsContainer", type=UserDetailsContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="UserSettings", type=UserSettings, multiplicity=Multiplicity(1, 1))
    }
)
association4: BinaryAssociation = BinaryAssociation(
    name="association4",
    ends={
        Property(name="UserDashboard", type=UserDashboard, multiplicity=Multiplicity(1, 1)),
        Property(name="MainMenu", type=MainMenu, multiplicity=Multiplicity(1, 1))
    }
)
association5: BinaryAssociation = BinaryAssociation(
    name="association5",
    ends={
        Property(name="MainMenu", type=MainMenu, multiplicity=Multiplicity(1, 1)),
        Property(name="NavContainer", type=NavContainer, multiplicity=Multiplicity(1, 1))
    }
)
association6: BinaryAssociation = BinaryAssociation(
    name="association6",
    ends={
        Property(name="NavContainer", type=NavContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="NavItem", type=NavItem, multiplicity=Multiplicity(5, 5))
    }
)
association14: BinaryAssociation = BinaryAssociation(
    name="association14",
    ends={
        Property(name="ContentSection", type=ContentSection, multiplicity=Multiplicity(1, 1)),
        Property(name="ContentItem", type=ContentItem, multiplicity=Multiplicity(1, 1))
    }
)
association8: BinaryAssociation = BinaryAssociation(
    name="association8",
    ends={
        Property(name="UserDashboard", type=UserDashboard, multiplicity=Multiplicity(1, 1)),
        Property(name="MainContent", type=MainContent, multiplicity=Multiplicity(1, 1))
    }
)
association9: BinaryAssociation = BinaryAssociation(
    name="association9",
    ends={
        Property(name="MainContent", type=MainContent, multiplicity=Multiplicity(1, 1)),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
association10: BinaryAssociation = BinaryAssociation(
    name="association10",
    ends={
        Property(name="MainContent", type=MainContent, multiplicity=Multiplicity(1, 1)),
        Property(name="InputContainer", type=InputContainer, multiplicity=Multiplicity(1, 1))
    }
)
association11: BinaryAssociation = BinaryAssociation(
    name="association11",
    ends={
        Property(name="MainContent", type=MainContent, multiplicity=Multiplicity(1, 1)),
        Property(name="ScrollContainer", type=ScrollContainer, multiplicity=Multiplicity(1, 1))
    }
)
association12: BinaryAssociation = BinaryAssociation(
    name="association12",
    ends={
        Property(name="ScrollContainer", type=ScrollContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="ContentContainer", type=ContentContainer, multiplicity=Multiplicity(1, 1))
    }
)
association13: BinaryAssociation = BinaryAssociation(
    name="association13",
    ends={
        Property(name="ContentContainer", type=ContentContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="ContentSection", type=ContentSection, multiplicity=Multiplicity(6, 6))
    }
)
association15: BinaryAssociation = BinaryAssociation(
    name="association15",
    ends={
        Property(name="ContentItem", type=ContentItem, multiplicity=Multiplicity(1, 1)),
        Property(name="ContentHeader", type=ContentHeader, multiplicity=Multiplicity(1, 1))
    }
)
association16: BinaryAssociation = BinaryAssociation(
    name="association16",
    ends={
        Property(name="ContentItem", type=ContentItem, multiplicity=Multiplicity(1, 1)),
        Property(name="ContentBody", type=ContentBody, multiplicity=Multiplicity(1, 1))
    }
)
association17: BinaryAssociation = BinaryAssociation(
    name="association17",
    ends={
        Property(name="ContentBody", type=ContentBody, multiplicity=Multiplicity(1, 1)),
        Property(name="ContentBodyItem", type=ContentBodyItem, multiplicity=Multiplicity(7, 7))
    }
)
association18: BinaryAssociation = BinaryAssociation(
    name="association18",
    ends={
        Property(name="ContentBodyItem", type=ContentBodyItem, multiplicity=Multiplicity(1, 1)),
        Property(name="Graph", type=Graph, multiplicity=Multiplicity(2, 2))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={Graph, UserDashboard, UserDetailsContainer, Avatar, UserSettings, MainMenu, NavContainer, NavItem, Subnav, MainContent, Header, InputContainer, ScrollContainer, ContentContainer, ContentSection, ContentItem, ContentHeader, ContentBody, ContentBodyItem},
    associations={association1, association2, association7, association3, association4, association5, association6, association14, association8, association9, association10, association11, association12, association13, association15, association16, association17, association18},
    generalizations={}
)
