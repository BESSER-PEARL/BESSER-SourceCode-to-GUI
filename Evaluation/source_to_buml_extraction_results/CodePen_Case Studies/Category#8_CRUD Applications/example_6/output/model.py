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
UserPage = Class(name="UserPage")
Modal = Class(name="Modal")

# UserPage class attributes and methods
UserPage_name: Property = Property(name="name", type=StringType)
UserPage_address: Property = Property(name="address", type=StringType)
UserPage_age: Property = Property(name="age", type=IntegerType)
UserPage.attributes={UserPage_age, UserPage_address, UserPage_name}

# Modal class attributes and methods

# Relationships
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="UserPage", type=UserPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Modal", type=Modal, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={UserPage, Modal},
    associations={association1},
    generalizations={}
)
