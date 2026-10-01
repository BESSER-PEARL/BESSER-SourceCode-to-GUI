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
AuthContainer = Class(name="AuthContainer")
FormWrapper = Class(name="FormWrapper")
FormContainer = Class(name="FormContainer")
FormSide = Class(name="FormSide")
FormHeader = Class(name="FormHeader")
SocialLogin = Class(name="SocialLogin")
FormDivider = Class(name="FormDivider")
FormRow = Class(name="FormRow")
FormGroup = Class(name="FormGroup")
PasswordGroup = Class(name="PasswordGroup")
FormOptions = Class(name="FormOptions")
CheckboxGroup = Class(name="CheckboxGroup")
FormSwitch = Class(name="FormSwitch")

# AuthContainer class attributes and methods

# FormWrapper class attributes and methods

# FormContainer class attributes and methods

# FormSide class attributes and methods

# FormHeader class attributes and methods

# SocialLogin class attributes and methods

# FormDivider class attributes and methods

# FormRow class attributes and methods

# FormGroup class attributes and methods
FormGroup_firstName: Property = Property(name="firstName", type=StringType)
FormGroup_lastName: Property = Property(name="lastName", type=StringType)
FormGroup_emailAddress: Property = Property(name="emailAddress", type=StringType)
FormGroup_password: Property = Property(name="password", type=StringType)
FormGroup.attributes={FormGroup_lastName, FormGroup_emailAddress, FormGroup_password, FormGroup_firstName}

# PasswordGroup class attributes and methods

# FormOptions class attributes and methods

# CheckboxGroup class attributes and methods
CheckboxGroup_remember: Property = Property(name="remember", type=BooleanType)
CheckboxGroup_terms: Property = Property(name="terms", type=BooleanType)
CheckboxGroup.attributes={CheckboxGroup_terms, CheckboxGroup_remember}

# FormSwitch class attributes and methods

# Relationships
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="AuthContainer", type=AuthContainer, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="FormWrapper", type=FormWrapper, multiplicity=Multiplicity(1, 1))
    }
)
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="FormWrapper", type=FormWrapper, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="FormContainer", type=FormContainer, multiplicity=Multiplicity(1, 1))
    }
)
association3: BinaryAssociation = BinaryAssociation(
    name="association3",
    ends={
        Property(name="FormContainer", type=FormContainer, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="FormSide", type=FormSide, multiplicity=Multiplicity(2, 2))
    }
)
association4: BinaryAssociation = BinaryAssociation(
    name="association4",
    ends={
        Property(name="FormSide", type=FormSide, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="FormHeader", type=FormHeader, multiplicity=Multiplicity(1, 1))
    }
)
association5: BinaryAssociation = BinaryAssociation(
    name="association5",
    ends={
        Property(name="FormSide", type=FormSide, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="SocialLogin", type=SocialLogin, multiplicity=Multiplicity(1, 1))
    }
)
association11: BinaryAssociation = BinaryAssociation(
    name="association11",
    ends={
        Property(name="FormSide", type=FormSide, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="FormSwitch", type=FormSwitch, multiplicity=Multiplicity(1, 1))
    }
)
association12: BinaryAssociation = BinaryAssociation(
    name="association12",
    ends={
        Property(name="FormOptions", type=FormOptions, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="CheckboxGroup", type=CheckboxGroup, multiplicity=Multiplicity(1, 1))
    }
)
association6: BinaryAssociation = BinaryAssociation(
    name="association6",
    ends={
        Property(name="FormSide", type=FormSide, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="FormDivider", type=FormDivider, multiplicity=Multiplicity(1, 1))
    }
)
association7: BinaryAssociation = BinaryAssociation(
    name="association7",
    ends={
        Property(name="FormSide", type=FormSide, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="FormRow", type=FormRow, multiplicity=Multiplicity(1, 1))
    }
)
association8: BinaryAssociation = BinaryAssociation(
    name="association8",
    ends={
        Property(name="FormSide", type=FormSide, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="FormGroup", type=FormGroup, multiplicity=Multiplicity(3, 3))
    }
)
association9: BinaryAssociation = BinaryAssociation(
    name="association9",
    ends={
        Property(name="FormSide", type=FormSide, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="PasswordGroup", type=PasswordGroup, multiplicity=Multiplicity(1, 1))
    }
)
association10: BinaryAssociation = BinaryAssociation(
    name="association10",
    ends={
        Property(name="FormSide", type=FormSide, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="FormOptions", type=FormOptions, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={AuthContainer, FormWrapper, FormContainer, FormSide, FormHeader, SocialLogin, FormDivider, FormRow, FormGroup, PasswordGroup, FormOptions, CheckboxGroup, FormSwitch},
    associations={association1, association2, association3, association4, association5, association11, association12, association6, association7, association8, association9, association10},
    generalizations={}
)
