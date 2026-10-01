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
WebPage = Class(name="WebPage")
RegisterAccount = Class(name="RegisterAccount")
SignForm = Class(name="SignForm")
Left = Class(name="Left")
Right = Class(name="Right")
Form = Class(name="Form")

# WebPage class attributes and methods

# RegisterAccount class attributes and methods

# SignForm class attributes and methods

# Left class attributes and methods

# Right class attributes and methods

# Form class attributes and methods
Form_userName: Property = Property(name="userName", type=StringType)
Form_password: Property = Property(name="password", type=StringType)
Form_rememberMe: Property = Property(name="rememberMe", type=BooleanType)
Form.attributes={Form_password, Form_rememberMe, Form_userName}

# Relationships
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="RegisterAccount", type=RegisterAccount, multiplicity=Multiplicity(1, 1))
    }
)
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="RegisterAccount", type=RegisterAccount, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="SignForm", type=SignForm, multiplicity=Multiplicity(1, 1))
    }
)
association3: BinaryAssociation = BinaryAssociation(
    name="association3",
    ends={
        Property(name="SignForm", type=SignForm, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Left", type=Left, multiplicity=Multiplicity(1, 1))
    }
)
association4: BinaryAssociation = BinaryAssociation(
    name="association4",
    ends={
        Property(name="SignForm", type=SignForm, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Right", type=Right, multiplicity=Multiplicity(1, 1))
    }
)
association5: BinaryAssociation = BinaryAssociation(
    name="association5",
    ends={
        Property(name="Right", type=Right, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Form", type=Form, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, RegisterAccount, SignForm, Left, Right, Form},
    associations={association1, association2, association3, association4, association5},
    generalizations={}
)
