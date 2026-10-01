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

# WebPage class attributes and methods
WebPage_headerLogo: Property = Property(name="headerLogo", type=StringType)
WebPage_headerMenu: Property = Property(name="headerMenu", type=StringType)
WebPage_headerOrderNow: Property = Property(name="headerOrderNow", type=StringType)
WebPage_headerBookATruck: Property = Property(name="headerBookATruck", type=StringType)
WebPage_mainTitle: Property = Property(name="mainTitle", type=StringType)
WebPage_mainDescription: Property = Property(name="mainDescription", type=StringType)
WebPage_foodItemName: Property = Property(name="foodItemName", type=StringType)
WebPage_foodItemDescription: Property = Property(name="foodItemDescription", type=StringType)
WebPage_foodItemPrice: Property = Property(name="foodItemPrice", type=FloatType)
WebPage_foodItemImage: Property = Property(name="foodItemImage", type=StringType)
WebPage_footerCopyright: Property = Property(name="footerCopyright", type=StringType)
WebPage.attributes={WebPage_headerLogo, WebPage_footerCopyright, WebPage_foodItemImage, WebPage_foodItemName, WebPage_headerOrderNow, WebPage_headerMenu, WebPage_headerBookATruck, WebPage_foodItemPrice, WebPage_mainTitle, WebPage_foodItemDescription, WebPage_mainDescription}

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage},
    associations={},
    generalizations={}
)
