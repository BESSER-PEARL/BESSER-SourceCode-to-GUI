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
Card = Class(name="Card")
Nav = Class(name="Nav")
Photo = Class(name="Photo")
Description = Class(name="Description")

# Card class attributes and methods

# Nav class attributes and methods

# Photo class attributes and methods

# Description class attributes and methods
Description_title: Property = Property(name="title", type=StringType)
Description_subtitle: Property = Property(name="subtitle", type=StringType)
Description_price: Property = Property(name="price", type=FloatType)
Description_description: Property = Property(name="description", type=StringType)
Description.attributes={Description_description, Description_title, Description_price, Description_subtitle}

# Relationships
navComponent: BinaryAssociation = BinaryAssociation(
    name="navComponent",
    ends={
        Property(name="Card", type=Card, multiplicity=Multiplicity(1, 1)),
        Property(name="Nav", type=Nav, multiplicity=Multiplicity(1, 1))
    }
)
photoComponent: BinaryAssociation = BinaryAssociation(
    name="photoComponent",
    ends={
        Property(name="Card", type=Card, multiplicity=Multiplicity(1, 1)),
        Property(name="Photo", type=Photo, multiplicity=Multiplicity(1, 1))
    }
)
descriptionComponent: BinaryAssociation = BinaryAssociation(
    name="descriptionComponent",
    ends={
        Property(name="Card", type=Card, multiplicity=Multiplicity(1, 1)),
        Property(name="Description", type=Description, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={Card, Nav, Photo, Description},
    associations={navComponent, photoComponent, descriptionComponent},
    generalizations={}
)
