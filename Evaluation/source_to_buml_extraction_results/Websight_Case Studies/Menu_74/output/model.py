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
MainContent = Class(name="MainContent")

# WebPage class attributes and methods

# Header class attributes and methods
Header_image: Property = Property(name="image", type=StringType)
Header.attributes={Header_image}

# Navigation class attributes and methods
Navigation_aboutLink: Property = Property(name="aboutLink", type=StringType)
Navigation_servicesLink: Property = Property(name="servicesLink", type=StringType)
Navigation_contactLink: Property = Property(name="contactLink", type=StringType)
Navigation_homeLink: Property = Property(name="homeLink", type=StringType)
Navigation.attributes={Navigation_servicesLink, Navigation_aboutLink, Navigation_homeLink, Navigation_contactLink}

# MainContent class attributes and methods
MainContent_welcomeMessage: Property = Property(name="welcomeMessage", type=StringType)
MainContent_servicesDescription: Property = Property(name="servicesDescription", type=StringType)
MainContent_contactInformation: Property = Property(name="contactInformation", type=StringType)
MainContent.attributes={MainContent_servicesDescription, MainContent_contactInformation, MainContent_welcomeMessage}

# Relationships
header: BinaryAssociation = BinaryAssociation(
    name="header",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
navigation: BinaryAssociation = BinaryAssociation(
    name="navigation",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Navigation", type=Navigation, multiplicity=Multiplicity(1, 1))
    }
)
mainContent: BinaryAssociation = BinaryAssociation(
    name="mainContent",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="MainContent", type=MainContent, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, Header, Navigation, MainContent},
    associations={header, navigation, mainContent},
    generalizations={}
)
