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
Product = Class(name="Product")
Shipping = Class(name="Shipping")
Share = Class(name="Share")

# Product class attributes and methods
Product_quantity: Property = Property(name="quantity", type=IntegerType)
Product_description: Property = Property(name="description", type=StringType)
Product_materials: Property = Property(name="materials", type=StringType)
Product_dimensions: Property = Property(name="dimensions", type=StringType)
Product_image: Property = Property(name="image", type=StringType)
Product_title: Property = Property(name="title", type=StringType)
Product_price: Property = Property(name="price", type=StringType)
Product.attributes={Product_image, Product_price, Product_quantity, Product_description, Product_dimensions, Product_materials, Product_title}

# Shipping class attributes and methods
Shipping_deliveryType: Property = Property(name="deliveryType", type=StringType)
Shipping_cost: Property = Property(name="cost", type=StringType)
Shipping_returnsAndRefunds: Property = Property(name="returnsAndRefunds", type=StringType)
Shipping.attributes={Shipping_cost, Shipping_deliveryType, Shipping_returnsAndRefunds}

# Share class attributes and methods
Share_twitter: Property = Property(name="twitter", type=StringType)
Share_facebook: Property = Property(name="facebook", type=StringType)
Share_instagram: Property = Property(name="instagram", type=StringType)
Share.attributes={Share_facebook, Share_twitter, Share_instagram}

# Relationships
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="Product", type=Product, multiplicity=Multiplicity(1, 1)),
        Property(name="Shipping", type=Shipping, multiplicity=Multiplicity(1, 1))
    }
)
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="Product", type=Product, multiplicity=Multiplicity(1, 1)),
        Property(name="Share", type=Share, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={Product, Shipping, Share},
    associations={association1, association2},
    generalizations={}
)
