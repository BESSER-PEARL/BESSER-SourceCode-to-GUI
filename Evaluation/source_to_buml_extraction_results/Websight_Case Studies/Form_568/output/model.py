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
TravelAgencyPage = Class(name="TravelAgencyPage")
Header = Class(name="Header")
Nav = Class(name="Nav")
Main = Class(name="Main")

# TravelAgencyPage class attributes and methods

# Header class attributes and methods

# Nav class attributes and methods

# Main class attributes and methods

# Relationships
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="TravelAgencyPage", type=TravelAgencyPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="TravelAgencyPage", type=TravelAgencyPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Nav", type=Nav, multiplicity=Multiplicity(1, 1))
    }
)
association3: BinaryAssociation = BinaryAssociation(
    name="association3",
    ends={
        Property(name="TravelAgencyPage", type=TravelAgencyPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={TravelAgencyPage, Header, Nav, Main},
    associations={association1, association2, association3},
    generalizations={}
)
