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
Input = Class(name="Input")
Signup = Class(name="Signup")

# LoginPage class attributes and methods

# Form class attributes and methods

# Input class attributes and methods
Input_uname: Property = Property(name="uname", type=StringType)
Input_psw: Property = Property(name="psw", type=StringType)
Input.attributes={Input_uname, Input_psw}

# Signup class attributes and methods

# Relationships
input_association: BinaryAssociation = BinaryAssociation(
    name="input_association",
    ends={
        Property(name="Form", type=Form, multiplicity=Multiplicity(2, 2), is_composite=True),
        Property(name="Input", type=Input, multiplicity=Multiplicity(2, 2))
    }
)
signup_association: BinaryAssociation = BinaryAssociation(
    name="signup_association",
    ends={
        Property(name="LoginPage", type=LoginPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Signup", type=Signup, multiplicity=Multiplicity(1, 1))
    }
)
form_association: BinaryAssociation = BinaryAssociation(
    name="form_association",
    ends={
        Property(name="LoginPage", type=LoginPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Form", type=Form, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={LoginPage, Form, Input, Signup},
    associations={input_association, signup_association, form_association},
    generalizations={}
)
