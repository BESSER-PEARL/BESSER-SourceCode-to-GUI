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
InventoryList = Class(name="InventoryList")

# InventoryItem class attributes and methods
InventoryItem_itemName: Property = Property(name="itemName", type=StringType)
InventoryItem_quantity: Property = Property(name="quantity", type=IntegerType)
InventoryItem_supplier: Property = Property(name="supplier", type=StringType)
InventoryItem_manufacturer: Property = Property(name="manufacturer", type=StringType)
InventoryItem_id: Property = Property(name="id", type=StringType)
InventoryItem.attributes={InventoryItem_manufacturer, InventoryItem_itemName, InventoryItem_quantity, InventoryItem_id, InventoryItem_supplier}

# InventoryList class attributes and methods
InventoryList_title: Property = Property(name="title", type=StringType)
InventoryList_description: Property = Property(name="description", type=StringType)
InventoryList.attributes={InventoryList_description, InventoryList_title}

# Relationships
contains: BinaryAssociation = BinaryAssociation(
    name="contains",
    ends={
        Property(name="InventoryList", type=InventoryList, multiplicity=Multiplicity(1, 1)),
        Property(name="InventoryItem", type=InventoryItem, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={InventoryItem, InventoryList},
    associations={contains},
    generalizations={}
)
