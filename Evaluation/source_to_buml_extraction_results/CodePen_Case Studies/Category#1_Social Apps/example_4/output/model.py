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
SignUpPage = Class(name="SignUpPage")
SocialSignIn = Class(name="SocialSignIn")

# SignUpPage class attributes and methods
SignUpPage_email: Property = Property(name="email", type=StringType)
SignUpPage_password: Property = Property(name="password", type=StringType)
SignUpPage_password_confirmation: Property = Property(name="password_confirmation", type=StringType)
SignUpPage.attributes={SignUpPage_password_confirmation, SignUpPage_password, SignUpPage_email}

# SocialSignIn class attributes and methods

# Relationships
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="SignUpPage", type=SignUpPage, multiplicity=Multiplicity(1, 1)),
        Property(name="SocialSignIn", type=SocialSignIn, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={SignUpPage, SocialSignIn},
    associations={association1},
    generalizations={}
)
