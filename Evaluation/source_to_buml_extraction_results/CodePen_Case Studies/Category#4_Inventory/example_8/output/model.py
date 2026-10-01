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

# InventoryItem class attributes and methods
InventoryItem_serial: Property = Property(name="serial", type=StringType)
InventoryItem_item_name: Property = Property(name="item_name", type=StringType)
InventoryItem_subtype: Property = Property(name="subtype", type=StringType)
InventoryItem_type: Property = Property(name="type", type=StringType)
InventoryItem_assigned_to: Property = Property(name="assigned_to", type=StringType)
InventoryItem_location: Property = Property(name="location", type=StringType)
InventoryItem_checkout: Property = Property(name="checkout", type=BooleanType)
InventoryItem_quantity: Property = Property(name="quantity", type=IntegerType)
InventoryItem_mac_address: Property = Property(name="mac_address", type=StringType)
InventoryItem_ip_address: Property = Property(name="ip_address", type=StringType)
InventoryItem.attributes={InventoryItem_location, InventoryItem_ip_address, InventoryItem_subtype, InventoryItem_checkout, InventoryItem_type, InventoryItem_serial, InventoryItem_item_name, InventoryItem_quantity, InventoryItem_mac_address, InventoryItem_assigned_to}

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={InventoryItem},
    associations={},
    generalizations={}
)
