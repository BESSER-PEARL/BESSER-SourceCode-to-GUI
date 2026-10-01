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
WebPage_navMenuItems: Property = Property(name="navMenuItems", type=StringType)
WebPage_mainAboutUsTitle: Property = Property(name="mainAboutUsTitle", type=StringType)
WebPage_headerLogo: Property = Property(name="headerLogo", type=StringType)
WebPage_mainAboutUsContent: Property = Property(name="mainAboutUsContent", type=StringType)
WebPage_mainOurServicesTitle: Property = Property(name="mainOurServicesTitle", type=StringType)
WebPage_mainOurServicesContent: Property = Property(name="mainOurServicesContent", type=StringType)
WebPage_mainContactUsTitle: Property = Property(name="mainContactUsTitle", type=StringType)
WebPage_mainContactUsContent: Property = Property(name="mainContactUsContent", type=StringType)
WebPage_footerCopyright: Property = Property(name="footerCopyright", type=StringType)
WebPage_footerSocialLinks: Property = Property(name="footerSocialLinks", type=StringType)
WebPage_footerNewsletterEmail: Property = Property(name="footerNewsletterEmail", type=StringType)
WebPage.attributes={WebPage_headerLogo, WebPage_mainOurServicesTitle, WebPage_mainOurServicesContent, WebPage_mainContactUsContent, WebPage_mainAboutUsTitle, WebPage_navMenuItems, WebPage_footerSocialLinks, WebPage_mainContactUsTitle, WebPage_footerCopyright, WebPage_footerNewsletterEmail, WebPage_mainAboutUsContent}

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage},
    associations={},
    generalizations={}
)
