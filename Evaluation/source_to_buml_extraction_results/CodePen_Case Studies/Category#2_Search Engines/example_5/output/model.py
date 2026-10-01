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
AcronymLookupTool = Class(name="AcronymLookupTool")
SearchArea = Class(name="SearchArea")
Footer = Class(name="Footer")

# AcronymLookupTool class attributes and methods
AcronymLookupTool_description: Property = Property(name="description", type=StringType)
AcronymLookupTool_title: Property = Property(name="title", type=StringType)
AcronymLookupTool.attributes={AcronymLookupTool_title, AcronymLookupTool_description}

# SearchArea class attributes and methods
SearchArea_acronymOnly: Property = Property(name="acronymOnly", type=BooleanType)
SearchArea_nameOnly: Property = Property(name="nameOnly", type=BooleanType)
SearchArea_search: Property = Property(name="search", type=StringType)
SearchArea.attributes={SearchArea_acronymOnly, SearchArea_nameOnly, SearchArea_search}

# Footer class attributes and methods
Footer_contactEmail: Property = Property(name="contactEmail", type=StringType)
Footer_poweredBy: Property = Property(name="poweredBy", type=StringType)
Footer_serviceDeskEmail: Property = Property(name="serviceDeskEmail", type=StringType)
Footer.attributes={Footer_serviceDeskEmail, Footer_poweredBy, Footer_contactEmail}

# Relationships
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="AcronymLookupTool", type=AcronymLookupTool, multiplicity=Multiplicity(1, 1)),
        Property(name="SearchArea", type=SearchArea, multiplicity=Multiplicity(1, 1))
    }
)
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="AcronymLookupTool", type=AcronymLookupTool, multiplicity=Multiplicity(1, 1)),
        Property(name="Footer", type=Footer, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={AcronymLookupTool, SearchArea, Footer},
    associations={association1, association2},
    generalizations={}
)
