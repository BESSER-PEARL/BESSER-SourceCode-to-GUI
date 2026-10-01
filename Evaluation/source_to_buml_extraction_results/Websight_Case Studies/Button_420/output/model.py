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
WebPage_logo: Property = Property(name="logo", type=StringType)
WebPage_servicesDescription: Property = Property(name="servicesDescription", type=StringType)
WebPage_pricingDescription: Property = Property(name="pricingDescription", type=StringType)
WebPage_reviewsDescription: Property = Property(name="reviewsDescription", type=StringType)
WebPage_homeLink: Property = Property(name="homeLink", type=StringType)
WebPage_servicesLink: Property = Property(name="servicesLink", type=StringType)
WebPage_pricingLink: Property = Property(name="pricingLink", type=StringType)
WebPage_reviewsLink: Property = Property(name="reviewsLink", type=StringType)
WebPage.attributes={WebPage_reviewsLink, WebPage_servicesDescription, WebPage_reviewsDescription, WebPage_pricingDescription, WebPage_logo, WebPage_homeLink, WebPage_servicesLink, WebPage_pricingLink}

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage},
    associations={},
    generalizations={}
)
