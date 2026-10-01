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
FashionRetailerPage = Class(name="FashionRetailerPage")

# FashionRetailerPage class attributes and methods
FashionRetailerPage_title: Property = Property(name="title", type=StringType)
FashionRetailerPage_description: Property = Property(name="description", type=StringType)
FashionRetailerPage_lastUpdated: Property = Property(name="lastUpdated", type=DateTimeType)
FashionRetailerPage_isAvailable: Property = Property(name="isAvailable", type=BooleanType)
FashionRetailerPage_discountRate: Property = Property(name="discountRate", type=FloatType)
FashionRetailerPage.attributes={FashionRetailerPage_title, FashionRetailerPage_lastUpdated, FashionRetailerPage_isAvailable, FashionRetailerPage_discountRate, FashionRetailerPage_description}

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={FashionRetailerPage},
    associations={},
    generalizations={}
)
