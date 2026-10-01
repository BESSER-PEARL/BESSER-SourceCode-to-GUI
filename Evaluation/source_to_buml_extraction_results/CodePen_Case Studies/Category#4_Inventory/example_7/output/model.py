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
SortingApp = Class(name="SortingApp")

# SortingApp class attributes and methods
SortingApp_name: Property = Property(name="name", type=StringType)
SortingApp_dateAssigned: Property = Property(name="dateAssigned", type=DateType)
SortingApp_amountPaid: Property = Property(name="amountPaid", type=FloatType)
SortingApp_originalBalance: Property = Property(name="originalBalance", type=FloatType)
SortingApp.attributes={SortingApp_amountPaid, SortingApp_originalBalance, SortingApp_name, SortingApp_dateAssigned}

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={SortingApp},
    associations={},
    generalizations={}
)
