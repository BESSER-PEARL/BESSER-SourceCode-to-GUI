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
RegistrationForm_email: Property = Property(name="email", type=StringType)
RegistrationForm_password: Property = Property(name="password", type=StringType)
RegistrationForm_firstName: Property = Property(name="firstName", type=StringType)
RegistrationForm_lastName: Property = Property(name="lastName", type=StringType)
RegistrationForm_gender: Property = Property(name="gender", type=StringType)
RegistrationForm_country: Property = Property(name="country", type=StringType)
RegistrationForm_agreeTerms: Property = Property(name="agreeTerms", type=BooleanType)
RegistrationForm_receiveNewsletter: Property = Property(name="receiveNewsletter", type=BooleanType)
RegistrationForm.attributes={RegistrationForm_firstName, RegistrationForm_gender, RegistrationForm_email, RegistrationForm_receiveNewsletter, RegistrationForm_country, RegistrationForm_agreeTerms, RegistrationForm_password, RegistrationForm_lastName}

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={RegistrationForm},
    associations={},
    generalizations={}
)
