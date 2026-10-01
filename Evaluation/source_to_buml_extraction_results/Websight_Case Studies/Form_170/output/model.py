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
Navigation = Class(name="Navigation")
Form = Class(name="Form")
Section = Class(name="Section")

# WebPage class attributes and methods

# Header class attributes and methods

# Main class attributes and methods

# Footer class attributes and methods

# Navigation class attributes and methods

# Form class attributes and methods
Form_searchQuery: Property = Property(name="searchQuery", type=StringType)
Form.attributes={Form_searchQuery}

# Section class attributes and methods
Section_title: Property = Property(name="title", type=StringType)
Section.attributes={Section_title}

# Relationships
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1))
    }
)
association3: BinaryAssociation = BinaryAssociation(
    name="association3",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)
association4: BinaryAssociation = BinaryAssociation(
    name="association4",
    ends={
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1)),
        Property(name="Navigation", type=Navigation, multiplicity=Multiplicity(1, 1))
    }
)
association5: BinaryAssociation = BinaryAssociation(
    name="association5",
    ends={
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1)),
        Property(name="Form", type=Form, multiplicity=Multiplicity(1, 1))
    }
)
association6: BinaryAssociation = BinaryAssociation(
    name="association6",
    ends={
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1)),
        Property(name="Section", type=Section, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, Header, Main, Footer, Navigation, Form, Section},
    associations={association1, association2, association3, association4, association5, association6},
    generalizations={}
)
