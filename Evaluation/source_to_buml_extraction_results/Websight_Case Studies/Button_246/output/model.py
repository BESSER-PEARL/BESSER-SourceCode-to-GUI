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
Button = Class(name="Button")

# WebPage class attributes and methods
WebPage_title: Property = Property(name="title", type=StringType)
WebPage_description: Property = Property(name="description", type=StringType)
WebPage_imageUrl: Property = Property(name="imageUrl", type=StringType)
WebPage.attributes={WebPage_title, WebPage_description, WebPage_imageUrl}

# Button class attributes and methods
Button_buttonText: Property = Property(name="buttonText", type=StringType)
Button.attributes={Button_buttonText}

# Relationships
contains_1: BinaryAssociation = BinaryAssociation(
    name="contains_1",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Button", type=Button, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, Button},
    associations={contains_1},
    generalizations={}
)
