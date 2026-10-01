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
ShareLink = Class(name="ShareLink")

# WebPage class attributes and methods
WebPage_text: Property = Property(name="text", type=StringType)
WebPage_via: Property = Property(name="via", type=StringType)
WebPage_tags: Property = Property(name="tags", type=StringType)
WebPage_url: Property = Property(name="url", type=StringType)
WebPage.attributes={WebPage_tags, WebPage_text, WebPage_via, WebPage_url}

# ShareLink class attributes and methods
ShareLink_platform: Property = Property(name="platform", type=StringType)
ShareLink_linkUrl: Property = Property(name="linkUrl", type=StringType)
ShareLink.attributes={ShareLink_linkUrl, ShareLink_platform}

# Relationships
containsLink: BinaryAssociation = BinaryAssociation(
    name="containsLink",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="ShareLink", type=ShareLink, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, ShareLink},
    associations={containsLink},
    generalizations={}
)
