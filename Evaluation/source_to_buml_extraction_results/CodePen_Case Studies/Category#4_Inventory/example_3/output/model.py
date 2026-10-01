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
GroceryInventoryTracker = Class(name="GroceryInventoryTracker")
Item = Class(name="Item")

# GroceryInventoryTracker class attributes and methods

# Item class attributes and methods
Item_name: Property = Property(name="name", type=StringType)
Item_quantity: Property = Property(name="quantity", type=IntegerType)
Item_threshold: Property = Property(name="threshold", type=IntegerType)
Item.attributes={Item_quantity, Item_name, Item_threshold}

# Relationships
manages: BinaryAssociation = BinaryAssociation(
    name="manages",
    ends={
        Property(name="GroceryInventoryTracker", type=GroceryInventoryTracker, multiplicity=Multiplicity(1, 1)),
        Property(name="Item", type=Item, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={GroceryInventoryTracker, Item},
    associations={manages},
    generalizations={}
)
