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
UserSignUp = Class(name="UserSignUp")
GoogleAuth = Class(name="GoogleAuth")

# UserSignUp class attributes and methods
UserSignUp_fname: Property = Property(name="fname", type=StringType)
UserSignUp_lname: Property = Property(name="lname", type=StringType)
UserSignUp_uname: Property = Property(name="uname", type=StringType)
UserSignUp_email: Property = Property(name="email", type=StringType)
UserSignUp_pword: Property = Property(name="pword", type=StringType)
UserSignUp.attributes={UserSignUp_uname, UserSignUp_pword, UserSignUp_lname, UserSignUp_fname, UserSignUp_email}

# GoogleAuth class attributes and methods
GoogleAuth_imageUser: Property = Property(name="imageUser", type=StringType)
GoogleAuth.attributes={GoogleAuth_imageUser}

# Relationships
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="UserSignUp", type=UserSignUp, multiplicity=Multiplicity(1, 1)),
        Property(name="GoogleAuth", type=GoogleAuth, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={UserSignUp, GoogleAuth},
    associations={association1},
    generalizations={}
)
