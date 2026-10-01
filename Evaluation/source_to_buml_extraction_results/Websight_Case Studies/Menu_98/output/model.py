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
WebPage_header: Property = Property(name="header", type=StringType)
WebPage_nav: Property = Property(name="nav", type=StringType)
WebPage_main: Property = Property(name="main", type=StringType)
WebPage.attributes={WebPage_header, WebPage_nav, WebPage_main}

# Header class attributes and methods
Header_logoSrc: Property = Property(name="logoSrc", type=StringType)
Header_logoAlt: Property = Property(name="logoAlt", type=StringType)
Header.attributes={Header_logoAlt, Header_logoSrc}

# Navigation class attributes and methods
Navigation_linkHref: Property = Property(name="linkHref", type=StringType)
Navigation_linkText: Property = Property(name="linkText", type=StringType)
Navigation.attributes={Navigation_linkHref, Navigation_linkText}

# MainContent class attributes and methods
MainContent_sectionDescription: Property = Property(name="sectionDescription", type=StringType)
MainContent_sectionImageSrc: Property = Property(name="sectionImageSrc", type=StringType)
MainContent_sectionImageAlt: Property = Property(name="sectionImageAlt", type=StringType)
MainContent_sectionId: Property = Property(name="sectionId", type=StringType)
MainContent_sectionTitle: Property = Property(name="sectionTitle", type=StringType)
MainContent.attributes={MainContent_sectionImageSrc, MainContent_sectionImageAlt, MainContent_sectionId, MainContent_sectionTitle, MainContent_sectionDescription}

# Relationships
header: BinaryAssociation = BinaryAssociation(
    name="header",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
nav: BinaryAssociation = BinaryAssociation(
    name="nav",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Navigation", type=Navigation, multiplicity=Multiplicity(1, 1))
    }
)
main: BinaryAssociation = BinaryAssociation(
    name="main",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="MainContent", type=MainContent, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, Header, Navigation, MainContent},
    associations={header, nav, main},
    generalizations={}
)
