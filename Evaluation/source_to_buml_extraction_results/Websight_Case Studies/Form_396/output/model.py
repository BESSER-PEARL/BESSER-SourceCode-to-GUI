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
FoodDeliveryService = Class(name="FoodDeliveryService")
Header = Class(name="Header")
Main = Class(name="Main")
Footer = Class(name="Footer")

# FoodDeliveryService class attributes and methods

# Header class attributes and methods

# Main class attributes and methods

# Footer class attributes and methods
Footer_email: Property = Property(name="email", type=StringType)
Footer.attributes={Footer_email}

# Relationships
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="FoodDeliveryService", type=FoodDeliveryService, multiplicity=Multiplicity(1, 1)),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="FoodDeliveryService", type=FoodDeliveryService, multiplicity=Multiplicity(1, 1)),
        Property(name="Main", type=Main, multiplicity=Multiplicity(1, 1))
    }
)
association3: BinaryAssociation = BinaryAssociation(
    name="association3",
    ends={
        Property(name="FoodDeliveryService", type=FoodDeliveryService, multiplicity=Multiplicity(1, 1)),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={FoodDeliveryService, Header, Main, Footer},
    associations={association1, association2, association3},
    generalizations={}
)
