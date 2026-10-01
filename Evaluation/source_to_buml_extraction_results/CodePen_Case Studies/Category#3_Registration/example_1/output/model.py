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
Form = Class(name="Form")
RegisterForm = Class(name="RegisterForm")
LoginForm = Class(name="LoginForm")

# LoginPage class attributes and methods

# Form class attributes and methods

# RegisterForm class attributes and methods
RegisterForm_password: Property = Property(name="password", type=StringType)
RegisterForm_emailAddress: Property = Property(name="emailAddress", type=StringType)
RegisterForm_name: Property = Property(name="name", type=StringType)
RegisterForm.attributes={RegisterForm_emailAddress, RegisterForm_name, RegisterForm_password}

# LoginForm class attributes and methods
LoginForm_username: Property = Property(name="username", type=StringType)
LoginForm_password: Property = Property(name="password", type=StringType)
LoginForm.attributes={LoginForm_username, LoginForm_password}

# Relationships
containsForm: BinaryAssociation = BinaryAssociation(
    name="containsForm",
    ends={
        Property(name="LoginPage", type=LoginPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Form", type=Form, multiplicity=Multiplicity(1, 1))
    }
)
includesRegisterForm: BinaryAssociation = BinaryAssociation(
    name="includesRegisterForm",
    ends={
        Property(name="Form", type=Form, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="RegisterForm", type=RegisterForm, multiplicity=Multiplicity(1, 1))
    }
)
includesLoginForm: BinaryAssociation = BinaryAssociation(
    name="includesLoginForm",
    ends={
        Property(name="Form", type=Form, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="LoginForm", type=LoginForm, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={LoginPage, Form, RegisterForm, LoginForm},
    associations={containsForm, includesRegisterForm, includesLoginForm},
    generalizations={}
)
