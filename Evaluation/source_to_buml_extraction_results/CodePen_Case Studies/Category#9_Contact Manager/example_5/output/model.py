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
ContactList = Class(name="ContactList")

# ContactManager class attributes and methods
ContactManager_name: Property = Property(name="name", type=StringType)
ContactManager_email: Property = Property(name="email", type=StringType)
ContactManager.attributes={ContactManager_email, ContactManager_name}

# ContactList class attributes and methods
ContactList_contactCount: Property = Property(name="contactCount", type=IntegerType)
ContactList.attributes={ContactList_contactCount}

# Relationships
manages: BinaryAssociation = BinaryAssociation(
    name="manages",
    ends={
        Property(name="ContactManager", type=ContactManager, multiplicity=Multiplicity(1, 1)),
        Property(name="ContactList", type=ContactList, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={ContactManager, ContactList},
    associations={manages},
    generalizations={}
)
