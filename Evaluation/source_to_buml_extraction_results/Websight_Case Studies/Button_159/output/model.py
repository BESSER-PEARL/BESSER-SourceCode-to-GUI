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
RealEstatePage = Class(name="RealEstatePage")
Property_ = Class(name="Property")

# RealEstatePage class attributes and methods
RealEstatePage_title: Property = Property(name="title", type=StringType)
RealEstatePage_description: Property = Property(name="description", type=StringType)
RealEstatePage.attributes={RealEstatePage_title, RealEstatePage_description}

# Property class attributes and methods
Property__address: Property = Property(name="address", type=StringType)
Property__price: Property = Property(name="price", type=FloatType)
Property__imageURL: Property = Property(name="imageURL", type=StringType)
Property_.attributes={Property__address, Property__price, Property__imageURL}

# Relationships
contains_1: BinaryAssociation = BinaryAssociation(
    name="contains_1",
    ends={
        Property(name="RealEstatePage", type=RealEstatePage, multiplicity=Multiplicity(1, 1)),
        Property(name="Property", type=Property_, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={RealEstatePage, Property_},
    associations={contains_1},
    generalizations={}
)
