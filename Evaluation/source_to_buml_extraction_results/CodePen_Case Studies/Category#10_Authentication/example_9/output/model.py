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
MainModal = Class(name="MainModal")
FormImage = Class(name="FormImage")
LoginForm = Class(name="LoginForm")
RegisterForm = Class(name="RegisterForm")
MobileLoginModal = Class(name="MobileLoginModal")

# MainModal class attributes and methods

# FormImage class attributes and methods

# LoginForm class attributes and methods
LoginForm_email: Property = Property(name="email", type=StringType)
LoginForm_password: Property = Property(name="password", type=StringType)
LoginForm_rememberMe: Property = Property(name="rememberMe", type=BooleanType)
LoginForm.attributes={LoginForm_email, LoginForm_rememberMe, LoginForm_password}

# RegisterForm class attributes and methods
RegisterForm_fullName: Property = Property(name="fullName", type=StringType)
RegisterForm_email: Property = Property(name="email", type=StringType)
RegisterForm_password: Property = Property(name="password", type=StringType)
RegisterForm_termsAgree: Property = Property(name="termsAgree", type=BooleanType)
RegisterForm.attributes={RegisterForm_password, RegisterForm_email, RegisterForm_fullName, RegisterForm_termsAgree}

# MobileLoginModal class attributes and methods

# Relationships
assoc1: BinaryAssociation = BinaryAssociation(
    name="assoc1",
    ends={
        Property(name="MainModal", type=MainModal, multiplicity=Multiplicity(1, 1)),
        Property(name="FormImage", type=FormImage, multiplicity=Multiplicity(1, 1))
    }
)
assoc2: BinaryAssociation = BinaryAssociation(
    name="assoc2",
    ends={
        Property(name="MainModal", type=MainModal, multiplicity=Multiplicity(1, 1)),
        Property(name="LoginForm", type=LoginForm, multiplicity=Multiplicity(1, 1))
    }
)
assoc3: BinaryAssociation = BinaryAssociation(
    name="assoc3",
    ends={
        Property(name="MainModal", type=MainModal, multiplicity=Multiplicity(1, 1)),
        Property(name="RegisterForm", type=RegisterForm, multiplicity=Multiplicity(1, 1))
    }
)
assoc4: BinaryAssociation = BinaryAssociation(
    name="assoc4",
    ends={
        Property(name="MainModal", type=MainModal, multiplicity=Multiplicity(1, 1)),
        Property(name="MobileLoginModal", type=MobileLoginModal, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={MainModal, FormImage, LoginForm, RegisterForm, MobileLoginModal},
    associations={assoc1, assoc2, assoc3, assoc4},
    generalizations={}
)
