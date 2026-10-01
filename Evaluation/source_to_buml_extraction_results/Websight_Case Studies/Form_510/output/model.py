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
Section = Class(name="Section")
Form = Class(name="Form")

# WebPage class attributes and methods

# Header class attributes and methods

# Main class attributes and methods

# Footer class attributes and methods

# Navigation class attributes and methods

# Section class attributes and methods

# Form class attributes and methods

# Relationships
containsHeader: BinaryAssociation = BinaryAssociation(
    name="containsHeader",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
containsMain: BinaryAssociation = BinaryAssociation(
    name="containsMain",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1))
    }
)
containsFooter: BinaryAssociation = BinaryAssociation(
    name="containsFooter",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)
includesNavigation: BinaryAssociation = BinaryAssociation(
    name="includesNavigation",
    ends={
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1)),
        Property(name="Navigation", type=Navigation, multiplicity=Multiplicity(1, 1))
    }
)
hasSections: BinaryAssociation = BinaryAssociation(
    name="hasSections",
    ends={
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1)),
        Property(name="Section", type=Section, multiplicity=Multiplicity(2, 2))
    }
)
includesForm: BinaryAssociation = BinaryAssociation(
    name="includesForm",
    ends={
        Property(name="Section", type=Section, multiplicity=Multiplicity(1, 1)),
        Property(name="Form", type=Form, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, Header, Main, Footer, Navigation, Section, Form},
    associations={containsHeader, containsMain, containsFooter, includesNavigation, hasSections, includesForm},
    generalizations={}
)
