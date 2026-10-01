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
Container = Class(name="Container")
ImageSection = Class(name="ImageSection")
LoginSection = Class(name="LoginSection")
LoginHeader = Class(name="LoginHeader")
Form = Class(name="Form")
FormGroup = Class(name="FormGroup")
ForgotPassword = Class(name="ForgotPassword")
CreateAccount = Class(name="CreateAccount")
AlternativeLogin = Class(name="AlternativeLogin")
SocialLogin = Class(name="SocialLogin")
SocialButton = Class(name="SocialButton")

# LoginPage class attributes and methods

# Container class attributes and methods

# ImageSection class attributes and methods

# LoginSection class attributes and methods

# LoginHeader class attributes and methods

# Form class attributes and methods
Form_username: Property = Property(name="username", type=StringType)
Form_password: Property = Property(name="password", type=StringType)
Form.attributes={Form_password, Form_username}

# FormGroup class attributes and methods

# ForgotPassword class attributes and methods

# CreateAccount class attributes and methods

# AlternativeLogin class attributes and methods

# SocialLogin class attributes and methods

# SocialButton class attributes and methods

# Relationships
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="LoginPage", type=LoginPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Container", type=Container, multiplicity=Multiplicity(1, 1))
    }
)
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="Container", type=Container, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="ImageSection", type=ImageSection, multiplicity=Multiplicity(1, 1))
    }
)
association3: BinaryAssociation = BinaryAssociation(
    name="association3",
    ends={
        Property(name="Container", type=Container, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="LoginSection", type=LoginSection, multiplicity=Multiplicity(1, 1))
    }
)
association4: BinaryAssociation = BinaryAssociation(
    name="association4",
    ends={
        Property(name="LoginSection", type=LoginSection, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="LoginHeader", type=LoginHeader, multiplicity=Multiplicity(1, 1))
    }
)
association5: BinaryAssociation = BinaryAssociation(
    name="association5",
    ends={
        Property(name="LoginSection", type=LoginSection, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Form", type=Form, multiplicity=Multiplicity(1, 1))
    }
)
association8: BinaryAssociation = BinaryAssociation(
    name="association8",
    ends={
        Property(name="LoginSection", type=LoginSection, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="CreateAccount", type=CreateAccount, multiplicity=Multiplicity(1, 1))
    }
)
association9: BinaryAssociation = BinaryAssociation(
    name="association9",
    ends={
        Property(name="LoginSection", type=LoginSection, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="AlternativeLogin", type=AlternativeLogin, multiplicity=Multiplicity(1, 1))
    }
)
association10: BinaryAssociation = BinaryAssociation(
    name="association10",
    ends={
        Property(name="AlternativeLogin", type=AlternativeLogin, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="SocialLogin", type=SocialLogin, multiplicity=Multiplicity(1, 1))
    }
)
association11: BinaryAssociation = BinaryAssociation(
    name="association11",
    ends={
        Property(name="SocialLogin", type=SocialLogin, multiplicity=Multiplicity(2, 2), is_composite=True),
        Property(name="SocialButton", type=SocialButton, multiplicity=Multiplicity(1, 1))
    }
)
association6: BinaryAssociation = BinaryAssociation(
    name="association6",
    ends={
        Property(name="Form", type=Form, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="FormGroup", type=FormGroup, multiplicity=Multiplicity(2, 2))
    }
)
association7: BinaryAssociation = BinaryAssociation(
    name="association7",
    ends={
        Property(name="LoginSection", type=LoginSection, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="ForgotPassword", type=ForgotPassword, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={LoginPage, Container, ImageSection, LoginSection, LoginHeader, Form, FormGroup, ForgotPassword, CreateAccount, AlternativeLogin, SocialLogin, SocialButton},
    associations={association1, association2, association3, association4, association5, association8, association9, association10, association11, association6, association7},
    generalizations={}
)
