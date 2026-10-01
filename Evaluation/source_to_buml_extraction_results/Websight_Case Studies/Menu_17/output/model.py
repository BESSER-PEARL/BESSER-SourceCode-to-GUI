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
WebPage_headerImage: Property = Property(name="headerImage", type=StringType)
WebPage_logoImage: Property = Property(name="logoImage", type=StringType)
WebPage_navLinkHome: Property = Property(name="navLinkHome", type=StringType)
WebPage_navLinkServices: Property = Property(name="navLinkServices", type=StringType)
WebPage_navLinkAboutUs: Property = Property(name="navLinkAboutUs", type=StringType)
WebPage_navLinkContact: Property = Property(name="navLinkContact", type=StringType)
WebPage_welcomeMessage: Property = Property(name="welcomeMessage", type=StringType)
WebPage_companyDescription: Property = Property(name="companyDescription", type=StringType)
WebPage_servicesSection: Property = Property(name="servicesSection", type=StringType)
WebPage.attributes={WebPage_navLinkHome, WebPage_companyDescription, WebPage_logoImage, WebPage_navLinkContact, WebPage_welcomeMessage, WebPage_headerImage, WebPage_navLinkServices, WebPage_servicesSection, WebPage_navLinkAboutUs}

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage},
    associations={},
    generalizations={}
)
