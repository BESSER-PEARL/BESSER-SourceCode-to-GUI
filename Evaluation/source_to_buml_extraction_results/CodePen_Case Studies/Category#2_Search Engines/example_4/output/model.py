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
MainPage = Class(name="MainPage")
User = Class(name="User")
Address = Class(name="Address")

# MainPage class attributes and methods
MainPage_search: Property = Property(name="search", type=StringType)
MainPage_loading: Property = Property(name="loading", type=BooleanType)
MainPage_title: Property = Property(name="title", type=StringType)
MainPage.attributes={MainPage_loading, MainPage_search, MainPage_title}

# User class attributes and methods
User_name: Property = Property(name="name", type=StringType)
User_email: Property = Property(name="email", type=StringType)
User.attributes={User_email, User_name}

# Address class attributes and methods
Address_city: Property = Property(name="city", type=StringType)
Address.attributes={Address_city}

# Relationships
userList: BinaryAssociation = BinaryAssociation(
    name="userList",
    ends={
        Property(name="MainPage", type=MainPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="User", type=User, multiplicity=Multiplicity(0, 9999))
    }
)
userAddress: BinaryAssociation = BinaryAssociation(
    name="userAddress",
    ends={
        Property(name="User", type=User, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Address", type=Address, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={MainPage, User, Address},
    associations={userList, userAddress},
    generalizations={}
)
