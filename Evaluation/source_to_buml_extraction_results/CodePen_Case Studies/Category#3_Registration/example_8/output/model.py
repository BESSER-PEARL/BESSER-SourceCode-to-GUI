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
RegistrationForm_password: Property = Property(name="password", type=StringType)
RegistrationForm_confirmPassword: Property = Property(name="confirmPassword", type=StringType)
RegistrationForm_gender: Property = Property(name="gender", type=StringType)
RegistrationForm_emailAddress: Property = Property(name="emailAddress", type=StringType)
RegistrationForm_phoneNumber: Property = Property(name="phoneNumber", type=StringType)
RegistrationForm_address: Property = Property(name="address", type=StringType)
RegistrationForm_postalCode: Property = Property(name="postalCode", type=StringType)
RegistrationForm_agreedToTerms: Property = Property(name="agreedToTerms", type=BooleanType)
RegistrationForm.attributes={RegistrationForm_emailAddress, RegistrationForm_postalCode, RegistrationForm_agreedToTerms, RegistrationForm_firstName, RegistrationForm_phoneNumber, RegistrationForm_password, RegistrationForm_confirmPassword, RegistrationForm_address, RegistrationForm_lastName, RegistrationForm_gender}

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={RegistrationForm},
    associations={},
    generalizations={}
)
