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
WebPage_header: Property = Property(name="header", type=Header)
WebPage_nav: Property = Property(name="nav", type=Navigation)
WebPage_main: Property = Property(name="main", type=MainContent)
WebPage.attributes={WebPage_main, WebPage_header, WebPage_nav}

# Header class attributes and methods
Header_logoSrc: Property = Property(name="logoSrc", type=StringType)
Header_logoAlt: Property = Property(name="logoAlt", type=StringType)
Header.attributes={Header_logoAlt, Header_logoSrc}

# Navigation class attributes and methods
Navigation_servicesText: Property = Property(name="servicesText", type=StringType)
Navigation_projectsHref: Property = Property(name="projectsHref", type=StringType)
Navigation_projectsText: Property = Property(name="projectsText", type=StringType)
Navigation_aboutHref: Property = Property(name="aboutHref", type=StringType)
Navigation_aboutText: Property = Property(name="aboutText", type=StringType)
Navigation_servicesHref: Property = Property(name="servicesHref", type=StringType)
Navigation.attributes={Navigation_projectsText, Navigation_aboutHref, Navigation_servicesHref, Navigation_servicesText, Navigation_aboutText, Navigation_projectsHref}

# MainContent class attributes and methods
MainContent_servicesTitle: Property = Property(name="servicesTitle", type=StringType)
MainContent_servicesDescription: Property = Property(name="servicesDescription", type=StringType)
MainContent_projectsTitle: Property = Property(name="projectsTitle", type=StringType)
MainContent_projectsDescription: Property = Property(name="projectsDescription", type=StringType)
MainContent_aboutTitle: Property = Property(name="aboutTitle", type=StringType)
MainContent_aboutDescription: Property = Property(name="aboutDescription", type=StringType)
MainContent.attributes={MainContent_servicesTitle, MainContent_servicesDescription, MainContent_projectsTitle, MainContent_projectsDescription, MainContent_aboutTitle, MainContent_aboutDescription}

# Relationships
WebPage_Header: BinaryAssociation = BinaryAssociation(
    name="WebPage_Header",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
WebPage_Navigation: BinaryAssociation = BinaryAssociation(
    name="WebPage_Navigation",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Navigation", type=Navigation, multiplicity=Multiplicity(1, 1))
    }
)
WebPage_MainContent: BinaryAssociation = BinaryAssociation(
    name="WebPage_MainContent",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="MainContent", type=MainContent, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, Header, Navigation, MainContent},
    associations={WebPage_Header, WebPage_Navigation, WebPage_MainContent},
    generalizations={}
)
