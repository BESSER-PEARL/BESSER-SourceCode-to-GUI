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
WebPage_title: Property = Property(name="title", type=StringType)
WebPage_description: Property = Property(name="description", type=StringType)
WebPage_phone: Property = Property(name="phone", type=StringType)
WebPage_email: Property = Property(name="email", type=StringType)
WebPage_video: Property = Property(name="video", type=StringType)
WebPage_navLinks: Property = Property(name="navLinks", type=StringType)
WebPage_heading: Property = Property(name="heading", type=StringType)
WebPage_subheading: Property = Property(name="subheading", type=StringType)
WebPage_contactInfo: Property = Property(name="contactInfo", type=StringType)
WebPage.attributes={WebPage_video, WebPage_title, WebPage_subheading, WebPage_phone, WebPage_contactInfo, WebPage_description, WebPage_navLinks, WebPage_heading, WebPage_email}

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage},
    associations={},
    generalizations={}
)
