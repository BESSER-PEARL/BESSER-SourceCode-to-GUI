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
ContactPage = Class(name="ContactPage")
ContactEntry = Class(name="ContactEntry")

# ContactPage class attributes and methods
ContactPage_fullName: Property = Property(name="fullName", type=StringType)
ContactPage_email: Property = Property(name="email", type=StringType)
ContactPage_phoneNumber: Property = Property(name="phoneNumber", type=StringType)
ContactPage_position: Property = Property(name="position", type=StringType)
ContactPage.attributes={ContactPage_phoneNumber, ContactPage_email, ContactPage_fullName, ContactPage_position}

# ContactEntry class attributes and methods
ContactEntry_fullName: Property = Property(name="fullName", type=StringType)
ContactEntry_email: Property = Property(name="email", type=StringType)
ContactEntry_phoneNumber: Property = Property(name="phoneNumber", type=StringType)
ContactEntry_position: Property = Property(name="position", type=StringType)
ContactEntry.attributes={ContactEntry_email, ContactEntry_phoneNumber, ContactEntry_position, ContactEntry_fullName}

# Relationships
formToEntry: BinaryAssociation = BinaryAssociation(
    name="formToEntry",
    ends={
        Property(name="ContactPage", type=ContactPage, multiplicity=Multiplicity(1, 1)),
        Property(name="ContactEntry", type=ContactEntry, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={ContactPage, ContactEntry},
    associations={formToEntry},
    generalizations={}
)
