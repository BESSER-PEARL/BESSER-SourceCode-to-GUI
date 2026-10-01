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
WebPage_services: Property = Property(name="services", type=StringType)
WebPage_pricing: Property = Property(name="pricing", type=StringType)
WebPage_orderingProcess: Property = Property(name="orderingProcess", type=StringType)
WebPage_image: Property = Property(name="image", type=StringType)
WebPage.attributes={WebPage_orderingProcess, WebPage_services, WebPage_pricing, WebPage_image, WebPage_logo}

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage},
    associations={},
    generalizations={}
)
