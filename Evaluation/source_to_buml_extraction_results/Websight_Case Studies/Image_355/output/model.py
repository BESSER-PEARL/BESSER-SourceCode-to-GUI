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
WebPage_navLinkProducts: Property = Property(name="navLinkProducts", type=StringType)
WebPage_navLinkAboutUs: Property = Property(name="navLinkAboutUs", type=StringType)
WebPage_navLinkContact: Property = Property(name="navLinkContact", type=StringType)
WebPage_productShowcase: Property = Property(name="productShowcase", type=StringType)
WebPage_aboutUs: Property = Property(name="aboutUs", type=StringType)
WebPage_contactPhone: Property = Property(name="contactPhone", type=StringType)
WebPage_contactEmail: Property = Property(name="contactEmail", type=StringType)
WebPage_contactAddress: Property = Property(name="contactAddress", type=StringType)
WebPage.attributes={WebPage_headerImage, WebPage_navLinkProducts, WebPage_aboutUs, WebPage_contactAddress, WebPage_navLinkAboutUs, WebPage_contactPhone, WebPage_navLinkContact, WebPage_productShowcase, WebPage_contactEmail, WebPage_logoImage, WebPage_navLinkHome}

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage},
    associations={},
    generalizations={}
)
