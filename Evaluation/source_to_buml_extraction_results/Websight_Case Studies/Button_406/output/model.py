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
WebPage_location: Property = Property(name="location", type=StringType)
WebPage_projectTitle: Property = Property(name="projectTitle", type=StringType)
WebPage_projectDescription: Property = Property(name="projectDescription", type=StringType)
WebPage_projectImage: Property = Property(name="projectImage", type=StringType)
WebPage_projectTeam: Property = Property(name="projectTeam", type=StringType)
WebPage_servicesProvided: Property = Property(name="servicesProvided", type=StringType)
WebPage.attributes={WebPage_servicesProvided, WebPage_location, WebPage_projectTitle, WebPage_projectImage, WebPage_projectTeam, WebPage_projectDescription}

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage},
    associations={},
    generalizations={}
)
