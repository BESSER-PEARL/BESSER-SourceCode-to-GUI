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
Container = Class(name="Container")
Slider = Class(name="Slider")
ProductInfo = Class(name="ProductInfo")
InfoWrapper = Class(name="InfoWrapper")
Tab = Class(name="Tab")
Content = Class(name="Content")
Buy = Class(name="Buy")

# Container class attributes and methods

# Slider class attributes and methods

# ProductInfo class attributes and methods
ProductInfo_title: Property = Property(name="title", type=StringType)
ProductInfo_price: Property = Property(name="price", type=FloatType)
ProductInfo.attributes={ProductInfo_title, ProductInfo_price}

# InfoWrapper class attributes and methods

# Tab class attributes and methods
Tab_tabId: Property = Property(name="tabId", type=StringType)
Tab_tabName: Property = Property(name="tabName", type=StringType)
Tab.attributes={Tab_tabId, Tab_tabName}

# Content class attributes and methods
Content_description: Property = Property(name="description", type=StringType)
Content_details: Property = Property(name="details", type=StringType)
Content.attributes={Content_description, Content_details}

# Buy class attributes and methods

# Relationships
containsSlider: BinaryAssociation = BinaryAssociation(
    name="containsSlider",
    ends={
        Property(name="Container", type=Container, multiplicity=Multiplicity(1, 1)),
        Property(name="Slider", type=Slider, multiplicity=Multiplicity(1, 1))
    }
)
containsProductInfo: BinaryAssociation = BinaryAssociation(
    name="containsProductInfo",
    ends={
        Property(name="Container", type=Container, multiplicity=Multiplicity(1, 1)),
        Property(name="ProductInfo", type=ProductInfo, multiplicity=Multiplicity(1, 1))
    }
)
hasInfoWrapper: BinaryAssociation = BinaryAssociation(
    name="hasInfoWrapper",
    ends={
        Property(name="ProductInfo", type=ProductInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="InfoWrapper", type=InfoWrapper, multiplicity=Multiplicity(1, 1))
    }
)
wrapsTabs: BinaryAssociation = BinaryAssociation(
    name="wrapsTabs",
    ends={
        Property(name="InfoWrapper", type=InfoWrapper, multiplicity=Multiplicity(1, 1)),
        Property(name="Tab", type=Tab, multiplicity=Multiplicity(2, 2))
    }
)
hasContent: BinaryAssociation = BinaryAssociation(
    name="hasContent",
    ends={
        Property(name="Tab", type=Tab, multiplicity=Multiplicity(1, 1)),
        Property(name="Content", type=Content, multiplicity=Multiplicity(1, 1))
    }
)
includesBuySection: BinaryAssociation = BinaryAssociation(
    name="includesBuySection",
    ends={
        Property(name="ProductInfo", type=ProductInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="Buy", type=Buy, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={Container, Slider, ProductInfo, InfoWrapper, Tab, Content, Buy},
    associations={containsSlider, containsProductInfo, hasInfoWrapper, wrapsTabs, hasContent, includesBuySection},
    generalizations={}
)
