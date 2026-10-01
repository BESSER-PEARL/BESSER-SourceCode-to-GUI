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
Navigation = Class(name="Navigation")
Menu = Class(name="Menu")

# WebPage class attributes and methods

# Header class attributes and methods
Header_logo: Property = Property(name="logo", type=StringType)
Header_backgroundImage: Property = Property(name="backgroundImage", type=StringType)
Header.attributes={Header_logo, Header_backgroundImage}

# Navigation class attributes and methods
Navigation_homeLink: Property = Property(name="homeLink", type=StringType)
Navigation_menuLink: Property = Property(name="menuLink", type=StringType)
Navigation_aboutUsLink: Property = Property(name="aboutUsLink", type=StringType)
Navigation_contactLink: Property = Property(name="contactLink", type=StringType)
Navigation.attributes={Navigation_aboutUsLink, Navigation_contactLink, Navigation_homeLink, Navigation_menuLink}

# Menu class attributes and methods
Menu_item: Property = Property(name="item", type=StringType)
Menu_price: Property = Property(name="price", type=FloatType)
Menu.attributes={Menu_price, Menu_item}

# Relationships
containsNavigation: BinaryAssociation = BinaryAssociation(
    name="containsNavigation",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Navigation", type=Navigation, multiplicity=Multiplicity(1, 1))
    }
)
containsMenu: BinaryAssociation = BinaryAssociation(
    name="containsMenu",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Menu", type=Menu, multiplicity=Multiplicity(1, 1))
    }
)
containsHeader: BinaryAssociation = BinaryAssociation(
    name="containsHeader",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, Header, Navigation, Menu},
    associations={containsNavigation, containsMenu, containsHeader},
    generalizations={}
)
