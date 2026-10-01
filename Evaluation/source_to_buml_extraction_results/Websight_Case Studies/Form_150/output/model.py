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
ConstructionCompanyPage = Class(name="ConstructionCompanyPage")
Header = Class(name="Header")
Main = Class(name="Main")
Section = Class(name="Section")
Footer = Class(name="Footer")
ContactForm = Class(name="ContactForm")

# ConstructionCompanyPage class attributes and methods

# Header class attributes and methods
Header_title: Property = Property(name="title", type=StringType)
Header.attributes={Header_title}

# Main class attributes and methods

# Section class attributes and methods
Section_imageSrc: Property = Property(name="imageSrc", type=StringType)
Section_description: Property = Property(name="description", type=StringType)
Section.attributes={Section_imageSrc, Section_description}

# Footer class attributes and methods

# ContactForm class attributes and methods
ContactForm_name: Property = Property(name="name", type=StringType)
ContactForm_email: Property = Property(name="email", type=StringType)
ContactForm_message: Property = Property(name="message", type=StringType)
ContactForm.attributes={ContactForm_email, ContactForm_message, ContactForm_name}

# Relationships
header: BinaryAssociation = BinaryAssociation(
    name="header",
    ends={
        Property(name="ConstructionCompanyPage", type=ConstructionCompanyPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
main: BinaryAssociation = BinaryAssociation(
    name="main",
    ends={
        Property(name="ConstructionCompanyPage", type=ConstructionCompanyPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1))
    }
)
footer: BinaryAssociation = BinaryAssociation(
    name="footer",
    ends={
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1)),
        Property(name="ConstructionCompanyPage", type=ConstructionCompanyPage, multiplicity=Multiplicity(1, 1))
    }
)
section: BinaryAssociation = BinaryAssociation(
    name="section",
    ends={
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1)),
        Property(name="Section", type=Section, multiplicity=Multiplicity(2, 2))
    }
)
contactForm: BinaryAssociation = BinaryAssociation(
    name="contactForm",
    ends={
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1)),
        Property(name="ContactForm", type=ContactForm, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={ConstructionCompanyPage, Header, Main, Section, Footer, ContactForm},
    associations={header, main, footer, section, contactForm},
    generalizations={}
)
