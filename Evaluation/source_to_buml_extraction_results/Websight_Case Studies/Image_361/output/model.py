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
Menu = Class(name="Menu")
ProductDisplay = Class(name="ProductDisplay")
ProductCard = Class(name="ProductCard")

# WebPage class attributes and methods

# Menu class attributes and methods

# ProductDisplay class attributes and methods

# ProductCard class attributes and methods
ProductCard_price: Property = Property(name="price", type=FloatType)
ProductCard_image: Property = Property(name="image", type=StringType)
ProductCard_name: Property = Property(name="name", type=StringType)
ProductCard.attributes={ProductCard_price, ProductCard_name, ProductCard_image}

# Relationships
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Menu", type=Menu, multiplicity=Multiplicity(1, 1))
    }
)
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="ProductDisplay", type=ProductDisplay, multiplicity=Multiplicity(1, 1))
    }
)
association3: BinaryAssociation = BinaryAssociation(
    name="association3",
    ends={
        Property(name="ProductDisplay", type=ProductDisplay, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="ProductCard", type=ProductCard, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, Menu, ProductDisplay, ProductCard},
    associations={association1, association2, association3},
    generalizations={}
)
