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
RegistrationForm_firstname: Property = Property(name="firstname", type=StringType)
RegistrationForm_lastname: Property = Property(name="lastname", type=StringType)
RegistrationForm_phoneno: Property = Property(name="phoneno", type=StringType)
RegistrationForm_email: Property = Property(name="email", type=StringType)
RegistrationForm_password: Property = Property(name="password", type=StringType)
RegistrationForm.attributes={RegistrationForm_password, RegistrationForm_firstname, RegistrationForm_email, RegistrationForm_phoneno, RegistrationForm_lastname}

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={RegistrationForm},
    associations={},
    generalizations={}
)
