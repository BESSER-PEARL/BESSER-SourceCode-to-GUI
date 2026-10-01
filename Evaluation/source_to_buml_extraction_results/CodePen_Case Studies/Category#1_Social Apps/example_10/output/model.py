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
Submenu = Class(name="Submenu")
SocialMediaLink = Class(name="SocialMediaLink")

# Container class attributes and methods

# Submenu class attributes and methods

# SocialMediaLink class attributes and methods
SocialMediaLink_icon: Property = Property(name="icon", type=StringType)
SocialMediaLink.attributes={SocialMediaLink_icon}

# Relationships
contains_submenu: BinaryAssociation = BinaryAssociation(
    name="contains_submenu",
    ends={
        Property(name="Container", type=Container, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Submenu", type=Submenu, multiplicity=Multiplicity(1, 1))
    }
)
contains_social_media_link: BinaryAssociation = BinaryAssociation(
    name="contains_social_media_link",
    ends={
        Property(name="Submenu", type=Submenu, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="SocialMediaLink", type=SocialMediaLink, multiplicity=Multiplicity(4, 4))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={Container, Submenu, SocialMediaLink},
    associations={contains_submenu, contains_social_media_link},
    generalizations={}
)
