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
RegistrationForm_addressLine1: Property = Property(name="addressLine1", type=StringType)
RegistrationForm_addressLine2: Property = Property(name="addressLine2", type=StringType)
RegistrationForm_state: Property = Property(name="state", type=StringType)
RegistrationForm_postalCode: Property = Property(name="postalCode", type=StringType)
RegistrationForm_country: Property = Property(name="country", type=StringType)
RegistrationForm_dateOfBirth: Property = Property(name="dateOfBirth", type=DateType)
RegistrationForm_gender: Property = Property(name="gender", type=StringType)
RegistrationForm_countryCode: Property = Property(name="countryCode", type=StringType)
RegistrationForm_phone: Property = Property(name="phone", type=StringType)
RegistrationForm_password: Property = Property(name="password", type=StringType)
RegistrationForm_confirmPassword: Property = Property(name="confirmPassword", type=StringType)
RegistrationForm.attributes={RegistrationForm_countryCode, RegistrationForm_addressLine1, RegistrationForm_country, RegistrationForm_firstName, RegistrationForm_phone, RegistrationForm_addressLine2, RegistrationForm_dateOfBirth, RegistrationForm_password, RegistrationForm_lastName, RegistrationForm_state, RegistrationForm_postalCode, RegistrationForm_gender, RegistrationForm_confirmPassword, RegistrationForm_email}

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={RegistrationForm},
    associations={},
    generalizations={}
)
