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
FoodDeliveryPage = Class(name="FoodDeliveryPage")
DietaryPreferencesFilter = Class(name="DietaryPreferencesFilter")
LocationFilter = Class(name="LocationFilter")
FoodSection = Class(name="FoodSection")

# FoodDeliveryPage class attributes and methods

# DietaryPreferencesFilter class attributes and methods

# LocationFilter class attributes and methods

# FoodSection class attributes and methods

# Relationships
locFilter: BinaryAssociation = BinaryAssociation(
    name="locFilter",
    ends={
        Property(name="FoodDeliveryPage", type=FoodDeliveryPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="LocationFilter", type=LocationFilter, multiplicity=Multiplicity(1, 1))
    }
)
foodSec: BinaryAssociation = BinaryAssociation(
    name="foodSec",
    ends={
        Property(name="FoodDeliveryPage", type=FoodDeliveryPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="FoodSection", type=FoodSection, multiplicity=Multiplicity(1, 1))
    }
)
dpFilter: BinaryAssociation = BinaryAssociation(
    name="dpFilter",
    ends={
        Property(name="FoodDeliveryPage", type=FoodDeliveryPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="DietaryPreferencesFilter", type=DietaryPreferencesFilter, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={FoodDeliveryPage, DietaryPreferencesFilter, LocationFilter, FoodSection},
    associations={locFilter, foodSec, dpFilter},
    generalizations={}
)
