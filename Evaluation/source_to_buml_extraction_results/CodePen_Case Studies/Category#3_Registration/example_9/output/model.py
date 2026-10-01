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
LoginPage = Class(name="LoginPage")

# LoginPage class attributes and methods
LoginPage_username: Property = Property(name="username", type=StringType)
LoginPage_password: Property = Property(name="password", type=StringType)
LoginPage_firstName: Property = Property(name="firstName", type=StringType)
LoginPage_lastName: Property = Property(name="lastName", type=StringType)
LoginPage_email: Property = Property(name="email", type=StringType)
LoginPage_confirmEmail: Property = Property(name="confirmEmail", type=StringType)
LoginPage_captcha: Property = Property(name="captcha", type=StringType)
LoginPage.attributes={LoginPage_lastName, LoginPage_email, LoginPage_username, LoginPage_password, LoginPage_confirmEmail, LoginPage_captcha, LoginPage_firstName}

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={LoginPage},
    associations={},
    generalizations={}
)
