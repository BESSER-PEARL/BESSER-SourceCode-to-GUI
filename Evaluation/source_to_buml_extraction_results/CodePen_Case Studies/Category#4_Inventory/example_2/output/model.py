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
InventoryManagement = Class(name="InventoryManagement")
Navbar = Class(name="Navbar")
Tab = Class(name="Tab")
CurrentInventory = Class(name="CurrentInventory")
IncomingPurchase = Class(name="IncomingPurchase")
OutgoingOrders = Class(name="OutgoingOrders")

# InventoryManagement class attributes and methods

# Navbar class attributes and methods

# Tab class attributes and methods

# CurrentInventory class attributes and methods
CurrentInventory_productName: Property = Property(name="productName", type=StringType)
CurrentInventory_productBrand: Property = Property(name="productBrand", type=StringType)
CurrentInventory_quantity: Property = Property(name="quantity", type=IntegerType)
CurrentInventory_productPrice: Property = Property(name="productPrice", type=FloatType)
CurrentInventory.attributes={CurrentInventory_quantity, CurrentInventory_productName, CurrentInventory_productBrand, CurrentInventory_productPrice}

# IncomingPurchase class attributes and methods
IncomingPurchase_productName: Property = Property(name="productName", type=StringType)
IncomingPurchase_productBrand: Property = Property(name="productBrand", type=StringType)
IncomingPurchase_quantity: Property = Property(name="quantity", type=IntegerType)
IncomingPurchase_productPrice: Property = Property(name="productPrice", type=FloatType)
IncomingPurchase.attributes={IncomingPurchase_productPrice, IncomingPurchase_productBrand, IncomingPurchase_productName, IncomingPurchase_quantity}

# OutgoingOrders class attributes and methods
OutgoingOrders_productName: Property = Property(name="productName", type=StringType)
OutgoingOrders_productBrand: Property = Property(name="productBrand", type=StringType)
OutgoingOrders_quantity: Property = Property(name="quantity", type=IntegerType)
OutgoingOrders_productPrice: Property = Property(name="productPrice", type=FloatType)
OutgoingOrders.attributes={OutgoingOrders_quantity, OutgoingOrders_productBrand, OutgoingOrders_productName, OutgoingOrders_productPrice}

# Relationships
tabLink: BinaryAssociation = BinaryAssociation(
    name="tabLink",
    ends={
        Property(name="InventoryManagement", type=InventoryManagement, multiplicity=Multiplicity(1, 1)),
        Property(name="Tab", type=Tab, multiplicity=Multiplicity(1, 1))
    }
)
currentInventoryLink: BinaryAssociation = BinaryAssociation(
    name="currentInventoryLink",
    ends={
        Property(name="Tab", type=Tab, multiplicity=Multiplicity(1, 1)),
        Property(name="CurrentInventory", type=CurrentInventory, multiplicity=Multiplicity(1, 1))
    }
)
incomingPurchaseLink: BinaryAssociation = BinaryAssociation(
    name="incomingPurchaseLink",
    ends={
        Property(name="Tab", type=Tab, multiplicity=Multiplicity(1, 1)),
        Property(name="IncomingPurchase", type=IncomingPurchase, multiplicity=Multiplicity(1, 1))
    }
)
navLink: BinaryAssociation = BinaryAssociation(
    name="navLink",
    ends={
        Property(name="InventoryManagement", type=InventoryManagement, multiplicity=Multiplicity(1, 1)),
        Property(name="Navbar", type=Navbar, multiplicity=Multiplicity(1, 1))
    }
)
outgoingOrdersLink: BinaryAssociation = BinaryAssociation(
    name="outgoingOrdersLink",
    ends={
        Property(name="Tab", type=Tab, multiplicity=Multiplicity(1, 1)),
        Property(name="OutgoingOrders", type=OutgoingOrders, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={InventoryManagement, Navbar, Tab, CurrentInventory, IncomingPurchase, OutgoingOrders},
    associations={tabLink, currentInventoryLink, incomingPurchaseLink, navLink, outgoingOrdersLink},
    generalizations={}
)
