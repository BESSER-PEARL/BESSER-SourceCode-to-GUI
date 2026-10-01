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
SocialSection = Class(name="SocialSection")
SocialContainer = Class(name="SocialContainer")
SocialLink = Class(name="SocialLink")

# SocialSection class attributes and methods
SocialSection_id: Property = Property(name="id", type=StringType)
SocialSection.attributes={SocialSection_id}

# SocialContainer class attributes and methods

# SocialLink class attributes and methods
SocialLink_href: Property = Property(name="href", type=StringType)
SocialLink_linkClass: Property = Property(name="linkClass", type=StringType)
SocialLink.attributes={SocialLink_linkClass, SocialLink_href}

# Relationships
contains: BinaryAssociation = BinaryAssociation(
    name="contains",
    ends={
        Property(name="SocialSection", type=SocialSection, multiplicity=Multiplicity(1, 1)),
        Property(name="SocialContainer", type=SocialContainer, multiplicity=Multiplicity(1, 1))
    }
)
includes: BinaryAssociation = BinaryAssociation(
    name="includes",
    ends={
        Property(name="SocialContainer", type=SocialContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="SocialLink", type=SocialLink, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={SocialSection, SocialContainer, SocialLink},
    associations={contains, includes},
    generalizations={}
)
