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
AuthenticationPage = Class(name="AuthenticationPage")
Form = Class(name="Form")
Rules = Class(name="Rules")

# AuthenticationPage class attributes and methods

# Form class attributes and methods
Form_username: Property = Property(name="username", type=StringType)
Form_password: Property = Property(name="password", type=StringType)
Form.attributes={Form_username, Form_password}

# Rules class attributes and methods

# Relationships
containsForm: BinaryAssociation = BinaryAssociation(
    name="containsForm",
    ends={
        Property(name="AuthenticationPage", type=AuthenticationPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Form", type=Form, multiplicity=Multiplicity(1, 1))
    }
)
containsRules: BinaryAssociation = BinaryAssociation(
    name="containsRules",
    ends={
        Property(name="AuthenticationPage", type=AuthenticationPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Rules", type=Rules, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={AuthenticationPage, Form, Rules},
    associations={containsForm, containsRules},
    generalizations={}
)
