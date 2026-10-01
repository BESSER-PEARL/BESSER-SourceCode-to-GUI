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
Search = Class(name="Search")
ContactList = Class(name="ContactList")

# Contact class attributes and methods
Contact_age: Property = Property(name="age", type=IntegerType)
Contact_email: Property = Property(name="email", type=StringType)
Contact_city: Property = Property(name="city", type=StringType)
Contact_zipCode: Property = Property(name="zipCode", type=IntegerType)
Contact_country: Property = Property(name="country", type=StringType)
Contact_name: Property = Property(name="name", type=StringType)
Contact.attributes={Contact_country, Contact_email, Contact_city, Contact_age, Contact_name, Contact_zipCode}

# Search class attributes and methods
Search_searchInput: Property = Property(name="searchInput", type=StringType)
Search_matchDisplay: Property = Property(name="matchDisplay", type=StringType)
Search.attributes={Search_searchInput, Search_matchDisplay}

# ContactList class attributes and methods

# Relationships
containsContacts: BinaryAssociation = BinaryAssociation(
    name="containsContacts",
    ends={
        Property(name="ContactList", type=ContactList, multiplicity=Multiplicity(1, 1)),
        Property(name="Contact", type=Contact, multiplicity=Multiplicity(0, 9999))
    }
)
usesSearch: BinaryAssociation = BinaryAssociation(
    name="usesSearch",
    ends={
        Property(name="ContactList", type=ContactList, multiplicity=Multiplicity(1, 1)),
        Property(name="Search", type=Search, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={Contact, Search, ContactList},
    associations={containsContacts, usesSearch},
    generalizations={}
)
