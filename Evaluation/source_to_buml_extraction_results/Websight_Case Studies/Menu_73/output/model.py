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
Nav = Class(name="Nav")
Main = Class(name="Main")
Section = Class(name="Section")

# WebPage class attributes and methods

# Header class attributes and methods

# Nav class attributes and methods

# Main class attributes and methods

# Section class attributes and methods
Section_title: Property = Property(name="title", type=StringType)
Section_content: Property = Property(name="content", type=StringType)
Section.attributes={Section_content, Section_title}

# Relationships
header: BinaryAssociation = BinaryAssociation(
    name="header",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
nav: BinaryAssociation = BinaryAssociation(
    name="nav",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Nav", type=Nav, multiplicity=Multiplicity(1, 1))
    }
)
main: BinaryAssociation = BinaryAssociation(
    name="main",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1))
    }
)
section: BinaryAssociation = BinaryAssociation(
    name="section",
    ends={
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Section", type=Section, multiplicity=Multiplicity(3, 3))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, Header, Nav, Main, Section},
    associations={header, nav, main, section},
    generalizations={}
)
