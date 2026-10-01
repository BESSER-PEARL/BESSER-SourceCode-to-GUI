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
EmailForm = Class(name="EmailForm")

# WebPage class attributes and methods
WebPage_description: Property = Property(name="description", type=StringType)
WebPage_title: Property = Property(name="title", type=StringType)
WebPage.attributes={WebPage_title, WebPage_description}

# EmailForm class attributes and methods
EmailForm_email: Property = Property(name="email", type=StringType)
EmailForm.attributes={EmailForm_email}

# Relationships
contains: BinaryAssociation = BinaryAssociation(
    name="contains",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="EmailForm", type=EmailForm, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, EmailForm},
    associations={contains},
    generalizations={}
)
