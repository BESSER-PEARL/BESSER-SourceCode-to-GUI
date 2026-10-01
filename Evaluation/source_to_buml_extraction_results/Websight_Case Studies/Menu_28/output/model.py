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
NavBar = Class(name="NavBar")
Sidebar = Class(name="Sidebar")
MainContent = Class(name="MainContent")
Footer = Class(name="Footer")
Image = Class(name="Image")
Form = Class(name="Form")

# WebPage class attributes and methods

# NavBar class attributes and methods

# Sidebar class attributes and methods

# MainContent class attributes and methods

# Footer class attributes and methods

# Image class attributes and methods
Image_src: Property = Property(name="src", type=StringType)
Image_alt: Property = Property(name="alt", type=StringType)
Image.attributes={Image_alt, Image_src}

# Form class attributes and methods
Form_email: Property = Property(name="email", type=StringType)
Form.attributes={Form_email}

# Relationships
navBar: BinaryAssociation = BinaryAssociation(
    name="navBar",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="NavBar", type=NavBar, multiplicity=Multiplicity(1, 1))
    }
)
mainContent: BinaryAssociation = BinaryAssociation(
    name="mainContent",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="MainContent", type=MainContent, multiplicity=Multiplicity(1, 1))
    }
)
sidebar: BinaryAssociation = BinaryAssociation(
    name="sidebar",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Sidebar", type=Sidebar, multiplicity=Multiplicity(1, 1))
    }
)
footer: BinaryAssociation = BinaryAssociation(
    name="footer",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)
images: BinaryAssociation = BinaryAssociation(
    name="images",
    ends={
        Property(name="MainContent", type=MainContent, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Image", type=Image, multiplicity=Multiplicity(4, 4))
    }
)
contactForm: BinaryAssociation = BinaryAssociation(
    name="contactForm",
    ends={
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Form", type=Form, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, NavBar, Sidebar, MainContent, Footer, Image, Form},
    associations={navBar, mainContent, sidebar, footer, images, contactForm},
    generalizations={}
)
