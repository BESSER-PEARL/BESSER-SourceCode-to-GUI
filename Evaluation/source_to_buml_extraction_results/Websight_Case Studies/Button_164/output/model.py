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
Navigation = Class(name="Navigation")
Content = Class(name="Content")

# WebPage class attributes and methods
WebPage_description: Property = Property(name="description", type=StringType)
WebPage_title: Property = Property(name="title", type=StringType)
WebPage.attributes={WebPage_title, WebPage_description}

# Navigation class attributes and methods
Navigation_brandName: Property = Property(name="brandName", type=StringType)
Navigation_menuItemCount: Property = Property(name="menuItemCount", type=IntegerType)
Navigation.attributes={Navigation_brandName, Navigation_menuItemCount}

# Content class attributes and methods
Content_heading: Property = Property(name="heading", type=StringType)
Content_paragraphCount: Property = Property(name="paragraphCount", type=IntegerType)
Content.attributes={Content_paragraphCount, Content_heading}

# Relationships
navLink: BinaryAssociation = BinaryAssociation(
    name="navLink",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Navigation", type=Navigation, multiplicity=Multiplicity(1, 1))
    }
)
contentLink: BinaryAssociation = BinaryAssociation(
    name="contentLink",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Content", type=Content, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, Navigation, Content},
    associations={navLink, contentLink},
    generalizations={}
)
