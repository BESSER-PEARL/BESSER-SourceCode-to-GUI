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
WebPage_navLinks: Property = Property(name="navLinks", type=StringType)
WebPage_mainContent: Property = Property(name="mainContent", type=StringType)
WebPage_formFields: Property = Property(name="formFields", type=StringType)
WebPage_reviews: Property = Property(name="reviews", type=StringType)
WebPage_contactInfo: Property = Property(name="contactInfo", type=StringType)
WebPage.attributes={WebPage_reviews, WebPage_navLinks, WebPage_logo, WebPage_mainContent, WebPage_formFields, WebPage_contactInfo}

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage},
    associations={},
    generalizations={}
)
