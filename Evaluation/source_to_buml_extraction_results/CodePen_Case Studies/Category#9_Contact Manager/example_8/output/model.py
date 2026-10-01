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
PhoneBook = Class(name="PhoneBook")

# PhoneBook class attributes and methods
PhoneBook_givenName: Property = Property(name="givenName", type=StringType)
PhoneBook_familyName: Property = Property(name="familyName", type=StringType)
PhoneBook_phoneNumber: Property = Property(name="phoneNumber", type=StringType)
PhoneBook_createdDate: Property = Property(name="createdDate", type=DateType)
PhoneBook_isActive: Property = Property(name="isActive", type=BooleanType)
PhoneBook.attributes={PhoneBook_createdDate, PhoneBook_isActive, PhoneBook_familyName, PhoneBook_phoneNumber, PhoneBook_givenName}

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={PhoneBook},
    associations={},
    generalizations={}
)
