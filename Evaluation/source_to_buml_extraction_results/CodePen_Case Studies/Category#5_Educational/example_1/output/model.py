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
WebPage = Class(name="WebPage")
Header = Class(name="Header")
Hero = Class(name="Hero")
BestSellers = Class(name="BestSellers")
Item = Class(name="Item")
CallToAction = Class(name="CallToAction")
Chairs = Class(name="Chairs")
Chair = Class(name="Chair")
BackToTop = Class(name="BackToTop")
Footer = Class(name="Footer")
ContactInfo = Class(name="ContactInfo")
SocialMedia = Class(name="SocialMedia")
Logo = Class(name="Logo")
Menu = Class(name="Menu")
MobileMenu = Class(name="MobileMenu")
IconList = Class(name="IconList")

# WebPage class attributes and methods

# Header class attributes and methods

# Hero class attributes and methods

# BestSellers class attributes and methods

# Item class attributes and methods
Item_name: Property = Property(name="name", type=StringType)
Item_description: Property = Property(name="description", type=StringType)
Item.attributes={Item_name, Item_description}

# CallToAction class attributes and methods

# Chairs class attributes and methods

# Chair class attributes and methods
Chair_name: Property = Property(name="name", type=StringType)
Chair_price: Property = Property(name="price", type=FloatType)
Chair.attributes={Chair_name, Chair_price}

# BackToTop class attributes and methods

# Footer class attributes and methods

# ContactInfo class attributes and methods
ContactInfo_address: Property = Property(name="address", type=StringType)
ContactInfo_hours: Property = Property(name="hours", type=StringType)
ContactInfo_phone: Property = Property(name="phone", type=StringType)
ContactInfo_email: Property = Property(name="email", type=StringType)
ContactInfo.attributes={ContactInfo_hours, ContactInfo_email, ContactInfo_phone, ContactInfo_address}

# SocialMedia class attributes and methods

# Logo class attributes and methods

# Menu class attributes and methods

# MobileMenu class attributes and methods

# IconList class attributes and methods

# Relationships
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1))
    }
)
association3: BinaryAssociation = BinaryAssociation(
    name="association3",
    ends={
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Menu", type=Menu, multiplicity=Multiplicity(1, 1))
    }
)
association4: BinaryAssociation = BinaryAssociation(
    name="association4",
    ends={
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="MobileMenu", type=MobileMenu, multiplicity=Multiplicity(1, 1))
    }
)
association5: BinaryAssociation = BinaryAssociation(
    name="association5",
    ends={
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="IconList", type=IconList, multiplicity=Multiplicity(1, 1))
    }
)
association6: BinaryAssociation = BinaryAssociation(
    name="association6",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Hero", type=Hero, multiplicity=Multiplicity(1, 1))
    }
)
association7: BinaryAssociation = BinaryAssociation(
    name="association7",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="BestSellers", type=BestSellers, multiplicity=Multiplicity(1, 1))
    }
)
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="Header", type=Header, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Logo", type=Logo, multiplicity=Multiplicity(1, 1))
    }
)
association9: BinaryAssociation = BinaryAssociation(
    name="association9",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="CallToAction", type=CallToAction, multiplicity=Multiplicity(1, 1))
    }
)
association10: BinaryAssociation = BinaryAssociation(
    name="association10",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Chairs", type=Chairs, multiplicity=Multiplicity(1, 1))
    }
)
association11: BinaryAssociation = BinaryAssociation(
    name="association11",
    ends={
        Property(name="Chairs", type=Chairs, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Chair", type=Chair, multiplicity=Multiplicity(8, 8))
    }
)
association12: BinaryAssociation = BinaryAssociation(
    name="association12",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="BackToTop", type=BackToTop, multiplicity=Multiplicity(1, 1))
    }
)
association8: BinaryAssociation = BinaryAssociation(
    name="association8",
    ends={
        Property(name="BestSellers", type=BestSellers, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Item", type=Item, multiplicity=Multiplicity(6, 6))
    }
)
association14: BinaryAssociation = BinaryAssociation(
    name="association14",
    ends={
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="ContactInfo", type=ContactInfo, multiplicity=Multiplicity(1, 1))
    }
)
association15: BinaryAssociation = BinaryAssociation(
    name="association15",
    ends={
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="SocialMedia", type=SocialMedia, multiplicity=Multiplicity(1, 1))
    }
)
association13: BinaryAssociation = BinaryAssociation(
    name="association13",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, Header, Hero, BestSellers, Item, CallToAction, Chairs, Chair, BackToTop, Footer, ContactInfo, SocialMedia, Logo, Menu, MobileMenu, IconList},
    associations={association1, association3, association4, association5, association6, association7, association2, association9, association10, association11, association12, association8, association14, association15, association13},
    generalizations={}
)
