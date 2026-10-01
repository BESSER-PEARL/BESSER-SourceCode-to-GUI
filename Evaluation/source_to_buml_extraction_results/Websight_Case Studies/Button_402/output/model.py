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
Header = Class(name="Header")
Button = Class(name="Button")
Footer = Class(name="Footer")

# WebPage class attributes and methods

# NavBar class attributes and methods

# Header class attributes and methods
Header_title: Property = Property(name="title", type=StringType)
Header_subtitle: Property = Property(name="subtitle", type=StringType)
Header.attributes={Header_subtitle, Header_title}

# Button class attributes and methods

# Footer class attributes and methods
Footer_text: Property = Property(name="text", type=StringType)
Footer.attributes={Footer_text}

# Relationships
navBar: BinaryAssociation = BinaryAssociation(
    name="navBar",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="NavBar", type=NavBar, multiplicity=Multiplicity(1, 1))
    }
)
header: BinaryAssociation = BinaryAssociation(
    name="header",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
button1: BinaryAssociation = BinaryAssociation(
    name="button1",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Button", type=Button, multiplicity=Multiplicity(2, 2))
    }
)
footer: BinaryAssociation = BinaryAssociation(
    name="footer",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, NavBar, Header, Button, Footer},
    associations={navBar, header, button1, footer},
    generalizations={}
)
