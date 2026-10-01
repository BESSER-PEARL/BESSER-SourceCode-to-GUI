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
SearchBar = Class(name="SearchBar")
Main = Class(name="Main")
Footer = Class(name="Footer")
SocialLinks = Class(name="SocialLinks")

# WebPage class attributes and methods
WebPage_header: Property = Property(name="header", type=StringType)
WebPage_main: Property = Property(name="main", type=StringType)
WebPage_footer: Property = Property(name="footer", type=StringType)
WebPage.attributes={WebPage_header, WebPage_main, WebPage_footer}

# Header class attributes and methods
Header_logo: Property = Property(name="logo", type=StringType)
Header_navigation: Property = Property(name="navigation", type=StringType)
Header_searchBar: Property = Property(name="searchBar", type=StringType)
Header.attributes={Header_navigation, Header_searchBar, Header_logo}

# Navigation class attributes and methods
Navigation_aboutLink: Property = Property(name="aboutLink", type=StringType)
Navigation_servicesLink: Property = Property(name="servicesLink", type=StringType)
Navigation_homeLink: Property = Property(name="homeLink", type=StringType)
Navigation_contactLink: Property = Property(name="contactLink", type=StringType)
Navigation.attributes={Navigation_homeLink, Navigation_servicesLink, Navigation_aboutLink, Navigation_contactLink}

# SearchBar class attributes and methods
SearchBar_placeholder: Property = Property(name="placeholder", type=StringType)
SearchBar.attributes={SearchBar_placeholder}

# Main class attributes and methods
Main_title: Property = Property(name="title", type=StringType)
Main_introduction: Property = Property(name="introduction", type=StringType)
Main_description: Property = Property(name="description", type=StringType)
Main.attributes={Main_introduction, Main_description, Main_title}

# Footer class attributes and methods
Footer_copyright: Property = Property(name="copyright", type=StringType)
Footer_socialLinks: Property = Property(name="socialLinks", type=StringType)
Footer.attributes={Footer_socialLinks, Footer_copyright}

# SocialLinks class attributes and methods
SocialLinks_facebookLink: Property = Property(name="facebookLink", type=StringType)
SocialLinks_twitterLink: Property = Property(name="twitterLink", type=StringType)
SocialLinks_instagramLink: Property = Property(name="instagramLink", type=StringType)
SocialLinks.attributes={SocialLinks_instagramLink, SocialLinks_twitterLink, SocialLinks_facebookLink}

# Relationships
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
footerLink: BinaryAssociation = BinaryAssociation(
    name="footerLink",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)
navLink: BinaryAssociation = BinaryAssociation(
    name="navLink",
    ends={
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1)),
        Property(name="Navigation", type=Navigation, multiplicity=Multiplicity(1, 1))
    }
)
searchLink: BinaryAssociation = BinaryAssociation(
    name="searchLink",
    ends={
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1)),
        Property(name="SearchBar", type=SearchBar, multiplicity=Multiplicity(1, 1))
    }
)
socialLink: BinaryAssociation = BinaryAssociation(
    name="socialLink",
    ends={
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1)),
        Property(name="SocialLinks", type=SocialLinks, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, Header, Navigation, SearchBar, Main, Footer, SocialLinks},
    associations={headerLink, mainLink, footerLink, navLink, searchLink, socialLink},
    generalizations={}
)
