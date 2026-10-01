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
InventoryItem = Class(name="InventoryItem")
Inventory = Class(name="Inventory")

# InventoryItem class attributes and methods
InventoryItem_number: Property = Property(name="number", type=IntegerType)
InventoryItem_name: Property = Property(name="name", type=StringType)
InventoryItem_price: Property = Property(name="price", type=FloatType)
InventoryItem_quantity: Property = Property(name="quantity", type=IntegerType)
InventoryItem.attributes={InventoryItem_quantity, InventoryItem_name, InventoryItem_number, InventoryItem_price}

# Inventory class attributes and methods
Inventory_query: Property = Property(name="query", type=StringType)
Inventory_itemCount: Property = Property(name="itemCount", type=IntegerType)
Inventory.attributes={Inventory_query, Inventory_itemCount}

# Relationships
contains: BinaryAssociation = BinaryAssociation(
    name="contains",
    ends={
        Property(name="InventoryItem", type=InventoryItem, multiplicity=Multiplicity(1, 1)),
        Property(name="Inventory", type=Inventory, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={InventoryItem, Inventory},
    associations={contains},
    generalizations={}
)
