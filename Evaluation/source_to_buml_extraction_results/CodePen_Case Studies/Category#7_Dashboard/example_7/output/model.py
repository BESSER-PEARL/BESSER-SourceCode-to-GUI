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
MainPage = Class(name="MainPage")
Menu = Class(name="Menu")
MenuHeader = Class(name="MenuHeader")
MenuBody = Class(name="MenuBody")
Nav = Class(name="Nav")
NavItem = Class(name="NavItem")
Badge = Class(name="Badge")

# MainPage class attributes and methods

# Menu class attributes and methods

# MenuHeader class attributes and methods
MenuHeader_title: Property = Property(name="title", type=StringType)
MenuHeader.attributes={MenuHeader_title}

# MenuBody class attributes and methods

# Nav class attributes and methods

# NavItem class attributes and methods
NavItem_isActive: Property = Property(name="isActive", type=BooleanType)
NavItem.attributes={NavItem_isActive}

# Badge class attributes and methods
Badge_count: Property = Property(name="count", type=IntegerType)
Badge.attributes={Badge_count}

# Relationships
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="MainPage", type=MainPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Menu", type=Menu, multiplicity=Multiplicity(2, 2))
    }
)
association4: BinaryAssociation = BinaryAssociation(
    name="association4",
    ends={
        Property(name="MenuBody", type=MenuBody, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Nav", type=Nav, multiplicity=Multiplicity(1, 1))
    }
)
association5: BinaryAssociation = BinaryAssociation(
    name="association5",
    ends={
        Property(name="Nav", type=Nav, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="NavItem", type=NavItem, multiplicity=Multiplicity(0, 9999))
    }
)
association6: BinaryAssociation = BinaryAssociation(
    name="association6",
    ends={
        Property(name="NavItem", type=NavItem, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Badge", type=Badge, multiplicity=Multiplicity(0, 1))
    }
)
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="Menu", type=Menu, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="MenuHeader", type=MenuHeader, multiplicity=Multiplicity(1, 1))
    }
)
association3: BinaryAssociation = BinaryAssociation(
    name="association3",
    ends={
        Property(name="Menu", type=Menu, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="MenuBody", type=MenuBody, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={MainPage, Menu, MenuHeader, MenuBody, Nav, NavItem, Badge},
    associations={association1, association4, association5, association6, association2, association3},
    generalizations={}
)
