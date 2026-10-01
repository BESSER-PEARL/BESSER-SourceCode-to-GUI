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
WebPage = Class(name="WebPage")
Header = Class(name="Header")
NavigationMenu = Class(name="NavigationMenu")
Main = Class(name="Main")
LeftSidebar = Class(name="LeftSidebar")
CenterSection = Class(name="CenterSection")
RightSidebar = Class(name="RightSidebar")

# WebPage class attributes and methods

# Header class attributes and methods

# NavigationMenu class attributes and methods

# Main class attributes and methods

# LeftSidebar class attributes and methods

# CenterSection class attributes and methods

# RightSidebar class attributes and methods

# Relationships
mainContent: BinaryAssociation = BinaryAssociation(
    name="mainContent",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1))
    }
)
navigation: BinaryAssociation = BinaryAssociation(
    name="navigation",
    ends={
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="NavigationMenu", type=NavigationMenu, multiplicity=Multiplicity(1, 1))
    }
)
left: BinaryAssociation = BinaryAssociation(
    name="left",
    ends={
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="LeftSidebar", type=LeftSidebar, multiplicity=Multiplicity(1, 1))
    }
)
center: BinaryAssociation = BinaryAssociation(
    name="center",
    ends={
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="CenterSection", type=CenterSection, multiplicity=Multiplicity(1, 1))
    }
)
right: BinaryAssociation = BinaryAssociation(
    name="right",
    ends={
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="RightSidebar", type=RightSidebar, multiplicity=Multiplicity(1, 1))
    }
)
header: BinaryAssociation = BinaryAssociation(
    name="header",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, Header, NavigationMenu, Main, LeftSidebar, CenterSection, RightSidebar},
    associations={mainContent, navigation, left, center, right, header},
    generalizations={}
)
