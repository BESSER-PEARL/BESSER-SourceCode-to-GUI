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
Section = Class(name="Section")
Footer = Class(name="Footer")

# WebPage class attributes and methods

# NavBar class attributes and methods
NavBar_title: Property = Property(name="title", type=StringType)
NavBar.attributes={NavBar_title}

# Header class attributes and methods
Header_subtitle: Property = Property(name="subtitle", type=StringType)
Header_title: Property = Property(name="title", type=StringType)
Header.attributes={Header_title, Header_subtitle}

# Section class attributes and methods
Section_title: Property = Property(name="title", type=StringType)
Section.attributes={Section_title}

# Footer class attributes and methods
Footer_copyright: Property = Property(name="copyright", type=StringType)
Footer.attributes={Footer_copyright}

# Relationships
header: BinaryAssociation = BinaryAssociation(
    name="header",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
navBar: BinaryAssociation = BinaryAssociation(
    name="navBar",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="NavBar", type=NavBar, multiplicity=Multiplicity(1, 1))
    }
)
section: BinaryAssociation = BinaryAssociation(
    name="section",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Section", type=Section, multiplicity=Multiplicity(1, 1))
    }
)
footer: BinaryAssociation = BinaryAssociation(
    name="footer",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, NavBar, Header, Section, Footer},
    associations={header, navBar, section, footer},
    generalizations={}
)
