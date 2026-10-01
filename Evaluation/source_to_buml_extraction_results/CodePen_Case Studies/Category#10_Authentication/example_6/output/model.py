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
Container = Class(name="Container")
Wrapper = Class(name="Wrapper")
Authentication = Class(name="Authentication")
Card = Class(name="Card")
Form = Class(name="Form")
Note = Class(name="Note")

# Container class attributes and methods

# Wrapper class attributes and methods

# Authentication class attributes and methods

# Card class attributes and methods

# Form class attributes and methods
Form_email: Property = Property(name="email", type=StringType)
Form_password: Property = Property(name="password", type=StringType)
Form_confirmPassword: Property = Property(name="confirmPassword", type=StringType)
Form.attributes={Form_confirmPassword, Form_password, Form_email}

# Note class attributes and methods

# Relationships
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="Container", type=Container, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Wrapper", type=Wrapper, multiplicity=Multiplicity(1, 1))
    }
)
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="Wrapper", type=Wrapper, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Authentication", type=Authentication, multiplicity=Multiplicity(1, 1))
    }
)
association3: BinaryAssociation = BinaryAssociation(
    name="association3",
    ends={
        Property(name="Authentication", type=Authentication, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Card", type=Card, multiplicity=Multiplicity(2, 2))
    }
)
association4: BinaryAssociation = BinaryAssociation(
    name="association4",
    ends={
        Property(name="Card", type=Card, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Wrapper", type=Wrapper, multiplicity=Multiplicity(1, 1))
    }
)
association5: BinaryAssociation = BinaryAssociation(
    name="association5",
    ends={
        Property(name="Wrapper", type=Wrapper, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Form", type=Form, multiplicity=Multiplicity(1, 1))
    }
)
association6: BinaryAssociation = BinaryAssociation(
    name="association6",
    ends={
        Property(name="Wrapper", type=Wrapper, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Note", type=Note, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={Container, Wrapper, Authentication, Card, Form, Note},
    associations={association1, association2, association3, association4, association5, association6},
    generalizations={}
)
