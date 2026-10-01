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
Main = Class(name="Main")
Footer = Class(name="Footer")

# WebPage class attributes and methods
WebPage_header: Property = Property(name="header", type=Header)
WebPage_main: Property = Property(name="main", type=Main)
WebPage_footer: Property = Property(name="footer", type=Footer)
WebPage.attributes={WebPage_main, WebPage_footer, WebPage_header}

# Header class attributes and methods
Header_logoSrc: Property = Property(name="logoSrc", type=StringType)
Header_logoAlt: Property = Property(name="logoAlt", type=StringType)
Header_navigationLinkText: Property = Property(name="navigationLinkText", type=StringType)
Header_navigationLinkHref: Property = Property(name="navigationLinkHref", type=StringType)
Header_socialMediaPlatform: Property = Property(name="socialMediaPlatform", type=StringType)
Header_socialMediaIconSrc: Property = Property(name="socialMediaIconSrc", type=StringType)
Header_socialMediaIconAlt: Property = Property(name="socialMediaIconAlt", type=StringType)
Header.attributes={Header_socialMediaPlatform, Header_navigationLinkHref, Header_logoAlt, Header_logoSrc, Header_socialMediaIconSrc, Header_socialMediaIconAlt, Header_navigationLinkText}

# Main class attributes and methods
Main_title: Property = Property(name="title", type=StringType)
Main_description: Property = Property(name="description", type=StringType)
Main.attributes={Main_title, Main_description}

# Footer class attributes and methods
Footer_copyrightNotice: Property = Property(name="copyrightNotice", type=StringType)
Footer.attributes={Footer_copyrightNotice}

# Relationships
footerLink: BinaryAssociation = BinaryAssociation(
    name="footerLink",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)
headerLink: BinaryAssociation = BinaryAssociation(
    name="headerLink",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
mainLink: BinaryAssociation = BinaryAssociation(
    name="mainLink",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, Header, Main, Footer},
    associations={footerLink, headerLink, mainLink},
    generalizations={}
)
