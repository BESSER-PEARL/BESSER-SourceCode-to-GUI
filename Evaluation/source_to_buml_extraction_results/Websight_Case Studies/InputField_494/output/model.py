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
WebPage_headerTitle: Property = Property(name="headerTitle", type=StringType)
WebPage_logoTitle: Property = Property(name="logoTitle", type=StringType)
WebPage_homeLink: Property = Property(name="homeLink", type=StringType)
WebPage_aboutLink: Property = Property(name="aboutLink", type=StringType)
WebPage_servicesLink: Property = Property(name="servicesLink", type=StringType)
WebPage_contactLink: Property = Property(name="contactLink", type=StringType)
WebPage_searchPlaceholder: Property = Property(name="searchPlaceholder", type=StringType)
WebPage_aboutTitle: Property = Property(name="aboutTitle", type=StringType)
WebPage_aboutContent: Property = Property(name="aboutContent", type=StringType)
WebPage_servicesTitle: Property = Property(name="servicesTitle", type=StringType)
WebPage_servicesContent: Property = Property(name="servicesContent", type=StringType)
WebPage_contactTitle: Property = Property(name="contactTitle", type=StringType)
WebPage_contactContent: Property = Property(name="contactContent", type=StringType)
WebPage.attributes={WebPage_logoTitle, WebPage_servicesContent, WebPage_headerTitle, WebPage_aboutTitle, WebPage_contactTitle, WebPage_servicesTitle, WebPage_aboutLink, WebPage_homeLink, WebPage_aboutContent, WebPage_contactContent, WebPage_servicesLink, WebPage_searchPlaceholder, WebPage_contactLink}

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage},
    associations={},
    generalizations={}
)
