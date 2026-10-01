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
RegistrationForm = Class(name="RegistrationForm")

# RegistrationForm class attributes and methods
RegistrationForm_firstName: Property = Property(name="firstName", type=StringType)
RegistrationForm_lastName: Property = Property(name="lastName", type=StringType)
RegistrationForm_email: Property = Property(name="email", type=StringType)
RegistrationForm_newPassword: Property = Property(name="newPassword", type=StringType)
RegistrationForm_accountType: Property = Property(name="accountType", type=StringType)
RegistrationForm_profilePicture: Property = Property(name="profilePicture", type=StringType)
RegistrationForm_age: Property = Property(name="age", type=IntegerType)
RegistrationForm_referrer: Property = Property(name="referrer", type=StringType)
RegistrationForm_bio: Property = Property(name="bio", type=StringType)
RegistrationForm_termsAndConditions: Property = Property(name="termsAndConditions", type=BooleanType)
RegistrationForm.attributes={RegistrationForm_firstName, RegistrationForm_accountType, RegistrationForm_bio, RegistrationForm_termsAndConditions, RegistrationForm_newPassword, RegistrationForm_profilePicture, RegistrationForm_email, RegistrationForm_age, RegistrationForm_lastName, RegistrationForm_referrer}

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={RegistrationForm},
    associations={},
    generalizations={}
)
