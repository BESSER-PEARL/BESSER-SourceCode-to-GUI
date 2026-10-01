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
ECommerceWebsite = Class(name="ECommerceWebsite")
TopNavBar = Class(name="TopNavBar")
SearchBox = Class(name="SearchBox")
MenuBar = Class(name="MenuBar")
MenuItem = Class(name="MenuItem")
Header = Class(name="Header")
SideMenu = Class(name="SideMenu")
Category = Class(name="Category")
SubMenu = Class(name="SubMenu")
Slider = Class(name="Slider")
Carousel = Class(name="Carousel")

# ECommerceWebsite class attributes and methods

# TopNavBar class attributes and methods

# SearchBox class attributes and methods
SearchBox_logo: Property = Property(name="logo", type=StringType)
SearchBox_searchInput: Property = Property(name="searchInput", type=StringType)
SearchBox.attributes={SearchBox_searchInput, SearchBox_logo}

# MenuBar class attributes and methods

# MenuItem class attributes and methods
MenuItem_name: Property = Property(name="name", type=StringType)
MenuItem.attributes={MenuItem_name}

# Header class attributes and methods

# SideMenu class attributes and methods

# Category class attributes and methods
Category_name: Property = Property(name="name", type=StringType)
Category.attributes={Category_name}

# SubMenu class attributes and methods
SubMenu_name: Property = Property(name="name", type=StringType)
SubMenu.attributes={SubMenu_name}

# Slider class attributes and methods

# Carousel class attributes and methods

# Relationships
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="ECommerceWebsite", type=ECommerceWebsite, multiplicity=Multiplicity(1, 1)),
        Property(name="TopNavBar", type=TopNavBar, multiplicity=Multiplicity(1, 1))
    }
)
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="TopNavBar", type=TopNavBar, multiplicity=Multiplicity(1, 1)),
        Property(name="SearchBox", type=SearchBox, multiplicity=Multiplicity(1, 1))
    }
)
association4: BinaryAssociation = BinaryAssociation(
    name="association4",
    ends={
        Property(name="MenuBar", type=MenuBar, multiplicity=Multiplicity(1, 1)),
        Property(name="MenuItem", type=MenuItem, multiplicity=Multiplicity(0, 9999))
    }
)
association5: BinaryAssociation = BinaryAssociation(
    name="association5",
    ends={
        Property(name="ECommerceWebsite", type=ECommerceWebsite, multiplicity=Multiplicity(1, 1)),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
association6: BinaryAssociation = BinaryAssociation(
    name="association6",
    ends={
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1)),
        Property(name="SideMenu", type=SideMenu, multiplicity=Multiplicity(1, 1))
    }
)
association7: BinaryAssociation = BinaryAssociation(
    name="association7",
    ends={
        Property(name="SideMenu", type=SideMenu, multiplicity=Multiplicity(1, 1)),
        Property(name="Category", type=Category, multiplicity=Multiplicity(0, 9999))
    }
)
association8: BinaryAssociation = BinaryAssociation(
    name="association8",
    ends={
        Property(name="Category", type=Category, multiplicity=Multiplicity(1, 1)),
        Property(name="SubMenu", type=SubMenu, multiplicity=Multiplicity(0, 9999))
    }
)
association9: BinaryAssociation = BinaryAssociation(
    name="association9",
    ends={
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1)),
        Property(name="Slider", type=Slider, multiplicity=Multiplicity(1, 1))
    }
)
association10: BinaryAssociation = BinaryAssociation(
    name="association10",
    ends={
        Property(name="Slider", type=Slider, multiplicity=Multiplicity(1, 1)),
        Property(name="Carousel", type=Carousel, multiplicity=Multiplicity(1, 1))
    }
)
association3: BinaryAssociation = BinaryAssociation(
    name="association3",
    ends={
        Property(name="TopNavBar", type=TopNavBar, multiplicity=Multiplicity(1, 1)),
        Property(name="MenuBar", type=MenuBar, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={ECommerceWebsite, TopNavBar, SearchBox, MenuBar, MenuItem, Header, SideMenu, Category, SubMenu, Slider, Carousel},
    associations={association1, association2, association4, association5, association6, association7, association8, association9, association10, association3},
    generalizations={}
)
