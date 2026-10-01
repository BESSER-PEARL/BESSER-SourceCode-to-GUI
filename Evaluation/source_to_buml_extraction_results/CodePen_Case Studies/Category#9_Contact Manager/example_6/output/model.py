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
Contact = Class(name="Contact")
ContactManager = Class(name="ContactManager")

# Contact class attributes and methods
Contact_name: Property = Property(name="name", type=StringType)
Contact_email: Property = Property(name="email", type=StringType)
Contact_phone: Property = Property(name="phone", type=StringType)
Contact_id: Property = Property(name="id", type=IntegerType)
Contact.attributes={Contact_phone, Contact_email, Contact_name, Contact_id}

# ContactManager class attributes and methods
ContactManager_contactCount: Property = Property(name="contactCount", type=IntegerType)
ContactManager.attributes={ContactManager_contactCount}

# Relationships
manages: BinaryAssociation = BinaryAssociation(
    name="manages",
    ends={
        Property(name="ContactManager", type=ContactManager, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Contact", type=Contact, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={Contact, ContactManager},
    associations={manages},
    generalizations={}
)
