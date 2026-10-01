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
ProductCard = Class(name="ProductCard")
ProductList = Class(name="ProductList")

# ProductCard class attributes and methods
ProductCard_title: Property = Property(name="title", type=StringType)
ProductCard_price: Property = Property(name="price", type=StringType)
ProductCard_imageUrl: Property = Property(name="imageUrl", type=StringType)
ProductCard_brand: Property = Property(name="brand", type=StringType)
ProductCard.attributes={ProductCard_brand, ProductCard_price, ProductCard_title, ProductCard_imageUrl}

# ProductList class attributes and methods
ProductList_productCount: Property = Property(name="productCount", type=IntegerType)
ProductList.attributes={ProductList_productCount}

# Relationships
contains: BinaryAssociation = BinaryAssociation(
    name="contains",
    ends={
        Property(name="ProductList", type=ProductList, multiplicity=Multiplicity(1, 1)),
        Property(name="ProductCard", type=ProductCard, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={ProductCard, ProductList},
    associations={contains},
    generalizations={}
)
