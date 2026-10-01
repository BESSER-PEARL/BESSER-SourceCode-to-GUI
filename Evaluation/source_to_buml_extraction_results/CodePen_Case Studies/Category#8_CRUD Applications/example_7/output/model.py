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
Vehicle = Class(name="Vehicle")

# Vehicle class attributes and methods
Vehicle_make: Property = Property(name="make", type=StringType)
Vehicle_model: Property = Property(name="model", type=StringType)
Vehicle_mileage: Property = Property(name="mileage", type=FloatType)
Vehicle_status: Property = Property(name="status", type=StringType)
Vehicle.attributes={Vehicle_mileage, Vehicle_status, Vehicle_make, Vehicle_model}

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={Vehicle},
    associations={},
    generalizations={}
)
