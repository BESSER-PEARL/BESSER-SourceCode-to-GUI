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
Section = Class(name="Section")
Footer = Class(name="Footer")

# WebPage class attributes and methods

# Header class attributes and methods

# Navigation class attributes and methods

# Main class attributes and methods

# Section class attributes and methods

# Footer class attributes and methods

# Relationships
comp5: BinaryAssociation = BinaryAssociation(
    name="comp5",
    ends={
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Section", type=Section, multiplicity=Multiplicity(3, 3))
    }
)
comp1: BinaryAssociation = BinaryAssociation(
    name="comp1",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
comp2: BinaryAssociation = BinaryAssociation(
    name="comp2",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Navigation", type=Navigation, multiplicity=Multiplicity(1, 1))
    }
)
comp3: BinaryAssociation = BinaryAssociation(
    name="comp3",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1))
    }
)
comp4: BinaryAssociation = BinaryAssociation(
    name="comp4",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, Header, Navigation, Main, Section, Footer},
    associations={comp5, comp1, comp2, comp3, comp4},
    generalizations={}
)
