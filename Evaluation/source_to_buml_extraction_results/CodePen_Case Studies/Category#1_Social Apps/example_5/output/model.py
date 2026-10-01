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
SocialMediaSharingPage = Class(name="SocialMediaSharingPage")
GeneratedShareLinks = Class(name="GeneratedShareLinks")

# SocialMediaSharingPage class attributes and methods
SocialMediaSharingPage_tweet: Property = Property(name="tweet", type=StringType)
SocialMediaSharingPage_hashtags: Property = Property(name="hashtags", type=StringType)
SocialMediaSharingPage_title: Property = Property(name="title", type=StringType)
SocialMediaSharingPage_summary: Property = Property(name="summary", type=StringType)
SocialMediaSharingPage_url: Property = Property(name="url", type=StringType)
SocialMediaSharingPage.attributes={SocialMediaSharingPage_url, SocialMediaSharingPage_hashtags, SocialMediaSharingPage_title, SocialMediaSharingPage_tweet, SocialMediaSharingPage_summary}

# GeneratedShareLinks class attributes and methods
GeneratedShareLinks_links: Property = Property(name="links", type=StringType)
GeneratedShareLinks.attributes={GeneratedShareLinks_links}

# Relationships
linkGeneration: BinaryAssociation = BinaryAssociation(
    name="linkGeneration",
    ends={
        Property(name="SocialMediaSharingPage", type=SocialMediaSharingPage, multiplicity=Multiplicity(1, 1)),
        Property(name="GeneratedShareLinks", type=GeneratedShareLinks, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={SocialMediaSharingPage, GeneratedShareLinks},
    associations={linkGeneration},
    generalizations={}
)
