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
Main = Class(name="Main")
AboutSection = Class(name="AboutSection")
ContactSection = Class(name="ContactSection")
Footer = Class(name="Footer")

# WebPage class attributes and methods

# Header class attributes and methods
Header_logo: Property = Property(name="logo", type=StringType)
Header.attributes={Header_logo}

# Navigation class attributes and methods
Navigation_menuItems: Property = Property(name="menuItems", type=StringType)
Navigation.attributes={Navigation_menuItems}

# Main class attributes and methods

# AboutSection class attributes and methods
AboutSection_title: Property = Property(name="title", type=StringType)
AboutSection_content: Property = Property(name="content", type=StringType)
AboutSection.attributes={AboutSection_title, AboutSection_content}

# ContactSection class attributes and methods
ContactSection_title: Property = Property(name="title", type=StringType)
ContactSection_name: Property = Property(name="name", type=StringType)
ContactSection_email: Property = Property(name="email", type=StringType)
ContactSection_message: Property = Property(name="message", type=StringType)
ContactSection.attributes={ContactSection_name, ContactSection_email, ContactSection_title, ContactSection_message}

# Footer class attributes and methods
Footer_contactInformation: Property = Property(name="contactInformation", type=StringType)
Footer_testimonials: Property = Property(name="testimonials", type=StringType)
Footer.attributes={Footer_testimonials, Footer_contactInformation}

# Relationships
header: BinaryAssociation = BinaryAssociation(
    name="header",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
aboutSection: BinaryAssociation = BinaryAssociation(
    name="aboutSection",
    ends={
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1)),
        Property(name="AboutSection", type=AboutSection, multiplicity=Multiplicity(1, 1))
    }
)
navigation: BinaryAssociation = BinaryAssociation(
    name="navigation",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Navigation", type=Navigation, multiplicity=Multiplicity(1, 1))
    }
)
main: BinaryAssociation = BinaryAssociation(
    name="main",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1))
    }
)
footer: BinaryAssociation = BinaryAssociation(
    name="footer",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)
contactSection: BinaryAssociation = BinaryAssociation(
    name="contactSection",
    ends={
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1)),
        Property(name="ContactSection", type=ContactSection, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, Header, Navigation, Main, AboutSection, ContactSection, Footer},
    associations={header, aboutSection, navigation, main, footer, contactSection},
    generalizations={}
)
