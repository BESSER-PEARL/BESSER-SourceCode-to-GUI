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
WebPage_mainSectionTitle: Property = Property(name="mainSectionTitle", type=StringType)
WebPage_footerSocialMediaInfo: Property = Property(name="footerSocialMediaInfo", type=StringType)
WebPage_footerContactInfo: Property = Property(name="footerContactInfo", type=StringType)
WebPage_footerNewsletterInfo: Property = Property(name="footerNewsletterInfo", type=StringType)
WebPage_headerLogo: Property = Property(name="headerLogo", type=StringType)
WebPage_headerNavLinks: Property = Property(name="headerNavLinks", type=StringType)
WebPage_mainImage: Property = Property(name="mainImage", type=StringType)
WebPage.attributes={WebPage_footerNewsletterInfo, WebPage_mainSectionTitle, WebPage_footerSocialMediaInfo, WebPage_footerContactInfo, WebPage_headerLogo, WebPage_mainImage, WebPage_headerNavLinks}

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage},
    associations={},
    generalizations={}
)
