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
SearchPage = Class(name="SearchPage")

# SearchPage class attributes and methods
SearchPage_searchWord: Property = Property(name="searchWord", type=StringType)
SearchPage_searchResultsTitle: Property = Property(name="searchResultsTitle", type=StringType)
SearchPage_searchResultsHyperlink: Property = Property(name="searchResultsHyperlink", type=StringType)
SearchPage_searchResultsDescription: Property = Property(name="searchResultsDescription", type=StringType)
SearchPage_reset: Property = Property(name="reset", type=BooleanType)
SearchPage.attributes={SearchPage_searchResultsTitle, SearchPage_reset, SearchPage_searchResultsDescription, SearchPage_searchWord, SearchPage_searchResultsHyperlink}

# Domain Model
domain_model = DomainModel(
    name="DomainModel",
    types={SearchPage},
    associations={},
    generalizations={}
)
