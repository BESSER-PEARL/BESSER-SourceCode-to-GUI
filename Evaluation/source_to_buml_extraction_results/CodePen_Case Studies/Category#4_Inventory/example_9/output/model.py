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
InventoryPage = Class(name="InventoryPage")
Sidenav = Class(name="Sidenav")
MainContent = Class(name="MainContent")
Header = Class(name="Header")
Table = Class(name="Table")
Product = Class(name="Product")

# InventoryPage class attributes and methods

# Sidenav class attributes and methods

# MainContent class attributes and methods

# Header class attributes and methods
Header_pageTitle: Property = Property(name="pageTitle", type=StringType)
Header.attributes={Header_pageTitle}

# Table class attributes and methods

# Product class attributes and methods
Product_name: Property = Property(name="name", type=StringType)
Product_category: Property = Property(name="category", type=StringType)
Product.attributes={Product_name, Product_category}

# Relationships
assoc2: BinaryAssociation = BinaryAssociation(
    name="assoc2",
    ends={
        Property(name="InventoryPage", type=InventoryPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="MainContent", type=MainContent, multiplicity=Multiplicity(1, 1))
    }
)
assoc3: BinaryAssociation = BinaryAssociation(
    name="assoc3",
    ends={
        Property(name="MainContent", type=MainContent, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
assoc4: BinaryAssociation = BinaryAssociation(
    name="assoc4",
    ends={
        Property(name="MainContent", type=MainContent, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Table", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
assoc5: BinaryAssociation = BinaryAssociation(
    name="assoc5",
    ends={
        Property(name="Table", type=Table, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Product", type=Product, multiplicity=Multiplicity(0, 9999))
    }
)
assoc1: BinaryAssociation = BinaryAssociation(
    name="assoc1",
    ends={
        Property(name="InventoryPage", type=InventoryPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Sidenav", type=Sidenav, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={InventoryPage, Sidenav, MainContent, Header, Table, Product},
    associations={assoc2, assoc3, assoc4, assoc5, assoc1},
    generalizations={}
)
