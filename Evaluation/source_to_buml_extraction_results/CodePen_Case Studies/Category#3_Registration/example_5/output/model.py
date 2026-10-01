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
RegistrationForm_name: Property = Property(name="name", type=StringType)
RegistrationForm_email: Property = Property(name="email", type=StringType)
RegistrationForm_position: Property = Property(name="position", type=StringType)
RegistrationForm_password: Property = Property(name="password", type=StringType)
RegistrationForm_gender: Property = Property(name="gender", type=StringType)
RegistrationForm_confirmData: Property = Property(name="confirmData", type=BooleanType)
RegistrationForm.attributes={RegistrationForm_position, RegistrationForm_name, RegistrationForm_email, RegistrationForm_password, RegistrationForm_gender, RegistrationForm_confirmData}

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={RegistrationForm},
    associations={},
    generalizations={}
)
