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
ContactManager = Class(name="ContactManager")

# ContactManager class attributes and methods
ContactManager_name: Property = Property(name="name", type=StringType)
ContactManager_email: Property = Property(name="email", type=StringType)
ContactManager_phone: Property = Property(name="phone", type=StringType)
ContactManager.attributes={ContactManager_email, ContactManager_phone, ContactManager_name}

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={ContactManager},
    associations={},
    generalizations={}
)
