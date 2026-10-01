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
WebPage_communitiesDescription: Property = Property(name="communitiesDescription", type=StringType)
WebPage_agentsDescription: Property = Property(name="agentsDescription", type=StringType)
WebPage_contactDescription: Property = Property(name="contactDescription", type=StringType)
WebPage_logo: Property = Property(name="logo", type=StringType)
WebPage_searchInput: Property = Property(name="searchInput", type=StringType)
WebPage_propertiesDescription: Property = Property(name="propertiesDescription", type=StringType)
WebPage.attributes={WebPage_contactDescription, WebPage_logo, WebPage_agentsDescription, WebPage_searchInput, WebPage_communitiesDescription, WebPage_propertiesDescription}

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={WebPage},
    associations={},
    generalizations={}
)
