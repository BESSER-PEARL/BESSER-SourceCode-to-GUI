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
SideNav = Class(name="SideNav")
MenuItem = Class(name="MenuItem")
SubMenuItem = Class(name="SubMenuItem")

# SideNav class attributes and methods
SideNav_logo: Property = Property(name="logo", type=StringType)
SideNav_toggle: Property = Property(name="toggle", type=StringType)
SideNav.attributes={SideNav_toggle, SideNav_logo}

# MenuItem class attributes and methods
MenuItem_icon: Property = Property(name="icon", type=StringType)
MenuItem_label: Property = Property(name="label", type=StringType)
MenuItem.attributes={MenuItem_icon, MenuItem_label}

# SubMenuItem class attributes and methods
SubMenuItem_label: Property = Property(name="label", type=StringType)
SubMenuItem.attributes={SubMenuItem_label}

# Relationships
containsMenuItem: BinaryAssociation = BinaryAssociation(
    name="containsMenuItem",
    ends={
        Property(name="SideNav", type=SideNav, multiplicity=Multiplicity(1, 1)),
        Property(name="MenuItem", type=MenuItem, multiplicity=Multiplicity(5, 5))
    }
)
containsSubMenuItem: BinaryAssociation = BinaryAssociation(
    name="containsSubMenuItem",
    ends={
        Property(name="MenuItem", type=MenuItem, multiplicity=Multiplicity(1, 1)),
        Property(name="SubMenuItem", type=SubMenuItem, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={SideNav, MenuItem, SubMenuItem},
    associations={containsMenuItem, containsSubMenuItem},
    generalizations={}
)
