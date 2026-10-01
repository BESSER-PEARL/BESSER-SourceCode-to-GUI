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
Service = Class(name="Service")

# WebPage class attributes and methods
WebPage_title: Property = Property(name="title", type=StringType)
WebPage_description: Property = Property(name="description", type=StringType)
WebPage.attributes={WebPage_title, WebPage_description}

# Service class attributes and methods
Service_name: Property = Property(name="name", type=StringType)
Service_description: Property = Property(name="description", type=StringType)
Service_icon: Property = Property(name="icon", type=StringType)
Service.attributes={Service_name, Service_icon, Service_description}

# Relationships
includes_1: BinaryAssociation = BinaryAssociation(
    name="includes_1",
    ends={
        Property(name="WebPage", type=WebPage, multiplicity=Multiplicity(1, 1)),
        Property(name="Service", type=Service, multiplicity=Multiplicity(2, 2))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage, Service},
    associations={includes_1},
    generalizations={}
)
