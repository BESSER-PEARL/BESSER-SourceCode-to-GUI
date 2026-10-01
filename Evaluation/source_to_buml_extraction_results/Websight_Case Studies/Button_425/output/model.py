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
TravelAgency = Class(name="TravelAgency")
Flights = Class(name="Flights")
Hotels = Class(name="Hotels")
Tours = Class(name="Tours")
Packages = Class(name="Packages")

# TravelAgency class attributes and methods

# Flights class attributes and methods

# Hotels class attributes and methods

# Tours class attributes and methods

# Packages class attributes and methods

# Relationships
containsFlights: BinaryAssociation = BinaryAssociation(
    name="containsFlights",
    ends={
        Property(name="TravelAgency", type=TravelAgency, multiplicity=Multiplicity(1, 1)),
        Property(name="Flights", type=Flights, multiplicity=Multiplicity(1, 1))
    }
)
containsPackages: BinaryAssociation = BinaryAssociation(
    name="containsPackages",
    ends={
        Property(name="Packages", type=Packages, multiplicity=Multiplicity(1, 1)),
        Property(name="TravelAgency", type=TravelAgency, multiplicity=Multiplicity(1, 1))
    }
)
containsHotels: BinaryAssociation = BinaryAssociation(
    name="containsHotels",
    ends={
        Property(name="TravelAgency", type=TravelAgency, multiplicity=Multiplicity(1, 1)),
        Property(name="Hotels", type=Hotels, multiplicity=Multiplicity(1, 1))
    }
)
containsTours: BinaryAssociation = BinaryAssociation(
    name="containsTours",
    ends={
        Property(name="TravelAgency", type=TravelAgency, multiplicity=Multiplicity(1, 1)),
        Property(name="Tours", type=Tours, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={TravelAgency, Flights, Hotels, Tours, Packages},
    associations={containsFlights, containsPackages, containsHotels, containsTours},
    generalizations={}
)
