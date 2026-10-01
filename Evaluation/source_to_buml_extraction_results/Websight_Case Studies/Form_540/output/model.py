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
Section = Class(name="Section")
Aside = Class(name="Aside")
Footer = Class(name="Footer")
Form = Class(name="Form")
WebPage = Class(name="WebPage")
Header = Class(name="Header")
Main = Class(name="Main")

# Section class attributes and methods
Section_title: Property = Property(name="title", type=StringType)
Section_description: Property = Property(name="description", type=StringType)
Section.attributes={Section_title, Section_description}

# Aside class attributes and methods
Aside_title: Property = Property(name="title", type=StringType)
Aside.attributes={Aside_title}

# Footer class attributes and methods
Footer_title: Property = Property(name="title", type=StringType)
Footer.attributes={Footer_title}

# Form class attributes and methods
Form_name: Property = Property(name="name", type=StringType)
Form_email: Property = Property(name="email", type=StringType)
Form_message: Property = Property(name="message", type=StringType)
Form.attributes={Form_email, Form_name, Form_message}

# WebPage class attributes and methods

# Header class attributes and methods
Header_title: Property = Property(name="title", type=StringType)
Header.attributes={Header_title}

# Main class attributes and methods

# Relationships
header: BinaryAssociation = BinaryAssociation(
    name="header",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
section: BinaryAssociation = BinaryAssociation(
    name="section",
    ends={
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1)),
        Property(name="Section", type=Section, multiplicity=Multiplicity(1, 1))
    }
)
aside: BinaryAssociation = BinaryAssociation(
    name="aside",
    ends={
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1)),
        Property(name="Aside", type=Aside, multiplicity=Multiplicity(1, 1))
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
contactForm: BinaryAssociation = BinaryAssociation(
    name="contactForm",
    ends={
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1)),
        Property(name="Form", type=Form, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={Section, Aside, Footer, Form, WebPage, Header, Main},
    associations={header, section, aside, main, footer, contactForm},
    generalizations={}
)
