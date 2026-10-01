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
Search = Class(name="Search")
ContactList = Class(name="ContactList")

# ContactManager class attributes and methods
ContactManager_name: Property = Property(name="name", type=StringType)
ContactManager_email: Property = Property(name="email", type=StringType)
ContactManager.attributes={ContactManager_name, ContactManager_email}

# Search class attributes and methods
Search_query: Property = Property(name="query", type=StringType)
Search.attributes={Search_query}

# ContactList class attributes and methods
ContactList_totalContacts: Property = Property(name="totalContacts", type=IntegerType)
ContactList.attributes={ContactList_totalContacts}

# Relationships
searchFunctionality: BinaryAssociation = BinaryAssociation(
    name="searchFunctionality",
    ends={
        Property(name="ContactManager", type=ContactManager, multiplicity=Multiplicity(1, 1)),
        Property(name="Search", type=Search, multiplicity=Multiplicity(1, 1))
    }
)
displayContacts: BinaryAssociation = BinaryAssociation(
    name="displayContacts",
    ends={
        Property(name="ContactManager", type=ContactManager, multiplicity=Multiplicity(1, 1)),
        Property(name="ContactList", type=ContactList, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={ContactManager, Search, ContactList},
    associations={searchFunctionality, displayContacts},
    generalizations={}
)
